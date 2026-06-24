import random
import string

# def 어떤 기능을 생성할 때 사용하는 명령어
# 사용 방법                                                     ":"(콜론) -> 기능만들기 시작 표기
# def 기능이름설정(세부적으로 커스텀할 데이터 추가하고 싶으면 추가) :
# 띄어쓰기4번 또는 탭 한 벚느오 def 안에 기능을 작성
# 띄어쓰기 또는 탭이 종료되면 def 내부에 기능 설정은 모두 종료

# def 비밀번호만들기() : # 비밀번호만들기 라는 기능을 만들겠다.
# 글자길이는 기본값으로 12로 설정하겠다.
# 만약에 12에서 다른 글자길이로 변경하고 싶다면 추후에 숫자를 작성하면 된다!

# string = 문자들이 나열된 표기법
# string.ascii_letters = 대소문자 알파벳 모두가 사용 ( a-z , A-Z ) -> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits        = 0-9까지의 숫자 모두다 사용 -> 0123456789
# string.punctuation   = 특수문자 모두다 사용 -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def 비밀번호만들기( 글자길이 = 12 ):
    사용할글자들 = string.ascii_letters + string.digits + string.punctuation

    #join = 문자열 리스트를 하나의 문자열로 합치는 기능
    #'구분자'.join( 리스트 )
    #         
    비밀번호 = ''.join( random.choice( 사용할글자들 ) for _ in range( 글자길이 ) )    
    return 비밀번호 # 비밀번호 만들라고 했지 출력하라 안했잖아!

print("비밀번호 만들기 1차 시작")
비밀번호만들기() # 비밀번호를 만들었으나 보여달라 하지 않아 아무것도 안보이는 상태

print("랜덤 비밀번호 12자리 만들기 : ", 비밀번호만들기())
print("랜덤 비밀번호 8자리 만들기  : ", 비밀번호만들기(8))