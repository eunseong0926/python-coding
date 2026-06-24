# 필수 설치
# pip install gTTS pygame

import tkinter as tk
from gtts import gTTS
# from 특정 기능만 꺼내서 가져오겠다 파일이름.py
# import 파일이름.py 에서 가져올 특정기능
# gttp.py에서 gTTS라는 기능만 갖고와
# 사용하기
import pygame

# ─────────────────────────────────────
# 1. 창 만들기
# ─────────────────────────────────────
window = tk.Tk()

window.title("🎤 텍스트 음성 변환기")
window.geometry("500x380")
window.configure(bg="#F2F5F9")   # 배경색
window.resizable(False, False)   # 창 크기 조절 금지

# pygame 준비
pygame.mixer.init()

# ─────────────────────────────────────
# 2. 제목
# ─────────────────────────────────────
제목 = tk.Label(
    window,
    text="🎧 TEXT TO SPEECH",
    font=("맑은 고딕", 22, "bold"),
    bg="#F2F5F9",
    fg="#2C3E50"
)
제목.pack(pady=(25, 10))

# ─────────────────────────────────────
# 3. 안내 문구
# ─────────────────────────────────────
안내라벨 = tk.Label(
    window,
    text="읽어줄 문장을 입력하세요",
    font=("맑은 고딕", 12),
    bg="#F2F5F9",
    fg="#555555"
)
안내라벨.pack(pady=5)

# ─────────────────────────────────────
# 4. 입력창
# ─────────────────────────────────────
입력창 = tk.Entry(
    window,
    width=35,
    font=("맑은 고딕", 15),
    bd=0,
    relief="flat",
    justify="center"
)

입력창.pack(ipady=10, pady=15)

# 입력창 테두리 느낌용 Frame
입력테두리 = tk.Frame(window, bg="#D0D7DE", padx=2, pady=2)

# ─────────────────────────────────────
# 5. 상태 표시 라벨
# ─────────────────────────────────────
상태라벨 = tk.Label(
    window,
    text="",
    font=("맑은 고딕", 11, "bold"),
    bg="#F2F5F9"
)

상태라벨.pack(pady=10)

# ─────────────────────────────────────
# 6. 버튼 기능
# ─────────────────────────────────────
def 읽어주기():

    글자 = 입력창.get()

    # 입력값 확인
    if 글자 == "":
        상태라벨.config(
            text="⚠ 글자를 입력해주세요!",
            fg="red"
        )
        return

    상태라벨.config(
        text="⏳ 음성 변환중...",
        fg="#E67E22"
    )

    window.update()

    # 이전 재생 중지
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # 텍스트 → 음성 변환
    tts = gTTS(text=글자, lang='ko')
    tts.save("변환음성.mp3")

    # 음성 재생
    pygame.mixer.init()
    pygame.mixer.music.load("변환음성.mp3")
    pygame.mixer.music.play()

    상태라벨.config(
        text="🔊 재생중입니다!",
        fg="#27AE60"
    )

# ─────────────────────────────────────
# 7. 버튼 Hover 효과
# ─────────────────────────────────────
def 버튼들어감(e):
    버튼.config(bg="#2980B9")

def 버튼나감(e):
    버튼.config(bg="#3498DB")

# ─────────────────────────────────────
# 8. 버튼 만들기
# ─────────────────────────────────────
버튼 = tk.Button(
    window,
    text="🔊 음성 재생",
    font=("맑은 고딕", 14, "bold"),
    bg="#3498DB",
    fg="white",
    activebackground="#2980B9",
    activeforeground="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    command=읽어주기
)

버튼.pack(pady=20)

# 마우스 올리면 색상 변경
버튼.bind("<Enter>", 버튼들어감)
버튼.bind("<Leave>", 버튼나감)

# ─────────────────────────────────────
# 9. 하단 설명
# ─────────────────────────────────────
하단글자 = tk.Label(
    window,
    text="Python + gTTS + pygame",
    font=("맑은 고딕", 10),
    bg="#F2F5F9",
    fg="gray"
)

하단글자.pack(side="bottom", pady=15)

# ─────────────────────────────────────
# 10. 시작
# ─────────────────────────────────────
window.mainloop()