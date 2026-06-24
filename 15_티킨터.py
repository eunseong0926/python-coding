"""
Tool Kit INTERface
파이썬으로 창(윈도우)을 만드는 도구
"""

import tkinter as tk
window = tk.Tk()
window.title("내 첫 창")

# def Label(창화면, text="")
라벨 = tk.Label(window, text="안녕하세요")
라벨.pack(padx=50, pady=50)
def 클릭버튼():
    print("버튼 눌렀어요!")
버튼 = tk.Button(window, text="눌러보세요", command=클릭버튼)
버튼.pack()
window.mainloop()
