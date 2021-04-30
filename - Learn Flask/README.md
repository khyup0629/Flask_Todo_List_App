# Learning Flask
+ [1. Hello Flask](#1-Hello-Flask)
	+ [1) 플라스크를 사용해 웹 페이지에 문자열 출력하기](#1-플라스크를-사용해-웹-페이지에-문자열-출력하기)
	+ [2) 플라스크 어플리케이션 동작과정](#2-플라스크-어플리케이션-동작과정)
+ [2. 파이썬 플라스크 라우팅](#2-파이썬-플라스크-라우팅)
	+ [1) 플라스크 정적 페이지 라우팅](#1-플라스크-정적-페이지-라우팅)
	+ [2) 플라스크 동적 페이지 라우팅](#2-플라스크-동적-페이지-라우팅)

---
# 1. Hello Flask

+ 플라스크 프레임워크 학습 후 플라스크를 활용해 웹 페이지에 문자열을 출력한다.
+ 웹 페이지에 문자열을 띄우는 학습을 통해 플라스크 동작 방식 또한 살펴본다.

## 1) 플라스크를 사용해 웹 페이지에 문자열 출력하기

+ 다음 소스코드를 활용해 웹 페이지에 문자열을 출력한다.
``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello World!</h>"

if __name__ == "__main__":
	app.run()
```
### 코드 설명

    app = Flask(__name__)

+ Flask 라는 클래스의 객체를 app이라는 변수에 할당하고 인자로 ___name___ 을 입력한다. 단일 모듈을 사용한다면, ___name___ 을 인자로 사용해야 한다.
+ 왜냐하면 어플리케이션으로 시작되는지 혹은 모듈로 임포트 되는지에 따라 이름이 달라지기 때문이다. 만약, 패키지를 사용하는 경우라면 일반적으로 패키지 이름으로 작성하는 것이 좋다.
+ 때문에 인자로는 모듈이나 패키지의 이름을 넣는다. 이는 플라스크(Flask)에서 템플릿이나 정적파일을 찾을 때 필요하다.

    	@app.route("/")

+ app 객체의 라우팅 경로를 설정한다. 즉, URL 을 설정하는 것을 의미한다.
+ route() 데코레이터를 사용해서 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려준다.
+ "/"로 경로를 설정하면 기본적으로 http://127.0.0.1:5000/ 이 설정된다.

    	def hello():
	    return "<h1>Hello World!</h>"

+ 해당 라우팅 경로로 요청이 오면 실행할 함수 정의한다.(문자열 출력)
+ 뷰함수(특정 URL을 호출했을 대 호출되는 함수)에 속한다.

    	if __name__ == "__main__":
      		app.run()

+ 최종적으로 run() 함수를 사용하여 개발한 어플리케이션을 로컬 서버로 실행한다.
+ 소스파일을 모듈이 아닌 python 인터프리터를 이용해서 직접 실행한다면,
+ if __name__ == '__main__': 은 '파이썬의 인터프리터가 메인 모듈로 실행됐는지'라는 의미이다.

### 실행 결과

+ 코드를 실행하면 로컬호스트 루프백 IP인 127.0.0.1의 플라스크 기본 포트 번호인 5000번으로 서버가 실행된다.

![image](https://user-images.githubusercontent.com/43658658/116643887-fda74900-a9ac-11eb-8f4b-aae9f612c5a7.png)

  + Serving Flask app "hello_world" (lazy loading) - 플라스크 앱인 "hello_world"을 옮겨 로딩. (파일 이름 : hello_world.py)
  + Environment: production - 환경에 대해 명시. 경고 메시지는 개발 서버이니 배포에 사용하지 말 것 당부.
  + Debug mode: off - 디버그 모드가 활성화 되어있지 않음.
  + Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 
  	+ 해당 주소로 서버가 활성화 되어있음. Ctrl + c 키나 quit를 입력하면 서버가 중단됨.
  	+ 이후로 서버 로그가 나옴. 로그는 [url] - - [시각] "요청" [HTTP 코드] - 의 형태

![image](https://user-images.githubusercontent.com/43658658/116643903-07c94780-a9ad-11eb-8fa8-c4b949f059b7.png)

+ 127.0.0.1:5000 혹은 localhost:5000으로 url을 입력해 브라우저에 접속하면 지정한 함수 안 내용처럼 Hello World! 문자열이 출력된다. 
+ 함수에 지정한 문자열은 h1태그로 둘려싸여있다. 이는 글씨 크키를 지정하는 HTML 웹 언어의 태그를 가져와 사용한 것이다.
	
## 2) 플라스크 어플리케이션 동작과정

+ 플라스크 어플리케이션을 만들고 실행하는 법은 간단하다. 다음 과정을 통해 플라스크 어플리케이션이 호출된다.

![image](https://user-images.githubusercontent.com/43658658/116644165-a2298b00-a9ad-11eb-9ae1-d82cce6162a8.png)

1. 플라스크는 특정 URL이 호출되며 실행된다.
2. 특정 URL이 호출되면 그 URL에 매핑된(대응하는) 함수가 실행된다.
3. 요청한 URL이나(HTTP GET 요청을 통해 가져올 글 요청), 내용(HTTP POST 요청을 통해 내용 요청)을 분석해  비즈니스 로직인 논리를 실행한다. 이때, 상황에 따라 요청의 상태를 유지할 경우 쿠키나 세션을 사용한다. 또한 프로그램의 상태를 기록하기 위해 로깅을 하고 오류가 발생한 경우에 처리할 로직을 별도로 제공할 수도 있다. 
4. 논리가 처리되면 결과를 응답으로 템플릿에 반환한다.
5. 응답으로 전송할 값을 HTML에 표현한다.

[위로](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221798632183
+ https://forensickelly.tistory.com/entry/Python-Windows%EC%97%90%EC%84%9C-Flask-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0

---

# 2. 파이썬 플라스크 라우팅

+ 플라스크는 복잡한 URL를 쉽게 함수로 연결하는 방법을 제공한다.
+ 직접 URL을 지정해 사용하거나 동적으로 변화되게 만들 수 있다.
+ 해당 기능인 route, 라우팅을 살펴본다.

## 1) 플라스크 정적 페이지 라우팅

+ 플라스크는 복잡한 URL를 쉽게 함수로 연결하는 방법을 제공한다. 
+ 해당 기능인 route() 함수를 사용해 쉽고 빠르게 원하는 URL를 처리하는 기능을 만들 수 있다.

+ 지난 예제에서 route('/')를 route('/hello')로 변경해보자. 이렇게 되면 기존 경로가 아닌 127.0.0.1:5000/hello 로 접속해야 올바르게 페이지를 찾을 수 있다.
``` python
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
	return "<h1>Hello World!</h>"

if __name__ == "__main__":
	app.run()
```
+ 기존 루트 경로에서는 연결된 함수가 없어 페이지를 찾을 수 없다.

![image](https://user-images.githubusercontent.com/43658658/116645376-ae631780-a9b0-11eb-8896-453c552c1d69.png)

+ 127.0.0.1:5000/hello 경로로 들어가면 라우트를 거쳐 뷰함수가 실행되어 지정된 문자열이 올바르게 나타나는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/43658658/116645389-b6bb5280-a9b0-11eb-8d28-b879324b7465.png)

## 2) 플라스크 동적 페이지 라우팅

+ 직접 URL을 지정하는 것이 아닌 상황에 따라 다른 URL로 변화하는 동적 적용도 가능하다. 또한 여러 URL을 한 함수에 적용할 수도 있다. 
+ URL에 동적인 변수를 사용하려면 원하는 위치에 "<변수>" 형태로 추가한다. 해당 변수는 URL과 일치하는 뷰 함수의 인자로 사용할 수 있다.

+ 기존 코드에 동적 라우팅을 적용해보자.
``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello world!"

@app.route('/profile/<username>')
def get_profile(username):
    	return 'profile : ' + username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    	return 'message_id : %d' % message_id

if __name__ == "__main__":
	app.run()
```
### 코드 설명 및 실행 결과
``` python
@app.route('/profile/<username>') #/profile/ 경로에 뒤에 입력한 문자열대로 페이지가 동적 접속.
def get_profile(username):
    return 'profile : ' + username
```
+ 코드에서 동적으로 변경되는 부분은 인자로 전달될 username 변수에 해당한다. 
+ URL의 끝점(endpoint)으로 추가된 username은 해당 URL과 일치하는 뷰 함수인 get_profile 함수의 인자로 들어가 함수 내에서 사용된다.

![image](https://user-images.githubusercontent.com/43658658/116646595-6ee9fa80-a9b3-11eb-8f54-22373acf9a2e.png)

+ 127.0.0.1:5000/profile/user 의 경로로 접속하게 되면 user가 변수가 되고 함수 인자로서 함수에 들어가 profile : user 의 문자열이 나타나는 것을 확인할 수 있다.

``` python
@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message_id : %d' % message_id
```
+ "<변환타입:변수>" 형태로 기입해 문자열이 아닌 다른 형태로 변환할 수도 있다. 
+ 다음 코드는 /message 경로에 숫자 형태로 입력을 받아 출력하며 출력 형태는 파이썬의 포맷팅 구조와 같이 %를 이용해 포맷팅해준다.

![image](https://user-images.githubusercontent.com/43658658/116646621-7f01da00-a9b3-11eb-8c65-42053ad3d71e.png)

+ 127.0.0.1:5000/message/1 의 경로로 접속하면 1이 정수 형태의 변수로 인식되고 함수 인자로서 함수에 들어가 %d 형식으로 나타나는 것을 확인할 수 있다.

[위로](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221798793729

---

