# def 없이 비밀번호 랜덤으로 만들기

# import = 가져오다
# random 과 string 도구를 가져와서 현재 .py 파일에서 사용할것이다.
# 그런데 pip install 도구이름으로 설치하지 않으면
# 파이썬 창시자 귀로빈섬이 만들어놓은 부가기능을 사용하는 것

import random
import string
"""
random.choice() : 랜덤으로 1개씩 뽑기 중복 가능하다
random.sample() : 한 번에 여러개 뽑기 중복 불가
                  소괄호 안에 ( 랜덤에서 사용할 비밀번호, 몇 개 뽑을 것인지 개수 )
"""
랜덤으로_비밀번호를_만들때_사용할글자들 = "abcde12345%!"
만들어진_비밀번호=''.join( random.choice( 랜덤으로_비밀번호를_만들때_사용할글자들 ) for _ in range( 5 ) )
print( "==>",만들어진_비밀번호 )
