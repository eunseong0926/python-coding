'''
pip란 
python 에서 패키지 관리자
파이썬 언어로 사용할 수 있는 외부 라이브러리(도구모음)를
인터넷에서 자동으로 찾아서 설치해주는 프로그램

사용방법
=> pip install 패키지이름

제거하다
=> pip uninstall 패키지이름

나의 컴퓨터에 설치된 패키지 보기
=> pip list

1. ...이나 터미널을 클릭하여 새터미널을 열어준다.
2. pip install 패키지이름을 입력하여 패키지를 설치한다.
3. 최초 1회 설치하고 나면, 삭제하기 전까지 마음껏 사용할 수 있다. 한번 설치하고 나면 다시설치하지 않는다. "이미 설치된 패키지 입니다. 라는 메시지가 뜬다.

macbook으로 개발을 한다는 것은 
- 마우스를 사용하지 않고 키보드로 개발 주로 진행
- pip install 패키지이름
- pip3 install 패키지이름

pip 예전에는 python 버전 2를 가리켰다.
맥/리눅스 환경에서는 pip가 pytohon2 버전을 가리키고 pip3 python3 버전을 가리킨다.
python2는 개발 트렌드에 맞지 않는 방식들이 많이 존재


window 컴퓨터가 마우스 + 키보드 최적화된 컴퓨터

No module named 'PIL' ( PIL[ Python Imaging Library ] ) 
-> PIL는 오픈소스 커뮤니티에서 이어받아 Pillow라는 이름으로 지금까지 발전시키고 있다.
   이 기술이 없으면 파이썬에 이미지 다르는 기능이 기본적으로 사라지는것과 같이 엄청난 일

pip install Pillow
- 따로 설치하는게 맞지만 qrcode를 설치할 때 함께 설치되는 경우도 있고, 설치가 되지 않는 경우도 있다.

Pillow
- 파이썬에서 이미지를 처리하는 라이브러리
- 이밎 파일을 열고, 필터, 편집 수정과 같은 작업할 수 있도록 도와주는 도구
'''

"""
아래 코드 구문들은 python 뿐만 아니라 다른 언어에서도 사용되는 문법들
import가 무엇인가



명칭.명칭2(명칭3) 각각 무엇인가 그리고 "." 무엇인가


"""

import qrcode

#url = "https://www.youtube.com"                                    # QR코드로 만들고 싶은 인터넷 주소
url = input("QR코드로 만들고 싶은 인터넷 주소를 입력하세요 : ")        # QR코드로 만들고 싶은 인터넷 주소 입력
img = qrcode.make(url)                                              # qrcode에 make() 가능을 이용해서 qr을 만든다.
파일이름 = input("저장할 파일이름을 입력하세요(ex:image.png) : ")
img.save(파일이름)                                                  # 만들어지 qr을 이미지로 저장한다.
print(파일이름,"QR코드가 생성되었습니다.")                           # 개발자에게 큐알만들기와 이미지 저장하기 완료되었다 표기한다.

#img.save( qrcode.make( input( "https://www.youtube.com" ) )  )
#img.save( qrcode.make( input( "https://www.youtube.com" ) ) ,".png" )