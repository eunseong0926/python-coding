"""

"""
# 파이참(pyCham) 같은 경우에는  import 한 후 빨간 글씨 위에 마우스를 살짝 올리면 설치해야하는 패키지를 클릭하면 알아서 설치해주기 때문에 따로 pip install 패키지이름을 작성할 필요가 없다.
# 패키지이름 = 도구모음이름

import tkinter
import psutil

window = tkinter.Tk()
window.title("내 PC 모니터")

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# 단축키 ctrl + d = 한줄 복사 만들기
tkinter.Label(window, text=f"CPU : {cpu}%").pack(pady=5)
tkinter.Label(window, text=f"RAM : {ram}%").pack(pady=5)
tkinter.Label(window, text=f"디스크 : {disk}%").pack(pady=5)

window.mainloop()


# 매시간  cpu와 메모리 ram이 실시간으로 감지되지 않는다.
# 매시간 cpu와 메모리 ram변화를 보고 싶어
# 현재 def update가 없는 코드는 창이 열릴 때 딱 한번 수치를 보여주고 끝나는 초기버전



'''
CLI - 키보드만 가능한 창 ex.커멘드창 
GUI - 키보드와 마우스가 가능한 화면 컴퓨터 자체
NUI - 음성인식, 손 터치 이용 가능한 창 대표적 스마트폰 태블릿
OUI - 장치가 필요하지 않은 상태
      핸드폰 없는 스마트폰 스마트워치가 없어도 팔에 전자시계가 보이는 세상 ( 테스트중... )
'''