
import tkinter as tk
from tkinter import ttk, messagebox
import yfinance as yf
import ctypes
import threading
import time

# ══════════════════════════════════════════════════════
# 주식 목록 (미국주식 / 한국주식)
# ══════════════════════════════════════════════════════
미국주식 = {
    "애플":         "AAPL",
    "엔비디아":     "NVDA",
    "마이크로소프트": "MSFT",
    "테슬라":       "TSLA",
    "아마존":       "AMZN",
    "구글":         "GOOGL",
    "메타":         "META",
    "넷플릭스":     "NFLX",
    "AMD":          "AMD",
    "팔란티어":     "PLTR",
    "스타벅스":     "SBUX",
    "코인베이스":   "COIN",
    "버크셔해서웨이": "BRK-B",
    "JP모건":       "JPM",
    "비자":         "V",
}

한국주식 = {
    "삼성전자":   "005930.KS",
    "SK하이닉스": "000660.KS",
    "LG에너지솔루션": "373220.KS",
    "삼성바이오로직스": "207940.KS",
    "현대차":     "005380.KS",
    "카카오":     "035720.KS",
    "네이버":     "035420.KS",
    "기아":       "000270.KS",
    "셀트리온":   "068270.KS",
    "포스코홀딩스": "005490.KS",
    "LG화학":     "051910.KS",
    "삼성SDI":    "006400.KS",
    "현대모비스": "012330.KS",
    "KB금융":     "105560.KS",
    "카카오뱅크": "323410.KS",
    "서호전기" : "065710.KQ"
}

확인간격_초 = 20   # 몇 초마다 가격 확인
알림기준_퍼센트 = 3.0  # 3% 변동 시 알림

# ══════════════════════════════════════════════════════
# 실시간 환율 가져오기 (야후 파이낸스 KRW=X)
# ══════════════════════════════════════════════════════
def 환율가져오기():
    try:
        환율데이터 = yf.Ticker("KRW=X")
        환율 = 환율데이터.history(period='1d')['Close'].iloc[-1]
        return round(환율, 2)
    except:
        return 1530  # 오류시 기본값

# ══════════════════════════════════════════════════════
# 주식 현재가 가져오기
# ══════════════════════════════════════════════════════
def 현재가가져오기(티커코드):
    try:
        종목 = yf.Ticker(티커코드)
        가격 = 종목.history(period='1d')['Close'].iloc[-1]
        return round(float(가격), 4)
    except:
        return None

# ══════════════════════════════════════════════════════
# 윈도우 팝업
# ══════════════════════════════════════════════════════
def 윈도우알림(제목, 내용):
    ctypes.windll.user32.MessageBoxW(0, 내용, 제목, 0x40)  # 0x40 = 파란 ℹ 아이콘

