"""
Flask = python으로 웹 서버/API를 만드는 마이크로 프레임워크
마이크로 = 소규모
마이크로 라는 말처럼 기본 기능만 딱 들어있고, 나머지는 필요할 때 추가하는 방식

회사에서 python으로 웹 프로그램을 만들때 Django를 사용하지만
회사가 아닌 개인적인 용도로 웹 프로그램을 만들 때는
Flask라는 도구를 사용해서 만든다.
프레임워크 = 규정이 정해져 있는 도구 모음
Flask로 웹을 만들 때 어지간하면 웹을 만드는  html 확장자 파일의 경우
templates 폴더 내에 만들어야 한다.

플라스크로 만든 웹 프로젝트 구조
프로젝트 폴더
    app.py
    templates/
        index.html
        about.html
    static/
        디자인.css
        기능.js

ModuleNotFoundError: No module named 'flask'
pip install flask
내 컴퓨터에 flask 라는 도구를 파이썬 도구 모음 웹사이트에서 가져와 설치하기
"""
# flask 도구에서 Flask = 인터넷 환경 생성 도구와
#               render_temlpate = temlpates 폴더에서 .html 파일을 찾아오는 도구를 꺼내서 사용하겠다.
# from 어떤도구함에서    도구모음
# import 가져오겠다     도구이름1번, 도구이름2번
from flask import Flask, render_template

# Flask() 도구를 변수이름 이라는 내부 공간에 담아두겠다.
# __name__ _를 두 번 작성하는 것은 파이썬에서 만들어놓은 예약언어로 
# __name__은 현재파일 이름을 기준으로 웹 사이트를 만들기 시작하겠다.
변수이름 = Flask(__name__)

# 변수이름이라는 공간에 route = 특정 경로를 담아두겠다.
# 인터넷에서 / 로 끝나는 경로에서는 index.html에 작성한 코드를 소비자들의 눈에 보여주겠다.
@변수이름.route("/")
def 메인페이지_보여주기():
    return render_template("index.html")

@변수이름.route("/about")
def 어바웃페이지_보여주기():
    return render_template("어바웃.html")

#/service라는 경로로 def 서비스페이지_보여주기()
#를 만든 후 servce내부에 생성하여 127.0.0.1:5000/service 로 접속했을때 
# service.html에 존재하는 코드를 웹으로 띄워 페이지 보여주기

@변수이름.route("/service")
def 서비스페이지_보여주기():
    return render_template("service.html")

# 깃허브 수요일 수업 전까지 가입하기

# 만약에 현재 파일에서 오른쪽 위에 있는 재생버튼을 누른게 맞다면
# 만약에 __name__ 이름이 app.py라는 파일에서
# __main__재생버튼을 누른게 사실이라면
# : 아래 코드를 실행할 것이다.
if __name__ == "__main__":
    # 변수이름에 담긴 모든 정보를 run 실행하겠다.
    # debug=True 개발자 모드로 수정된 코드가 있으면 바로바로 인터넷에 반영하겠다.

    # debug=False 개발자 모드가 아닌 소비자에게 배포한 용도로 수정된 사항을 인터넷에 실시간으로 반영하지 않겠다.
    # 서비스 점검시간이나 운영중지시간을 이용해서 다시 웹사이트를 껐다가 킬 것이다.
    변수이름.run(debug=True) #상태모드