# 숫자만 이용한 랜덤 비밀번호 생성 + ZIP 압축

import random
import pyzipper
from pathlib import Path

# 사용할 숫자들
비밀번호에사용할숫자 = "0123456789"

# 6자리 랜덤 비밀번호 생성
만들어진비밀번호 = ''.join( random.choice( 비밀번호에사용할숫자 ) for _ in range( 6 ) )

print("생성된 비밀번호 :", 만들어진비밀번호)

# ZIP 파일 생성
with pyzipper.AESZipFile(
    "결과.zip",
    "w",
    compression=pyzipper.ZIP_DEFLATED,
    encryption=pyzipper.WZ_AES
) as 파일압축:

    # 비밀번호 설정
    파일압축.setpassword(만들어진비밀번호.encode())

    # 현재 폴더의 파일 압축
    for 파일 in Path(".").iterdir():
        if 파일.is_file():
            if 파일.name != "결과.zip":
                파일압축.write(파일)

print("압축 완료!")
print("압축 해제 비밀번호 :", 만들어진비밀번호)