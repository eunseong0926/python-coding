"""
책에는  win10toast를 사용해서
윈도우10에서 알림받기를 해라

윈도우 11이나 10버전이 아닌 윈도우에서는 사용이 안된다.
실제로 토스트와 같은 기능은 설치하지 않아도 파이썬에서 기본으로
내장되어 있는 알린을 사용해도 된다.

토스트(Toast)
- 구운 빵
- 건배 축배 누군가의 건강을 기원하거나 축하하면 잔을 올리는 행위
- you're toast 너는 이제 끝났어. 망했어 속어
- it 업계에서는 스마트폰 화면 하단에 잠깐 나타났다가 사라지는 알림팝업의 의미로 사용되어진다.
"""

# win10toast는 윈도우 10이외에는 안된다.
import ctypes
def 윈도우봇():
    """
    ctypes = 파이썬이 윈도우 컴퓨터 운영체제 기능을 직접 사용할 수 있게 해주는 도구
    컴퓨터를 자유롭게 조작할 수 있는 기능

    windll = 윈도우 기능이 들어있는 창고
         창고 안에 있는 기능들 중에서 
    user32 = 화면/팝업 감강 기능
        MessageBoxW = 팝업창 띄우기 기능
    """
    ctypes.windll.user32.MessageBoxW(
        0,                   # 부모 창 없음 맨 앞에 0으로 표기
        "잠시 쉬어가세요~^^", # 팝업 창 안에 쓸 내용
        "알림창",   # 팝업창 제목
        1           # 버튼종료
        )
"""
버튼 종류에는 5가지 버튼 종류가 있다.
0 확인
1 확인 + 취소
2 중단 + 재시도 + 무시
3 예 + 아니오 + 취소
4 예 + 아니오

"""
import subprocess #파이썬이 맥 운영체제한테 명령 내리는 도구
# 윈도우의 ctypes와 동일한 기능을 제공
def 맥북_1():
    # subprocess.run 맥북한테 이거 실행해줘@
    # 'osascript' 윈도우에서 windll.user32와 같은 역할
    # display dialog 팝업창 보여줘 맥 명령어
    subprocess.run('osascript','-e','display dialog "잠시 쉬어가세요.^^" with tile "알림" buttons {"취소","확인"}')

import os
def 맥북_2():
    os.system( 'osascript','-e \'display dialog "잠시 쉬어가세요.^^" with tile "알림"\'' )

def 맥북_버튼추가():
    os.system( 'osascript','-e \'display dialog "잠시 쉬어가세요.^^" with tile "알림" buttons {"취소","확인"} default button "확인"\'' )

윈도우봇()