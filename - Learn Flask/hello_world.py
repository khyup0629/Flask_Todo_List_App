from flask import Flask
app = Flask(__name__)
# Flask 라는 클래스의 객체를 생성하고 인자로 __name__ 을 입력합니다.
# [그림 3]과 같이 단일 모듈을 사용한다면, __name__을 인자로 사용해야 합니다.
# 왜냐하면 어플리케이션으로 시작되는지 혹은 모듈로 임포트 되는지에 따라 이름이 달라지기 때문입니다.
# 만약, 패키지를 사용하는 경우라면 일반적으로 패키지 이름으로 작성하는 것이 좋습니다.
# 때문에 인자로는 모듈이나 패키지의 이름을 넣습니다.
# 이는 플라스크(Flask)에서 템플릿이나 정적파일을 찾을 때 필요합니다.

@app.route('/')
# route( ) 데코레이터를 사용해서 Flask 에게 어떤 URL 이 우리가 작성한 함수를 실행시키는지 알려줍니다.
# 즉, 생성한 객체의 route 를 설정합니다. 이는 URL 을 설정하는 것을 의미합니다.
def hello_world():
    return 'Hello World'

if __name__=='__main__':
    app.run()
# 최종적으로 run() 함수를 사용하여 개발한 어플리케이션을 로컬 서버로 실행합니다.
# 소스파일을 모듈이 아닌 python 인터프리터를 이용해서 직접 실행한다면,
# if __name__ == '__main__': 은 우리가 실행한 서버가 현재 동작되는 유일한 서버라는 의미입니다.

# https://forensickelly.tistory.com/entry/Python-Windows%EC%97%90%EC%84%9C-Flask-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
