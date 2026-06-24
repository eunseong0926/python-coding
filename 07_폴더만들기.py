'''
makedirs("폴더이름") : 폴더를 만들어주는 함수(=기능)

사용 방법
import os
os.makedirs("폴더이름", exist_ok=True)

폴더를 만든 때 exits_ok=True 만약 만들고자 하는 폴더이름이 존재하면 건너뛰기

True = 사실이다 맞다 진실이다
False = 거짓이다 아니다 틀리다
exist_ok = False # 톨더가 존재할 경우 에러가 발생한다.

mkdir("폴더이름") : 딱 하나의 폴더만 만들어주는 기능 그렇게까지 많이 사용되지는 않는다.
makedirs("폴더1번/폴더2번/폴더3번",exist_ok=True)
폴더 1번안에 폴더2번 생성하ㅏ고 폴더3번을 생성하는 폴더 여러개 만든기 기능을 더 많이 사용

mkdir() 경우 동일한 명칭의 폴더가 있으면 에러 발생 -> 번거롭게 추가 세팅작업 필요
makedirs() 사용해서 하나의 폴더, 여러폴더를 만들며 동일한 명칭의 폴더가 있으면 유연하게 건너뛰기 사용
'''

import qrcode
import os # 파이썬에서 자체적으로 만든기능 
# 기본기능 이외 부가기능을 갖올 때도 import 사용해서 가져오기도 한다.
# os = 운영체제 windows, Mac과 같은 환경 의미
#dir = directory = 폴더
# / = 폴더를 구분하는 방식

# 폴더이름을 입력하세요 : 
# 저장할 주소를 입력하세요 : 
# 이미지 파일이름을 입력하세요 : 

폴더이름 = input("폴더 이름을 입력하세요 : ") # 큐알폴더
url     = input("저장할 주소를 입력하세요 : ")  # https://www.google.com
파일이름 = input("이미지 파일이름을 입력하세요 : ") # 구글
os.makedirs( 폴더이름, exist_ok = True )
img = qrcode.make(url)
img.save(폴더이름+"/"+파일이름+".png")
#img.save(폴더이름+"/"+파일이름+".jpg")

print(파일이름,"QR코드가 생성되었습니다.")