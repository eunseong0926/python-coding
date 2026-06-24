"""
텍스트로 작성한 글자를 mp3로 변환 할 수 있다.

텍스트 음성변환 기능 설치하여 사용하기
pip install gTTS pygame

gTTS : Google Text-to-Speech 구글번역기를 이용해서 텍스트를 읽어주는 기능
- 구글번역기 안에 텍스트를 음성으로 변환하는 기능이 있고 이 기능이 무료다
- 구글과 연동 코드를 작업해서 소리로 표현하고자 하는 글자를 읽어주는 것

pygame : 게임을 만들 때 사용하는 도구
- 
"""
from gtts import gTTS
import pygame

text = "안녕하세요. 반갑습니다. 석가탄신일이네요. 즐거운 하루 되세요."
tts = gTTS(text=text, lang='ko') # 글자를 한국어로 변환해서 말하자
# tts = gTTS(text=text, lang='en') # 글자를 영어로 변환해서 말하자
tts.save("hello.mp3") # 변환된 음성을 mp3파일로 저장

# pygame 재생
#   mixer : 소리를 재생하는 기능들이 담겨져 있다.
#   image : 이미지를 재생하는 기능이 담겨져 있다.
#   key   : 키보드 입력을 처리하는 기능이 담겨져 있다.
#   mouse : 마우스 입력을 처리하는 기능이 담겨져 있다.
pygame.mixer.init() # 소리 기능을 시작하겠다. 세팅
pygame.mixer.music.load("hello.mp3") # mp3파일을 가져와서 재생할 준비
pygame.mixer.music.play()            # mp3파일 재생시작

# pygame.mixer.Sound : 짧은 효과음 재생용 ( 총소리, 점츠음 등 )
# pygame.mixer.music : 긴 음악이나 긴 데이터 소리 재생용
# pygame.mixer.music.get_busy() : 재생중인지 확인하는 기능
# 재생중이면 True, 재생이 끝나면 False 반환
# while = 오른쪽에 작성된 코드나 데이터가 True인 동안 반복하겠다.

# while True 일 동안 무한 반복할 때 사용하는 코드

# while 파이썬아 오른쪽에 있는 코드가 True여서 프로그램을 종료하면 안돼
# 원래는 pass 자리에 True일 때 반복할 기능들을 작성하지만 소리만 재생하고 싶어 = pass 사용

while pygame.mixer.music.get_busy(): #소리를 재생하고 있는데 프로그램이 종료되지 않도록 기다리는 코드
    pass # while 문 안에서 아무것도 하지 않고, 기다리는 용도

# GPT 에게 프롬프트를 보낼 때
# 위 코드를 참고해서 소비자가 input으로 작성한 데이터를 실시간으로 읽어주는 코드를 작성해줘 와 함께 위 코드를 함께 전송하면 위 코드 형태에 맞게 코드 수정해서 전달