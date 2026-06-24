import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import threading
import time
import ctypes

import matplotlib
import mplfinance as mpf
import matplotlib.pyplot as plt

# ==============================
# 🔥 한글 깨짐 방지
# ==============================
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False


# ==============================
# 주식 목록
# ==============================
미국주식 = {
    "애플": "AAPL",
    "엔비디아": "NVDA",
    "테슬라": "TSLA",
    "아마존": "AMZN",
}

한국주식 = {
    "삼성전자": "005930.KS",
    "SK하이닉스": "000660.KS",
    "네이버": "035420.KS",
    "카카오": "035720.KS"
}

확인간격_초 = 20
알림기준_퍼센트 = 3.0


# ==============================
def 알림(title, msg):
    ctypes.windll.user32.MessageBoxW(0, msg, title, 0x40)


def 현재가(ticker):
    try:
        return yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1]
    except:
        return None


# ==============================
# 📊 트레이딩뷰 스타일 차트 (중복 제목 완전 제거 버전)
# ==============================
def 트레이딩뷰차트(ticker):
    try:
        df = yf.Ticker(ticker).history(period="6mo", interval="1d")

        if df.empty:
            messagebox.showerror("오류", "데이터 없음")
            return

        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

        # 이동평균
        ma5 = df['Close'].rolling(5).mean()
        ma20 = df['Close'].rolling(20).mean()

        addplots = [
            mpf.make_addplot(ma5, color='dodgerblue'),
            mpf.make_addplot(ma20, color='orange')
        ]

        style = mpf.make_mpf_style(
            base_mpf_style='nightclouds',
            facecolor='#0f0f1a',
            gridstyle='--',
            rc={'font.family': 'Malgun Gothic'}
        )

        # ✔ 핵심: returnfig=True로 직접 제어
        fig, axes = mpf.plot(
            df,
            type='candle',
            style=style,
            volume=True,
            addplot=addplots,
            returnfig=True,
            figsize=(11, 6),
            tight_layout=True
        )

        # ✔ 중복 제목 제거 핵심
        fig.suptitle(f"{ticker}", fontsize=14, color="white")

        for ax in axes:
            ax.set_title("")  # 내부 제목 완전 삭제

        plt.show()

    except Exception as e:
        messagebox.showerror("에러", str(e))


# ==============================
class 앱:
    def __init__(self, root):
        self.root = root
        self.root.title("TradingView Stock Monitor")
        self.root.geometry("850x700")

        self.running = False
        self.base = {}

        self.ui()
        self.init_base()

    # ================= UI =================
    def ui(self):
        top = tk.Frame(self.root)
        top.pack(fill="x")

        tk.Label(top, text="🔥 TradingView Stock Monitor",
                 font=("Arial", 16, "bold")).pack(side="left")

        self.nb = ttk.Notebook(self.root)
        self.nb.pack(fill="both", expand=True)

        self.us = tk.Frame(self.nb)
        self.kr = tk.Frame(self.nb)

        self.nb.add(self.us, text="미국")
        self.nb.add(self.kr, text="한국")

        self.us_tree = self.make_table(self.us)
        self.kr_tree = self.make_table(self.kr)

        # ✔ 더블클릭 → 차트
        self.us_tree.bind("<Double-1>", self.open_chart)
        self.kr_tree.bind("<Double-1>", self.open_chart)

        btn = tk.Button(self.root, text="감시 시작", command=self.toggle)
        btn.pack(pady=10)

    # ================= table =================
    def make_table(self, parent):
        cols = ("이름", "티커", "현재", "기준", "변동", "상태")
        tree = ttk.Treeview(parent, columns=cols, show="headings")

        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=120)

        tree.pack(fill="both", expand=True)
        return tree

    # ================= 기준가 =================
    def init_base(self):
        def run():
            for n, t in {**미국주식, **한국주식}.items():
                p = 현재가(t)
                if p:
                    self.base[t] = p

        threading.Thread(target=run, daemon=True).start()

    # ================= chart =================
    def open_chart(self, event):
        item = event.widget.selection()
        if item:
            ticker = item[0]
            threading.Thread(target=트레이딩뷰차트, args=(ticker,), daemon=True).start()

    # ================= loop =================
    def toggle(self):
        self.running = not self.running
        if self.running:
            threading.Thread(target=self.loop, daemon=True).start()

    def loop(self):
        while self.running:

            for name, t in {**미국주식, **한국주식}.items():
                now = 현재가(t)
                base = self.base.get(t, now)

                if not now:
                    continue

                diff = (now - base) / base * 100

                tree = self.us_tree if t in 미국주식.values() else self.kr_tree

                self.root.after(0, lambda tr=tree, tk=t, n=now, b=base, d=diff:
                    tr.insert("", "end", iid=tk,
                              values=(name, tk, n, b, f"{d:.2f}%", "상승" if d > 0 else "하락")))

                if abs(diff) >= 알림기준_퍼센트:
                    알림("주식 알림", f"{name} {diff:.2f}%")

            time.sleep(확인간격_초)


# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = 앱(root)
    root.mainloop()