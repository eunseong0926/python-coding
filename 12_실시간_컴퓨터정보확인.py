# 파이참이란...vscode보다 더 똑똑한 메모장이다.
# 예전에는 무료버전 유료버전 따로 다운로드 받아야 했지만
# 이제는 하나의 버전으로 다운받으면 한달 동안은 무료로 유료버전을 맛보기 체험
# 시키고, 돈을 내지 않으면 무료버전을 사용하게 한다.

#import = 가져오겠다 tkinter = 이 기능을
# 그런데 tkinter 라는 이름이 너~무 길다. as tk 그래서 tk라는 이름으로
# 축소해서 사용하겠다.

import tkinter as tk
import psutil

# 1. 창 만들기
window = tk.Tk()  #window라는 공간에 tkinter에서 만든 기능을 담아두고 필요할때 사용하겠다.

window.title("내 PC 모니터")

#. 2. 글자 표시할 공간 만들기
#. tk.Label() 창 내부에 보여줄 글자 파이썬 개발자가 기능을 만들 때 Label()
#. 반드시 대문자로 시작해야 파이썬 개발자가 만든 Label()도구를 사용할 수 있다
#.tk.Label(   ) = GUI 화면에서 어떤 글자를 작성하여 사용하겠다.
#           어떤창에서, 처음 시작할 글자는 text="" 아무것도 작성하지 않겠다.
# tk.Label(window          ,text="")

라벨 = tk.Label(window,text="")


#. pack = 창 안에 글자 상하좌우 여백을 설정하고 싶을 때 사용
#. 라벨.pack() = 어떤 글자에 여백을 주고 싶은가
#. 라벨.pack(padx=(왼쪽,오른쪽),pady=(위, 아래))
#. 라벨.pack(padx=왼쪽오른쪽모두,pady=위아래모두)
라벨.pack(padx=20,pady=20) # padx = 가로 좌우 여백 pady = 세로 상하 여백
#. 3. 수치를 가져와서 화면에 보여주는 함수
def 업데이트(): #기능이름을 업데이트로 설정하겠다.
    #. psutil = process and System UTILities 줄임말
    # 내 컴퓨터 안을 들여다보는 도구

    # . cpu_percent() = 내 컴퓨터에서 CPU가 얼마나 바쁜지 %로 읽기
    cpu = psutil.cpu_percent()                  # CPU 사용량
    #. virtual_memory() = RAM이 얼마나 바쁜지 .percent %로 읽겠다
    ram = psutil.virtual_memory().percent       # RAM 사용량
    #. disk_usage('C:/') 특정 C 드라이브가 얼마나 꽉찼는지 .percent %로 읽겠다.
    disk = psutil.disk_usage('C:/').percent     # disk 사용량


    #화면에 출력
    # 텍스트 글자안에 다시 설정하겠다. 현재 나의 컴퓨터 상태를
    라벨.config(text=f"CPU : {cpu} %, RAM : {ram} %, Disk : {disk} %")
    # CPU 사용이 50% 넘으면 빨간색, 아니면 검은색
    if cpu > 50 :
        라벨.config(fg="red") #. foreground 글자 색상을 빨간색으로 주겠다.
    else : #. 50미만이면 foreground 글자 색상을 검정색으로 주겠다.
        라벨.config(fg="black")

    #. 1초 뒤에 이 함수를 다시 실행
    window.after( 1000, 업데이트 ) # 현재창을 1초후에 다시 실행하여 실시간으로 화면 상태를 확인하겠다.

#. 4.시작
업데이트()
window.mainloop() # 소비자가 x버튼을 누르기전까지 종료 금지하겠다.
