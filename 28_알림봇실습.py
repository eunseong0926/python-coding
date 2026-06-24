"""
밥 먹고 가기
와 같은 팝업창 띄우고

3번 버튼종류를 이용해서 예 아니오 취소
클릭할 수 있도록 만들기
"""

import ctypes
# 1.일반
#ctypes.windll.user32.MessageBoxW( 0, "밥 먹고 가기", "팝업창", 3 )

# 2.함수만들어서 호출

def 윈도우알림봇():
    ctypes.windll.user32.MessageBoxW( 0, "밥 먹고 가기", "알림", 3 )

"""
1995년 32비트 컴퓨터 시절 
그때 많은 dll 확장자들의 명칭을 user32 gdi32 이런식으로 명칭 붙이는 시대

kernel32 = 파일 메모리 컴퓨터 기능
winmm    = 소리 음악
gdi      = 그림 도형 색깔그리기
shell32  = 바탕화면
"""
윈도우알림봇()
