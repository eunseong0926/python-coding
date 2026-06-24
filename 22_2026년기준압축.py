# 22_2026년기준압축
import zipfile
import os

#import = 가져오다 가져올 도구이름
#from 가져오겠다 도구이름 import 어떤 도구만 가져오겠다. 가져올 도구이름
from pathlib import Path # 2020년 대에는 path를 자주 사용
# pathlib.py에서 def Path(): 가능 가져와서 사용하겠다.

with zipfile.ZipFile("결과3.zip","w") as 파일압축:
    # Path(".") Path = 폴더 경로 "." = 현재 폴더 위치
    # .iterdir()     = 폴더 안 파일을 하나씩 꺼내겠다.
    # iter = 반복 dir() = 폴더 안에 있는 파일 전부다
    for 파일 in Path(".").iterdir():
        if 파일.is_file():
            if 파일.name != "결과3.zip":
                파일압축.write(파일)
print("파일을 완성했습니다.")

# 로그인 하지 않은 GPT나 무료버전 GPT는 현재 작업하고 있는 압축파일을 제외하고 압축해야한다는 개념자체가 없기 때문에
# 잘못하다가 컴퓨터 한 대 날리는 불상사가 발생할 수 있다.
# 이러한 개념은 개발자가 인지한 상태에서 명령을 지시해야한다.

# 현재 작업하고 있는 압축파일은 제외한 상태에서 현재 폴더 내에 존재하는 파일들을 압축하는 코드 파이썬으로 작성해줘