# ══════════════════════════════════════════════════════
# 메인 앱
# ══════════════════════════════════════════════════════
class 주식알림앱:
    def __init__(self, 창):
        self.창 = 창
        self.창.title("주식 실시간 알림봇  |  3% 변동 감지")
        self.창.geometry("780x700")
        self.창.resizable(True, True)
        self.창.configure(bg="#0f0f1a")

        # 감시 상태
        self.감시중 = False
        self.환율 = 환율가져오기()

        # 기준가 저장 {티커: 기준가격}
        self.기준가dict = {}
        # 알림 발생 기록 {티커: True}
        self.알림발생dict = {}

        self.UI만들기()
        self.기준가초기화()

    # ─────────────────────────────
    # UI 전체 구성
    # ─────────────────────────────
    def UI만들기(self):
        # ── 헤더 ──
        헤더 = tk.Frame(self.창, bg="#0f0f1a")
        헤더.pack(fill="x", padx=20, pady=(15, 5))

        tk.Label(헤더, text="주식 실시간 알림봇",
                 font=("맑은 고딕", 20, "bold"),
                 bg="#0f0f1a", fg="#e0e0ff").pack(side="left")

        self.환율라벨 = tk.Label(헤더,
                 text=f"USD/KRW  {self.환율:,.0f}원",
                 font=("맑은 고딕", 10),
                 bg="#0f0f1a", fg="#888aaa")
        self.환율라벨.pack(side="right", pady=5)

        # ── 설명 ──
        tk.Label(self.창,
                 text=f"시작 시 기준가 자동 저장 →  ±{알림기준_퍼센트}% 변동 시 팝업 알림  |  미국주식은 원화 환산 표시",
                 font=("맑은 고딕", 9),
                 bg="#0f0f1a", fg="#555577").pack(pady=(0, 10))

        # ── 탭 (미국/한국) ──
        탭스타일 = ttk.Style()
        탭스타일.theme_use("default")
        탭스타일.configure("TNotebook", background="#0f0f1a", borderwidth=0)
        탭스타일.configure("TNotebook.Tab",
                          background="#1a1a2e", foreground="#888aaa",
                          font=("맑은 고딕", 10, "bold"),
                          padding=[20, 6])
        탭스타일.map("TNotebook.Tab",
                    background=[("selected", "#7c3aed")],
                    foreground=[("selected", "#ffffff")])

        self.탭컨트롤 = ttk.Notebook(self.창)
        self.탭컨트롤.pack(fill="both", expand=True, padx=15, pady=5)

        # 미국 탭
        미국탭 = tk.Frame(self.탭컨트롤, bg="#0f0f1a")
        self.탭컨트롤.add(미국탭, text="🇺🇸  미국 주식")
        self.미국테이블만들기(미국탭)

        # 한국 탭
        한국탭 = tk.Frame(self.탭컨트롤, bg="#0f0f1a")
        self.탭컨트롤.add(한국탭, text="🇰🇷  한국 주식")
        self.한국테이블만들기(한국탭)

        # ── 하단 버튼 + 상태 ──
        하단 = tk.Frame(self.창, bg="#0f0f1a")
        하단.pack(fill="x", padx=20, pady=10)

        self.시작버튼 = tk.Button(
            하단, text="감시 시작",
            font=("맑은 고딕", 13, "bold"),
            bg="#7c3aed", fg="white",
            activebackground="#6d28d9",
            bd=0, padx=30, pady=10,
            cursor="hand2",
            command=self.감시토글
        )
        self.시작버튼.pack(side="left")

        self.상태라벨 = tk.Label(하단,
            text=f"대기 중  |  {확인간격_초}초마다 확인",
            font=("맑은 고딕", 9),
            bg="#0f0f1a", fg="#555577")
        self.상태라벨.pack(side="left", padx=20)

        # 환율 새로고침 버튼
        tk.Button(하단, text="환율 새로고침",
                  font=("맑은 고딕", 9),
                  bg="#1a1a2e", fg="#888aaa",
                  activebackground="#2a2a3e",
                  bd=0, padx=10, pady=5,
                  cursor="hand2",
                  command=self.환율새로고침).pack(side="right")

    # ─────────────────────────────
    # 테이블 만들기 (공통)
    # ─────────────────────────────
    def 테이블만들기_공통(self, 부모프레임):
        스타일 = ttk.Style()
        스타일.configure("Custom.Treeview",
                        background="#12122a",
                        foreground="#ccccee",
                        rowheight=28,
                        fieldbackground="#12122a",
                        font=("맑은 고딕", 9))
        스타일.configure("Custom.Treeview.Heading",
                        background="#1a1a3e",
                        foreground="#aaaacc",
                        font=("맑은 고딕", 9, "bold"))
        스타일.map("Custom.Treeview",
                   background=[("selected", "#3a3a6e")])

        컬럼 = ("종목명", "티커", "현재가(원)", "기준가(원)", "변동률", "상태")
        트리 = ttk.Treeview(부모프레임, columns=컬럼,
                            show="headings", style="Custom.Treeview")

        너비 = {"종목명": 120, "티커": 100, "현재가(원)": 130,
                "기준가(원)": 130, "변동률": 90, "상태": 80}
        for col in 컬럼:
            트리.heading(col, text=col)
            트리.column(col, width=너비[col], anchor="center")

        스크롤 = ttk.Scrollbar(부모프레임, orient="vertical", command=트리.yview)
        트리.configure(yscrollcommand=스크롤.set)
        트리.pack(side="left", fill="both", expand=True)
        스크롤.pack(side="right", fill="y")

        return 트리

    def 미국테이블만들기(self, 탭):
        self.미국트리 = self.테이블만들기_공통(탭)
        for 이름, 티커 in 미국주식.items():
            self.미국트리.insert("", "end", iid=티커,
                values=(이름, 티커, "불러오는 중...", "-", "-", ""))

    def 한국테이블만들기(self, 탭):
        self.한국트리 = self.테이블만들기_공통(탭)
        for 이름, 티커 in 한국주식.items():
            self.한국트리.insert("", "end", iid=티커,
                values=(이름, 티커, "불러오는 중...", "-", "-", "⏸"))

    # ─────────────────────────────
    # 기준가 초기화 (시작할 때 현재가 = 기준가)
    # ─────────────────────────────
    def 기준가초기화(self):
        def 초기화스레드():
            모든주식 = {**미국주식, **한국주식}
            for 이름, 티커 in 모든주식.items():
                가격 = 현재가가져오기(티커)
                if 가격:
                    self.기준가dict[티커] = 가격
                    self.알림발생dict[티커] = False
                    원화가격 = self.원화변환(가격, 티커)
                    트리 = self.미국트리 if 티커 in 미국주식.values() else self.한국트리
                    self.창.after(0, lambda t=트리, tk2=티커, p=원화가격:
                        t.set(tk2, "기준가(원)", f"{p:,.0f}원"))
        threading.Thread(target=초기화스레드, daemon=True).start()

    # ─────────────────────────────
    # 원화 변환 (미국주식만 환율 곱하기)
    # ─────────────────────────────
    def 원화변환(self, 달러가격, 티커):
        if 티커 in 미국주식.values():
            return 달러가격 * self.환율
        return 달러가격  # 한국주식은 이미 원화

    # ─────────────────────────────
    # 감시 시작/정지
    # ─────────────────────────────
    def 감시토글(self):
        if not self.감시중:
            self.감시중 = True
            self.시작버튼.config(text="감시 정지", bg="#dc2626")
            self.상태라벨.config(text=f"감시 중  |  {확인간격_초}초마다 확인  |  ±{알림기준_퍼센트}% 알림",
                                fg="#86efac")
            threading.Thread(target=self.감시루프, daemon=True).start()
        else:
            self.감시중 = False
            self.시작버튼.config(text="감시 시작", bg="#7c3aed")
            self.상태라벨.config(text="정지됨", fg="#555577")

    # ─────────────────────────────
    # 메인 감시 루프
    # ─────────────────────────────
    def 감시루프(self):
        while self.감시중:
            # 환율 주기적으로 업데이트
            self.환율 = 환율가져오기()
            self.창.after(0, lambda:
                self.환율라벨.config(text=f"USD/KRW  {self.환율:,.0f}원"))

            모든주식 = {**미국주식, **한국주식}
            for 이름, 티커 in 모든주식.items():
                if not self.감시중:
                    break

                현재가 = 현재가가져오기(티커)
                if 현재가 is None:
                    continue

                기준가 = self.기준가dict.get(티커)
                if 기준가 is None:
                    self.기준가dict[티커] = 현재가
                    기준가 = 현재가

                원화현재가 = self.원화변환(현재가, 티커)
                원화기준가 = self.원화변환(기준가, 티커)

                # 변동률 계산
                변동률 = ((현재가 - 기준가) / 기준가) * 100
                변동률텍스트 = f"{변동률:+.2f}%"

                # 색깔 결정
                if 변동률 >= 알림기준_퍼센트:
                    상태 = "급등"
                elif 변동률 <= -알림기준_퍼센트:
                    상태 = "급락"
                elif 변동률 > 0:
                    상태 = "상승"
                elif 변동률 < 0:
                    상태 = "하락"
                else:
                    상태 = "보합"

                트리 = self.미국트리 if 티커 in 미국주식.values() else self.한국트리

                # UI 업데이트
                self.창.after(0, lambda t=트리, tk2=티커,
                              cp=원화현재가, bp=원화기준가,
                              ch=변동률텍스트, st=상태:
                    (t.set(tk2, "현재가(원)", f"{cp:,.0f}원"),
                     t.set(tk2, "기준가(원)", f"{bp:,.0f}원"),
                     t.set(tk2, "변동률", ch),
                     t.set(tk2, "상태", st)))

                # 3% 이상 변동 → 팝업 알림 (한 번만)
                if abs(변동률) >= 알림기준_퍼센트 and not self.알림발생dict.get(티커, False):
                    self.알림발생dict[티커] = True
                    방향 = "급등" if 변동률 > 0 else "급락"
                    메시지 = (
                        f"{방향}  {이름} ({티커})\n\n"
                        f"현재가 : {원화현재가:,.0f}원\n"
                        f"기준가 : {원화기준가:,.0f}원\n"
                        f"변동률 : {변동률텍스트}\n\n"
                        f"USD/KRW : {self.환율:,.0f}원"
                    )
                    threading.Thread(
                        target=윈도우알림,
                        args=(f"주식 알림  |  {이름}", 메시지),
                        daemon=True
                    ).start()

            time.sleep(확인간격_초)

    # ─────────────────────────────
    # 환율 새로고침
    # ─────────────────────────────
    def 환율새로고침(self):
        def 새로고침():
            self.환율 = 환율가져오기()
            self.창.after(0, lambda:
                self.환율라벨.config(text=f"USD/KRW  {self.환율:,.0f}원"))
        threading.Thread(target=새로고침, daemon=True).start()


# ══════════════════════════════════════════════════════
# 실행
# ══════════════════════════════════════════════════════
if __name__ == "__main__":
    창 = tk.Tk()
    앱 = 주식알림앱(창)
    창.mainloop()