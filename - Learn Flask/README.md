# Learning Flask
+ [1. Hello Flask](#1-Hello-Flask)
	+ [1) 플라스크를 사용해 웹 페이지에 문자열 출력하기](#1-플라스크를-사용해-웹-페이지에-문자열-출력하기)
	+ [2) 플라스크 어플리케이션 동작과정](#2-플라스크-어플리케이션-동작과정)
+ [2. 파이썬 플라스크 라우팅](#2-파이썬-플라스크-라우팅)
	+ [1) 플라스크 정적 페이지 라우팅](#1-플라스크-정적-페이지-라우팅)
	+ [2) 플라스크 동적 페이지 라우팅](#2-플라스크-동적-페이지-라우팅)
+ [3. 플라스크 렌더링](#3-플라스크-렌더링)
	+ [1) HTML](#1-HTML)
	+ [2) 플라스크에서 HTML 코드 사용하기](#2-플라스크에서-HTML-코드-사용하기)
	+ [3) 플라스크 HTML 파일 렌더링](#3-플라스크-HTML-파일-렌더링)
+ [4. 플라스크 요청과 응답](#4-플라스크-요청과-응답)
 	+ [1) HTTP 메소드](#1-HTTP-메소드)
 	+ [2) 플라스크 GET 요청](#2-플라스크-GET-요청)
 	+ [3) 플라스크 POST 요청](#3-플라스크-POST-요청)
 	+ [4) GET과 POST 능동처리](#4-GET과-POST-능동처리)
+ [5. 로컬 서버 실행](#5-로컬-서버-실행)
	+ [1) 로컬 서버 실행 설정](#1-로컬-서버-실행-설정)
+ [6. 파이선 플라스크 jinja2 템플릿](#6-파이선-플라스크-jinja2-템플릿)
	+ [1) 정적 파일과 템플릿](#1-정적-파일과-템플릿)
	+ [2) 신사2 템플릿 문법](#2-신사2-템플릿-문법)
+ [7. 파이썬 플라스크 CSS 사용하기](#7-파이썬-플라스크-CSS-사용하기)
	+ [1) CSS](#1-CSS)
	+ [2) 파이썬 플라스크에서 CSS 파일 포함시키는 방법](#2-파이썬-플라스크에서-CSS-파일-포함시키는-방법)
+ [8. 렌더링할 HTML 파일에 이미지 삽입](#8-렌더링할-HTML-파일에-이미지-삽입)
	+ [1) 정적 이미지 삽입](#1-정적-이미지-삽입)
	+ [2) 동적 이미지 삽입](#2-동적-이미지-삽입)
+ [9. 파이썬 플라스크 파일 업로드 서버 구축](#9-파이썬-플라스크-파일-업로드-서버-구축)
	+ [1) 정적 파일 구성](#1-정적-파일-구성9강)
	+ [2) 백엔드 서버 구현](#2-백엔드-서버-구현9강)
	+ [3) 프론트엔드 구현](#3-프론트엔드-구현9강)
+ [10. 파이썬 플라스크 파일 다운로드 서버 구축](#10-파이썬-플라스크-파일-다운로드-서버-구축)
	+ [1) 정적 파일 구성](#1-정적-파일-구성10강)
	+ [2) 백엔드 서버 구현](#2-백엔드-서버-구현10강)
	+ [3) 프론트엔드 구현](#3-프론트엔드-구현10강)
+ [11. 파이썬 플라스크 에러와 로깅](#11-파이썬-플라스크-에러와-로깅)
	+ [1) 에러 처리](#1-에러-처리)
	+ [2) 로깅](#2-로깅)
+ [12. 로그인과 세션, SQLite DB](#12-로그인과-세션-SQLite-DB)
	+ [1) 라이브러리 설치 및 파일 구성](#1-라이브러리-설치-및-파일-구성)
	+ [2) 회원가입 및 로그인 폼 만들기](#2-회원가입-및-로그인-폼-만들기)
	+ [3) 데이터베이스 설정](#3-데이터베이스-설정)
	+ [4) 세션 설정](#4-세션-설정)
	+ [5) 블로그 페이지 오픈 설정](#5-블로그-페이지-오픈-설정)
	+ [6) 서버 구현](#6-서버-구현)

---
# 1. Hello Flask

> <h3>학습 목표

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

> <h3>코드 설명

```
app = Flask(__name__)
```
+ Flask 라는 클래스의 객체를 app이라는 변수에 할당하고 인자로 ___name___ 을 입력한다. 단일 모듈을 사용한다면, ___name___ 을 인자로 사용해야 한다.
+ 왜냐하면 어플리케이션으로 시작되는지 혹은 모듈로 임포트 되는지에 따라 이름이 달라지기 때문이다. 만약, 패키지를 사용하는 경우라면 일반적으로 패키지 이름으로 작성하는 것이 좋다.
+ 때문에 인자로는 모듈이나 패키지의 이름을 넣는다. 이는 플라스크(Flask)에서 템플릿이나 정적파일을 찾을 때 필요하다.
```
@app.route("/")
```
+ app 객체의 라우팅 경로를 설정한다. 즉, URL 을 설정하는 것을 의미한다.
+ route() 데코레이터를 사용해서 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려준다.
+ "/"로 경로를 설정하면 기본적으로 http://127.0.0.1:5000/ 이 설정된다.
```
def hello():
	return "<h1>Hello World!</h>"
```
+ 해당 라우팅 경로로 요청이 오면 실행할 함수 정의한다.(문자열 출력)
+ 뷰함수(특정 URL을 호출했을 대 호출되는 함수)에 속한다.
```
if __name__ == "__main__":
	app.run()
```
+ 최종적으로 run() 함수를 사용하여 개발한 어플리케이션을 로컬 서버로 실행한다.
+ 소스파일을 모듈이 아닌 python 인터프리터를 이용해서 직접 실행한다면,
+ if __name__ == '__main__': 은 '파이썬의 인터프리터가 메인 모듈로 실행됐는지'라는 의미이다.

> <h3>실행 결과

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

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221798632183
+ https://forensickelly.tistory.com/entry/Python-Windows%EC%97%90%EC%84%9C-Flask-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0

---

# 2. 파이썬 플라스크 라우팅

> <h3>학습 목표

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

> <h3>코드 설명 및 실행 결과

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

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221798793729

---
# 3. 플라스크 렌더링

> <h3>학습 목표

+ 웹은 크게 사용자에게 보여지는 **프론트엔드**와 프론트에서 요청한 내용을 처리하는 **백엔드**단이 있다.
+ 플라스크는 디장고와 달리 마이크로 프레임워크기 때문에 **프론트엔드와 백엔드를 동시에 처리하지 못한다.**
+ 플라스크는 서버의 **백엔드만 담당**하며 사용자에게 보여지는 부분은 **프론트엔드 언어를 사용**해야 한다. 
+ 웹 페이지에서 주로 보여지는 부분인 **HTML 언어**를 알아보고 플라스크에서 활용면을 살펴본다.

## 1) HTML
+ 하이퍼텍스트 마크업 언어(HyperText Markup Language), 구조적 웹 문서를 만들 수 있는 언어로 태그 단위로 제어한다. 
+ 너무 간단하고 태그로만 이뤄진 스크립트라는 등의 이유로 프로그래밍 언어의 범주는 속하지 않지만 웹을 구축하기 위해서는 꼭 알아야 할 언어다.

+ HTML 언어로 구조화하여 문자열을 출력하는 법은 다음 코드와 같다.
```
<!doctype html>
<html>
  <head>
    <title>Hello HTML</title>
  </head>
  <body>
    <p>Hello World!</p>
  </body>
</html>
```

> <h3>코드 설명

+ 확장자 : html
+ 특징과 문법 : 
	+ 태그 구조 : 시작 태그와 종료 태그가 한 묶음이며 종료 태그에는 "/"가 붙는다.
	+ 문서의 시작 : 문서의 시작은 html이다. 이는 문서가 html 문서임을 표시하는 것이다.
	+ 주석 : 일종의 개발자들의 설명줄. 코드에 영향을 주지 않는다. html에서는 !내용으로 표기한다.
	+ 코드 구조 : html은 head와 body 구조로 나뉜다. 
		+ head : 문서 제목과 같은 보충 정보
		+ body : 실제 브라우저 표시 내용 (웹 문서의 본문)
+ 태그 : (이외에도 다양한 태그가 존재)
	+ title : 브라우저의 윗부분인 제목을 설정
	+ h1,6 : 표제. h1,h6까지 숫자가 커질수록 글씨가 작아진다
	+ p : 단락(문장) 변경
	+ br : 줄 바꿈
	+ center : 가운데 정렬

> <h3>실행 결과

+ **앞서 행했던 예제**를 이용해 웹 페이지에 접속해 **F12** 개발자키를 누르면 페이지 소스를 볼 수 있다.
+ 파이썬에서 입력한 문자열이 HTML 코드로 자동 반영되어 들어가 있다.

![image](https://user-images.githubusercontent.com/43658658/116661154-fb55e680-a9ce-11eb-885f-76ed1ac97812.png)

## 2) 플라스크에서 HTML 코드 사용하기

+ HTML이 무엇이고 어떻게 사용하는지 알았으니 간단히 기본 태그와 입력, 버튼 태그만 가지고 입력창을 만들어보자.
``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	html = """\
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8"> 
		<title>HTML for python flask</title>
	</head>
	<body>
	<form>
		<p>이름 : <input type="text" id="input"></p>
		<p>이름을 입력하고 제출버튼을 누르세요. <input type="button" value="제출" onclick="alert('제출 완료!')" /></p>
	</form>
	</body>
	"""
	return html

if __name__ == "__main__":
	app.run()
```

> <h3>코드 설명

```
	html = """\
```
+ html이라는 변수에 html 코드를 넣어줄 것이다. 여러줄에 걸쳐서 입력하기 위해 """\로 시작한다.

```
		<meta charset="UTF-8">
```
+ 페이지를 **한국어로 인코딩**한다. 즉, 한국어가 깨지지 않고 제대로 보일 수 있도록 해준다.

```
		<title>HTML for python flask</title>
```
+ HTML for python flask로 페이지의 제목을 설정한다.

```
	<form>
	
	</form>
```
+ form 태그 내에는 웹 서버와 웹 프로그램을 통해 처리되어야 하는 데이터들을 담는다.

```
		<p>이름 : <input type="text" id="input"></p>
		<p>이름을 입력하고 제출버튼을 누르세요. <input type="button" value="제출" onclick="alert('제출 완료!')" /></p>
```
+ 문장을 표시할 때는 p 태그를 이용한다.
+ input type="text" id="input"는 문자를 입력할 수 있는 박스 하나를 생성한다.
+ input type="button" value="제출" onclick="alert('제출 완료!')" /는 제출(value)이라는 이름의 클릭할 수 있는 버튼(button)을 생성하고 이를 클릭할 시(onclick) '제출 완료!'라는 알림(alert)이 뜨도록 한다.

```
	return html
```
+ html 코드를 반환한다. 

> 실행 결과

+ 파이썬을 실행하면 페이지 제목이 'HTML for python flask'인 페이지가 아래와 같이 나타난다.

![image](https://user-images.githubusercontent.com/43658658/116664686-c304d700-a9d3-11eb-963d-8068837639a6.png)

+ 이름을 입력하고 제출 버튼을 누르면 '제출 완료!'라는 알림이 뜬다.

![image](https://user-images.githubusercontent.com/43658658/116664504-8a64fd80-a9d3-11eb-9b73-f6bc3bb2c5b5.png)

## 3) 플라스크 HTML 파일 렌더링

+ 파이썬 코드 내부에서 html 코드작업을 하다보면 다소 불편하고 작성이 어렵다.
+ 플라스크에서 제공하는 렌더링 함수를 이용해 외부에서 작성한 html 파일을 가져와 사용할 수 있어 간편하게 웹 페이지를 조성할 수 있다.
+ 앞서 html 변수에 담았던 html 작성 내용을 파이썬 코드가 위치한 경로에 templates 폴더를 만든 뒤 .html 확장자로 저장한다.

![image](https://user-images.githubusercontent.com/43658658/116665233-7c63ac80-a9d4-11eb-82ee-fc87cefd70c6.png)

![image](https://user-images.githubusercontent.com/43658658/116665548-e11f0700-a9d4-11eb-9f0a-5c61c0796c44.png)

+ 각 html 웹 페이지를 별도의 파일로 작성하면 유지보수가 쉬워 용이하다.
+ 이제 작성한 코드의 내용을 render_temlate 함수를 이용해 가져올 것이다.

``` python
from flask import Flask, render_template  # 랜더링 import
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('input.html')  # 랜더링 반환

if __name__ == "__main__":
	app.run()
```
+ 저장한 input.html 파일을 render_template 함수를 이용해 반환하면 된다.
+ 실행하면 동일한 결과가 나옴을 확인할 수 있다.

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221800287035

---

# 4. 플라스크 요청과 응답

> <h3>학습 목표

+ 플라스크가 제공하는 기능 중 하나인 요청과 응답을 알아본다.
+ GET 요청과 POST 요청을 살펴본다. 아울러 HTTP 메소드 개념을 학습한다.

## 1) HTTP 메소드

+ 어떤 방식으로 웹 어플리케이션 페이지를 개발하더라도 가장 기본적이고 필수적인 처리 과정은 **요청을 받아 적절히 처리하고 그 결과로 응답을 주는 것**이다.
+ 가장 먼저 처리해야 하는 것은 **HTTP 요청으로 넘어온 데이터를 어떻게 받아 처리하는지**다. 이완 관련해 **HTTP 메서드**를 먼저 알아보자.

+ 모든 컴퓨터 서비스는 인터넷 통신 규약인 프로토콜의 하나를 사용해 통신한다. 웹 사이트의 **URL**은 그 중 **http와 https 프로토콜**을 사용한다. 
+ 기존 http 프로토콜이 사용되었으며 점차 보안을 위해 보안 기능이 탑재된 **https 프로토콜**을 사용하기 시작한다. 
+ 이는 WWW(world wide web)에서 데이터 통신을 하는데 근간이다. 명시된 URL에 데이터를 탐색하는 메서드가 프로토콜에 정의되어있다.
+ HTTP 메서드는 다음과 같이 존재한다.

![image](https://user-images.githubusercontent.com/43658658/116776355-fc584800-aaa2-11eb-9b7b-b1fce5e8d5e8.png)

+ 서버에 요청을 보내 응답을 받기 위해서 GET 혹은 POST 방식으로 요청한다.

## 2) 플라스크 GET 요청

+ 플라스크에서 요청에 대한 정보는 **request에 담겨있고** 객체는 안전을 보장한다.
+ 파이썬에 존재하는 requests 모듈이 아니라 **플라스크 프레임워크에 존재하는 request를 불러와 사용한다.**

	from flask import request

> <h3>request 모듈 구성 요소

+ HTTP 메서드에 대한 정보를 얻을 수 있는 **method**
+ GET 방식으로 URL에 인자를 'key=value' 형태로 전달했을 때 그 인자를 참조할 수 있는 args, POST, PUT 방식의 HTML 폼 데이터를 얻을 수 있는 **form**
+ 뒤에 있을 POST 방식 역시 request 모듈을 사용하고 따라서 정보는 method와 form으로 구성되어 있음

> <h3>GET 방식
	
+ **모든 파라미터를 url로 보내 요청하는 방식**이다. 

	localhost:5000/?name=user01&juso=평택시

+ url에 파라미터로 값을 넣는 방법은 ?를 붙이고 키=값의 쌍 형태로 넣으면 된다. 파라미터를 추가하고자 할 때는 &를 붙인 뒤 동일하게 추가한다.

+ 코드로 request의 args를 활용한 GET 방식 요청을 살펴보자.
``` python
from flask import Flask
from flask import request  # request 모듈 임포트
 
app = Flask(__name__)
 
@app.route('/')
def user_juso():
 
    temp = request.args.get('name', "user01")
    temp1 = request.args.get('juso', "평택시")
 
    return temp + "-" + temp1

if __name__ == "__main__":
		app.run()
```

+ 위의 코드를 실행하면 기본적으로 URL에 아무 파라미터도 입력되지 않았을 때 "user01"와 "평택시"가 디폴트값으로 설정된다.

![image](https://user-images.githubusercontent.com/43658658/116776847-ccf70a80-aaa5-11eb-8897-7c3ff602510f.png)

+ 하지만 127.0.0.1:5000/?name=user03&juso=서울시 로 입력하게 되면 값이 "user03"와 "서울시"로 바뀌게 되며 아래와 같이 출력된다.

![image](https://user-images.githubusercontent.com/43658658/116776866-e5672500-aaa5-11eb-9d2c-481cbca84911.png)

## 3) 플라스크 POST 요청

+ POST 요청은 눈에 파라미터가 보이는 GET 요청과 달리 전달하려는 정보가 **HTTP body에 포함되어 전달**된다.
	+ GET 요청 : URL에 정보 포함, 작은 양의 데이터를 보낼 때
	+ POST 요청 : HTTP body에 정보 포함, 데이터 양이 많을 때
+ 전달하려는 정보는 Form Data, Json strings 등이 있다. 이에 따라 사용하는 경우가 다르다.
+ POST 요청은 주로 입력창에서 발생한다. POST 요청 실습은 지난번에 구성했던 HTML 파일을 이용한다.

> <h3>input.html

```
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>HTML for python flask</title>
</head>

<body>
	<form action="/post" method="post">
		<p>이름 : <input type="text" id="input" name="input"></p>
		<p>이름을 입력하고 제출버튼을 누르세요. <input type="submit" value="제출" onclick="alert('제출 완료!')" /></p>
	</form>
</body>
</html>
```
+ 변경한 코드는 버튼을 클릭하면 post 요청이 이루어진다.
+ post 메서드를 통해 /post url로 접근하도록 변경했다. 이때 버튼 타입을 submit으로 변경해 값을 제출하도록 했다.
	- form에 action을 /post로 지정해 정보가 전달되는 곳이 action에 지정된 /post url로 보내짐.
	- input 입력 태그에 name을 지정해 정보를 전달받으므로 name 값 지정은 필수불가결.
	- submit은 form안에서 작성한 내용을 통째로 서버로 보내겠다는 뜻.
	- value는 버튼에 들어갈 값. 기본값은 "제출"
+ 위의 코드를 templates 폴더에 input.html로 저장하자. 
+ 위 코드는 프론트엔드이며, 플라스크의 기본 서버인 5000번으로 접속했을 때 페이지에 띄울 화면이다.

> <h3>서버 코드

``` python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('input.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 님 환영합니다." %value
	return msg

if __name__ == "__main__":
	app.run()
```

> <h3>코드 동작 순서

1. 5000번 URL로 접근 시 작성한 html 파일 호출

![image](https://user-images.githubusercontent.com/43658658/116777940-26613880-aaaa-11eb-909d-a3a4190b31d2.png)

2. 이름을 입력하고 제출을 누르면 submit에 의해 method = 'post', name = 'input'의 형태로 구성된 정보가 127.0.0.1:5000/post 로 보내지며 post 요청 수행

3. 127.0.0.1:5000/post 주소로 post 메서드를 통해 요청이 들어오면 'input'의 정보를 넣은 메시지 호출

![image](https://user-images.githubusercontent.com/43658658/116778107-f5353800-aaaa-11eb-9152-02fbdb99faff.png)

> <h3>예외처리

+ 이름 입력 후 버튼을 누르는 post 요청없이 바로 url에 접속하는 get 요청을 통해 주소에 접속하면 메서드가 허용되지 않았다는 메시지가 나온다.

![image](https://user-images.githubusercontent.com/43658658/116778283-e8651400-aaab-11eb-8f06-0da51bce51ba.png)

## 4) GET과 POST 능동처리

+ GET 요청과 POST 요청에 따라 페이지가 다르게 노출되도록 할 수 있다.

> <h3>변경된 서버 코드

``` python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return "This is the main page"

@app.route("/user",methods=['GET', 'POST'])
def post():
	if(request.method =='GET'):
		return render_template('input.html')

	elif(request.method == 'POST'):
		value = request.form['input']
		return render_template('default.html', name=value)

if __name__ == "__main__":
	app.run()
```

> <h3>변경된 프론트엔드(input.html) 코드

```
<form action="" method="post">
```

> <h3>추가된 프론트엔드(default.html) 코드

```
<!DOCTYPE default.html>
{{ name }} 님 환영합니다.
```

> <h3>코드 분석

``` python
@app.route("/")
def hello():
	return "This is the main page"
```
+ 기본적으로 코드를 실행하면 "This is the main page" 문자열이 출력되는 페이지가 보여진다.

![image](https://user-images.githubusercontent.com/43658658/116779177-a2aa4a80-aaaf-11eb-9d5e-cce83c890df6.png)

``` python
@app.route("/user",methods=['GET', 'POST'])
def post():
	if(request.method =='GET'):
		return render_template('input.html')
```
+ URL에 127.0.0.1:5000/user을 직접 입력해서 들어가면(GET 요청) 'input.html'가 화면에 보여지도록 한다.

![image](https://user-images.githubusercontent.com/43658658/116779184-afc73980-aaaf-11eb-8a0f-d562c9b5d911.png)

``` python
elif(request.method == 'POST'):
		value = request.form['input']
		return render_template('default.html', name=value)
```
```
<form action="" method="post">
```
```
<!DOCTYPE default.html>
{{ name }} 님 환영합니다.
```
+ 이름을 입력하고 제출을 누르면 submit에 의해 form 내부에 name='input'이라는 정보가 담겨 POST 메서드(method='post')로 같은 주소(127.0.0.1:5000/user)로 POST 요청하며 보내진다.
+ POST 요청을 받으면 form 내부의 'input'정보를 name이라는 변수에 넣고 default.html을 페이지에 띄운다.

![image](https://user-images.githubusercontent.com/43658658/116779190-c2417300-aaaf-11eb-9854-42619f6d0900.png)

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221804755045

---

# 5. 로컬 서버 실행

> <h3>학습 목표

+ 파이썬 플라스크의 기본 서버 호스팅은 127.0.0.1 IP에 포트번호 5000번을 사용한다.
+ 라즈베리파이와 같은 미니 서버 혹 로컬 컴퓨터에서 서버를 열어 외부에서도 접근할 수 있게 하려면 0.0.0.0으로 지정해야 한다. 
+ 해당 정보를 알아보자.

## 1) 로컬 서버 실행 설정

+ 이번 챕터에서 다룰 내용은 app.run() 함수에 해당한다. 
+ 플라스크 객체로 선언된 변수인 app에 run() 함수를 명령하면 서버가 열린다. 이때 **host를 지정**하면 지정한 호스트로 열린다.
``` python
app.run() //기본 실행, 127.0.0.1 또는 localhost로 접속
app.run(host='192.168.0.22') //로컬 컴퓨터의 내부 로컬 IP
app.run(host='0.0.0.0') //어떤 호스트에서도 연결 가능하도록.
```
+ 호스트 뿐 아니라 기본 포트 번호인 5000번 말고 다른 포트로 서버를 열고 싶을 때도 설정해주면 변경된다.
``` python
app.run(host='0.0.0.0', port=변경하고자 하는 포트)
ex)app.run(host='0.0.0.0', port=8080)
```
+ run() 서버에는 디버그 정보를 보여주는 기능이 있으며 기본 **Fasle**이므로 **True**로 인자를 설정하면 디버그 기능을 사용할 수 있다. 
+ 단, 디버그 설정을 사용할 때 라즈베리파이와 같은 곳 등에서 실행시 관리자 권한을 요구할 수 있다.
``` python
app.run(host='0.0.0.0', debug=True)
```
+ 디버그 모드로 플라스크 로컬 개발 서버를 기동하면 콘솔창에 reloader가 다시 시작되었다는 메시지가 추가된다.
+ 또한 **수정 값이 반영**된다.

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221806680590

---
# 6. 파이선 플라스크 jinja2 템플릿

> <h3>학습 목표

+ 정적 파일의 위치 지정과 호출하는 방법에 대해 알아보자.
+ 동적 HTML을 구성하는 방법에 대해 알아보자.
+ 신사2의 대표적인 템플릿 문법들을 알아보자.

## 1) 정적 파일과 템플릿

> <h3>코드 파일 구성의 경우

+ 일반적인 웹 어플리케이션 : HTML/CSS(프론트엔드) + 자바스크립트, PHP(백엔드)
+ 플라스크 : HTML/CSS(프론트엔드) + 자바스크립트, 파이썬 플라스크(백엔드)

> <h3>뷰 함수에 대한 응답의 경우

+ 일반적인 웹 어플리케이션 : HTML/CSS/자바스크립트를 이용해 다양한 방식으로 화면을 표현한다.
+ 플라스크 : 화면 구성에 필요한 정적 파일을 지정하고 웹에서 처리된 데이터를 표현하는 템플릿을 지원한다.

> <h3>정적 파일 위치 지정의 경우

+ 일반적인 웹 어플리케이션 : 웹 서버 설정으로 지정한다.
+ 플라스크 : 생성한 패키지 폴더에 포함하거나 모듈 바로 옆 static 폴더를 만들면 /static에서 정적 파일에 접근이 가능하다.
+ url_for()의 첫 인자로 'static', 다음 인자로 filename='정적 파일명'을 통해 사용할 정적 파일 호출 가능.

``` python
url_for('static', filename='style.css')
```

+ 위 함수의 결과는 아래와 같다.

``` python
/static/style.css
```

> <h3>동적 HTML 구성

+ 신사2(jinja2) 템플릿 엔진은 CSS, 이미지, 처리 데이터를 화면에 보여주기 위한 동적 HTML을 구성하고 그 과정에서 발생하는 특수문자 처리, 웹 보안 등도 처리한다.
+ HTML 렌더링 과정에서 HTML 템플릿을 이미 간단히 다뤄본 적이 있다.
+ 아래의 예제는 이미 공부했던 input.html을 불러오는 코드이다.

``` python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('input.html')

if __name__ == "__main__":
	app.run()
```

+ 다음 예제는 단순히 불러오는 것 말고 값에 따라 출력이 달라지는 동적 HTML을 구성한다.

> input2.html

``` python
hello {{ name }}!
```

``` python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):  # 아무것도 적히지 않으면 디폴트 값인 None 출력
	return render_template('input2.html', name=name)  # url에 적힌 값이 출력

if __name__ == "__main__":
	app.run()
```
+ 아무것도 적히지 않으면 None 출력

![image](https://user-images.githubusercontent.com/43658658/117615055-2a751080-b1a4-11eb-86c4-9e2619c13112.png)

+ input2.html 파일의 {{ name }}에 url에 입력한 '/이름'이 들어간다.

![image](https://user-images.githubusercontent.com/43658658/117615082-3234b500-b1a4-11eb-9973-16e590983a98.png)

## 2) 신사2 템플릿 문법

+ 공식 신사2 문서 페이지 참고

=> https://jinja.palletsprojects.com/en/2.11.x/

> <h3>주석

``` html
{#
주석처리할 코드
#}
```

> <h3>공백

+ 기본적으로 신사2는 줄 끝 개행 문자를 제외한 공백(탭, 공백 문자, 개행 문자)은 제거하지 않는다.
	+ keep_trailing_newline : 줄 끝 개행 문자 유지
	+ trim_blocks : 템플릿 태그 뒤 첫 개행 문자 자동 제거
	+ lstrip_blocks : 템플릿 태그가 나오기 전 탭과 공백 문자 제거

``` html
  <ul>
	<li><a href="https://blog.naver.com/dsz08082">컴퓨터 블로그</a></li>
  </ul>
```

+ 템플릿 시작 태그에 +를 붙이면 태그 앞 공백을 제거.
+ 시작 태그나 종료 태그에 -를 붙이면 태그 시작과 끝 공백 제거.
+ 위와 같은 +, -를 사용했다면 태그와 기호 사이 공백이 없게 해야 함. (중복 불가)
+ 다음과 같이 - 하면 태그 시작과 끝 공백이 제거됨.

``` html
  <ul>
    {% for user in users -%}
	<li><a href="{{ user.href }}">{{ user.caption }}</a></li>
    {%- endfor %}
  </ul>
```

> <h3>이스케이핑

+ 이스케이핑 : 어떤 조건이나 환경에서 특별한 구문이나 의미로 해석되는 문자열의 의미 제거.

+ 다음은 신사2 템플릿에서 변수의 값을 출력하는데 사용하는 변수 구분자인 '{'를 이스케이핑한다.

``` html
{{ '{{' }} //구분자에 따옴표를 붙여 문자열처리
```

+ 더 큰 범위는 raw 구문을 사용한다.

``` html
{% raw %}
    <이스케이핑할 문자열>
{% endraw %}
```

> <h3>반복문

+ 일반적 for 반복 구조와 유사하다.
+ 예제로 가져왔던 다음 반복문에서 users는 리스트 형태의 변수로 user를 객체를 담고 요소를 in 구문을 사용해 가져온다.
+ href 과 caption 속성은 {{...}}를 사용해 출력한다.

``` html
  <ul>
    {% for user in users -%}
	<li><a href="{{ user.href }}">{{ user.caption }}</a></li>
    {%- endfor %}
  </ul>
```

+ for 구문 안에는 템플릿 엔진이 제공하는 특별한 변수를 사용할 수 있고 다음 표가 해당 목록이다.
	+ loop.index : for 구문이 현재 반복한 회수 (1부터)
	+ loop.index() : for 구문이 현재 반복한 회수 (0부터)
	+ loop.revindex : for 구문이 역순 반복 회수 (1부터)
	+ loop.revindex() : for 구문이 역순 반복 회수 (0부터)
	+ loop.first : 반복이 처음 실행되면 True, 아니면 False
	+ loop.last : 반복이 마지막이면 True, 아니면 False
	+ loop.length : 전체 반복 횟수
	+ loop.cycle : loop.cycle() 함수의 인자로 넘기는 리스트 항목 순서대로 전달

+ 일반적 구문

``` html
{% for <개별요소> in <리스트 형태 > %}
  <코드>
{% endfor %}
```

> <h3>if 조건문

+ if 구문으로 변수나 변수 이용 표현이 들어가고 변수의 존재 여부나 변수 값 혹 결과값의 참 거짓 값을 판단해 구성.

``` html
{% if <조건> %}
<코드>
{% elseif <조건> %}
<코드>
{% else %}
<코드>
{% endif %}
```

+ 인라인으로 다른 구문과 같이도 사용 가능하다.

``` html
{% <코드> if <조건> else <거짓시 코드> %}
```

``` html
{% for user in user if users %}
<li>{{ user.username }}</li>
{% endfor %}
```

> <h3>매크로(macro)

+ 매크로 : 반복적 사용 코드로 반복 작업을 줄이고 템플릿 코드 재사용, 일반적으로 다음 형식이다.
+ 파이썬의 함수와 같은 역할

``` html
{% macro <매크로 이름>(매크로 인자, ...) -%}
<코드>
{%- endmacro %}
```

+ 사용 예시를 살펴보자.

``` html
<p><input type="text" name="username" value=""></p>
<p><input type="password" name="password" value=""></p>
```

+ 위 HTML 코드를 매크로를 사용하면 다음과 같이 된다.

> input.html
``` html
{% macro input(name, value="",type='text') -%}
<input type="{{ text }}" name="{{ name }}" value="{{{value}}">
{%- endmacro %}
```

+ 필요한 곳에서 다음처럼 호출한다.

``` html
{% from 'input.html' import input %}  # 다른 html 파일의 input 매크로를 가져온다.
<p>{{ input('username') }} </p>
<p>{{ input('password', type='password') }} </p>
```

> <h3>import 

+ import : **다른 템플릿 파일 내용** 또는 **매크로**를 가져올 때 사용한다.
	+ 가져오는 템플릿은 캐시된 상태. 가져오는 템플릿에서 가져오는 변수는 사용불가능.

+ 다음 두 가지 방법으로 사용한다.

``` html
{% import "<매크로 정의 템플릿 이름>" as <템플릿 참조 변수>%}

{% from "<매크로 정의 템플릿 이름>" import <매크로 이름> as <템플릿 참조 변수>%}
{{ <매크로 참조 변수> }}
```

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221840840103

---
# 7. 파이썬 플라스크 CSS 사용하기

> <h3>학습목표

+ CSS에 대해 알아보고, 간단한 문법과 HTML에 적용하는 방법에 대해 알아보자.
+ 파이썬 플라스크에서 CSS 파일을 포함시키는 방법에 대해 알아보자.

## 1) CSS

> <h3>CSS란?

+ CSS(Cascading Style Sheets)는 마크업 언어(HTML)가 실제 표현되는 방법을 기술한 언어로 실제 사용되는 웹은 필연적으로 CSS를 포함한다.
+ 일반적인 웹에서 HTML은 기본 틀, 자바스크립트는 동적인 움직임을 담당하고 CSS는 웹의 모양을 꾸미는 디자인에 사용한다.
+ 설계된 CSS는 재활용이 가능하고 테마, 템플릿의 형태로 확장 가능하다.

> <h3>CSS 기능

+ CSS가 지원하는 기능은 다음과 같다.
	- HTML로부터 디자인적 요소를 분리해 정의하는 기능을 지원한다.
	- 잘 정의된 CSS는 서로 다른 여러 웹 페이지에 적용할 수 있다.
	- 웹 문서의 내용과 상관없이 디자인만 바꾸거나 디자인은 그대로 두고 웹 문서 내용을 변경할 수 있다.
	- 다양한 기기에 맞게 유동적, 탄력적, 동적으로 바뀌는 반응형 디자인이 가능하다.
	- 동일한 문서구조를 가지고 서로 다른 CSS 테마 적용이 가능하다.

> <h3>CSS 기본 문법

+ CSS는 선택자와 선언부로 구성된다. 
	- 선택자 : 스타일을 지정할 HTML 요소
	- 선언부 :  CSS 속성 이름과 값의 쌍의 형태다.
		- 선언부는 콜론(:)으로 구분된 다수의 항목을 포함하고 각 선언 후 항상 세미콜론(;)을 입력해야 한다.
		- 선언부는 중괄호로 각 선언부를 블록(block) 단위로 구분한다. 
		- 속성이 여러 개면 한 줄로 나열해도 상관없지만 가독성을 위해 여러 줄에 걸쳐 작성할 것을 추천한다.

``` html
선택자  {속성:값; 속성:값....}

예)
/* h3태그(선택자)의 색상을 파란색으로 크기는 16px로 지정한다.*/
h3 {
color:blue; font-size:16px;
}
```

> <h3>작성한 CSS를 HTML에 적용하기

#### 내부 스타일 시트

+ html 파일 안에 스타일을 기술하는 방법이다.
+ <head></head> 태그 사이 <style></style> 태그를 만들어 정의한다.
+ html과 css가 한 파일에 있어 작업이 쉽고 간편한 대신 재활용이 안되는 문제가 있다.

``` html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        background-color: gray;
      }

      h1 {
        color: blue;
        margin-left: 40px;
      }
    </style>
  </head>
  <body><center>
    <h1>Hello World!</h1>
  </body></center>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/117626153-c6594900-b1b1-11eb-8fed-afe25e62e9a0.png)

#### 외부 스타일 시트

+ CSS를 작성하는 가장 기본적인 방법이다.
+ 별도 파일에 CSS를 작성하고 필요로 하는 HTML 문서에서 불러와 사용하는 형식이다.
+ CSS는 동일한 위치에 파일을 배치하거나 url을 통해 다른 서버의 CSS 파일을 참조할 수도 있다.
+ 불러올 때는 link로 가져온다.

``` html
<link rel="stylesheet" type="text/css" href="test.css"> #내부 작성한 css, 경로 지정.
<link rel="stylesheet" type="text/css" href="http://... .css"> #다른 서버에 위치한 css
```

+ 내부 스타일 시트의 코드에서 head부분을 'test.css' 파일로 따로 저장하고, link를 통해 불러온다.

``` html
<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" type="text/css" href="test.css">
	</head>
	<body><center>
	<h1>Hello World!</h1>
	</body></center>
</html>
```

> test.css

``` html
body {
	background-color: gray;
}

h1 {
        color: blue;
        margin-left: 40px;
}
```

#### 인라인 스타일

+ html 태그에 필요한 디자인 속성을 직접 작성하는 형식이다.
+ 예제는 h1 태그에 스타일 값을 반영한다.

``` html
<!DOCTYPE html>
<html>
  <body><center>
    <h1 style="color:blue; margin-left:30px;">Hello World!</h1>
  </body></center>
</html>
```

## 2) 파이썬 플라스크에서 CSS 파일 포함시키는 방법

+ 이미 만들어진 CSS 파일을 가져와 사용하면 용이하다.
+ 다음 사이트를 참고하면 CSS 파일을 무료로 다운받을 수 있다.
+ CSS 뿐 아니라 다른 언어도 오픈 라이센스로 코드를 제공한다.

=> https://www.w3schools.com/

+ CSS를 사용하기 위해서는 작성한 HTML 파일을 렌더링했던것처럼 파일을 가져와야 한다.
+ 다음은 프로젝트 파일 폴더의 구조이다.

![image](https://user-images.githubusercontent.com/43658658/117628834-834ca500-b1b4-11eb-9441-4bae33b20c19.png)

+ 먼저, 파이썬 플라스크 서버 구동 파일(flask_server.py)이 있다.
+ 다음으로 HTML 파일을 담은 템플릿 폴더가 있다.
+ CSS와 자바스크립트, 이미지 같은 정적 파일을 담은 static 폴더가 있다.
	+ '.css' 확장자는 static 폴더 안에 저장한다.
	+ CSS 파일이 너무 많다면 static 폴더 내 별도의 CSS 폴더 내에 저장한다.

![image](https://user-images.githubusercontent.com/43658658/117629337-053cce00-b1b5-11eb-97a3-31ee983a6da8.png)

+ 위 상황을 기준으로 코드를 구성하자. 
+ 파이썬 서버 코드는 단순히 템플릿(home.html)을 렌더링하는 내용을 담는다.

> flask_server.py

``` python
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('home.html')
 
if __name__ == "__main__":
    app.run()
```

+ 렌더링할 템플릿(home.html) 내용에 다음과 같이 작성하면 CSS 파일(w3.css)을 포함시킨다.

> home.html

``` html
<!doctype html>
<html>
  <head>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/w3.css') }}">
  </head>
  <body>
  <p><h2>subject</h2>
  </p>
  </body>
</html>
```

+ static 폴대 내 css 폴더 내에 있는 w3.css 파일을 렌더링한다.
+ href로 나타나는 링크를 {{   }} 로 묶고 안에 url_for로 'static' 폴더에 filename으로 지정한 파일이 있다고 설정한다.

``` html
<link rel="stylesheet" href="{{ url_for('static', filename='css/w3.css') }}">
```

[목차](#Learning-Flask)

---
[출처]
+ https://blog.naver.com/dsz08082/221878406932
+ https://m.blog.naver.com/dsz08082/221855358279

---

# 8. 렌더링할 HTML 파일에 이미지 삽입

> <h3>학습목표

+ 정적 이미지 삽입과 동적 이미지 삽입을 알아보자.

## 1) 정적 이미지 삽입

+ 정적(static)인 이미지를 파일로 넣어 렌더링할 HTML 파일에서 불러오는 방법은 CSS 파일을 넣고 불러오는 방법과 동일하다. 
+ 다음과 같이 파일 구조를 만들어 static의 images 폴더에서 사진을 가져올 수 있도록 만든다.

![image](https://user-images.githubusercontent.com/43658658/117934212-67283f80-b33d-11eb-987e-944978fd968d.png)

> <h3>flask_server.py

+ 백엔드(파이썬 서버)는 단순히 템플릿(home.html)을 렌더링한다.

``` python
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('home.html')
 
if __name__ == "__main__":
    app.run()
```

> <h3>home.html
 
+ 아래와 같이 작성하면 템플릿을 불러올 때 지정한 이미지만을 가져온다.
+ url_for을 이용하며, static 폴더 내 image 폴더 내에 있는 어떤 파일을 가져온다.

``` html
<html>
  <head>
  </head>
  <body>
    <img src="{{ url_for('static', filename='image/파일이름.이미지 파일 확장자') }}">
  </div>
  </body>
</html>
```

## 2) 동적 이미지 삽입

+ 이미지가 계속 바뀌어야 한다면 파라미터로 이미지 파일의 이름을 넘겨오는 방식을 사용해야 한다.

> <h3>flask_server.py

+ render_template 함수로 HTML 파일에 파라미터를 넘기고 Jinja2 템플릿 문법을 사용해 파라미터를 인식한다.

``` python
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('home.html', image_file='image/파일이름.이미지 파일 확장자')
 
if __name__ == "__main__":
    app.run()
 ```

> <h3>home.html

+ 다음과 같이 작성하면 들어온 인자 값에 따라 다른 이미지를 띄운다. 
+ 신사2 템플릿 문법의 if 문을 넣어 파라미터로 인식시킬 수 있다. 
+ 문법 자체는 다음 파일에서 단독적인 의미를 가지지 않지만 파이썬 코드에서 전달한 파라미터를 인식하는데 목적이 있다.

``` html
<html>
  <head>
  </head>
  <body>
    {% if True %}
    <img src="{{ url_for('static', filename=image_file) }}">
    {% endif %}
  </body>
</html>
```

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221855380626

---

# 9. 파이썬 플라스크 파일 업로드 서버 구축

> <h3>학습 목표

+ 플라스크를 활용해 선택한 파일을 서버에 업로드하는 웹 페이지를 구성해보자.

[자료]
+ [9강 자료 바로가기](https://github.com/khyup0629/Flask_Todo_List_App/tree/main/-%20Learn%20Flask/9%EA%B0%95%20%EC%9E%90%EB%A3%8C)

## 1) 정적 파일 구성(9강)

+ 먼저 다음과 같이 전체 프로젝트 폴더를 구성한다.

![image](https://user-images.githubusercontent.com/43658658/117937942-790be180-b341-11eb-977d-5c305eaf3495.png)

+ static내에 images 폴더를 만들고 사이트에 사용할 이미지를 담는다.
+ 픽토그램 사이트에서 무료 이미지를 다운 받을 수 있다.

=> https://www.flaticon.com/

![image](https://user-images.githubusercontent.com/43658658/117938008-8aed8480-b341-11eb-82e0-b36c86785cbe.png)

## 2) 백엔드 서버 구현(9강)

> <h3>flask_server.py

``` python
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #파일 업로드 용량 제한 단위:바이트


# HTML 렌더링
@app.route('/')
def home_page():
	return render_template('home.html')


# 파일 리스트
@app.route('/list')
def list_page():
	file_list = os.listdir("./uploads")
	html = """<center><a href="/">홈페이지</a><br><br>"""
	html += "file_list: {}".format(file_list) + "</center>"
	return html


# 업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
	return render_template('upload.html')


# 파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		# 저장할 경로 + 파일명
		f.save('./uploads/' + secure_filename(f.filename))
		return render_template('check.html')


# 서버 실행
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
```

> <h3>코드 분석

``` python
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
```
+ Flask : 플라스크 서버 실행을 위해 사용.
+ render_template : html 파일 렌더링을 위해 사용.
+ request : 파일 업로드를 위해 사용.
+ secrue_filename : 업로드할 파일이 실제 시스템에 저장되기 전 이름을 보호하기 위해 사용.
	+ Werkzeug 모듈 0.16.0 버전에서는 from werkzeug import secure_filename를 통해 secure_filename을 사용할 수 있다.
	+ Werkzeug 모듈 1.0.0 버전에서는 from werkzeug.utils import secure_filename를 통해 secure_filename을 사용할 수 있다.

``` python
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
```

+ 주석 처리한 다음 문장을 실행하면 파일 업로드 용량 제한을 줄 수 있다. 필요에 따라 사용하면 된다. 
+ 파일 업로드 용량 제한 단위는 바이트임에 유의하자. 즉, 다음 예제코드는 16MB 용량을 최대 제한으로 둔다.

``` python
#HTML 렌더링
@app.route('/')
def home_page():
	return render_template('home.html')
```

+ 홈페이지 파일(home.html)을 렌더링한다. 홈페이지가 나타난다.

``` python
#업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
	return render_template('upload.html')
```

+ 업로드 파일(upload.html)을 렌더링한다. 업로드 페이지가 나타난다.

``` python
#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		#저장할 경로 + 파일명
		f.save('./uploads/' + secure_filename(f.filename))
		return render_template('check.html')
```

+ request.file['file'] : 업로드 페이지에서 POST 방식으로 해당 페이지로 넘어오면 requests 객체의 file 이라는 이름의 폼으로 전송된 파일을 가져온다.
+ f.save('./uploads/' + secure_filename(f.filename)) : secure로 파일 이름을 보호하고 f.save로 파일 객체를 지정한 폴더에 저장한다. 지정한 폴더는 업로드 폴더다.
	+ secure_filename 으로 보안처리를 하지 않으면 파일을 저장함에 있어 Permission Error가 뜬다.
+ 저장이 완료되면 완료 페이지(check.html)로 렌더링한다. 

``` python
# 파일 리스트
@app.route('/list')
def list_page():
	file_list = os.listdir("./uploads")
	html = """<center><a href="/">홈페이지</a><br><br>""" 
	html += "file_list: {}".format(file_list) + "</center>"
	return html
```

+ file_list = os.listdir("./uploads") : 업로드 폴더에 있는 파일 리스트를 가져온다.
+ html 코드가 간단하기 때문에 백엔드 서버에서 html 코드를 직접 작성해서 반환한다.
+ 작성된 html 코드가 나타내는 페이지는 아래와 같다.

![image](https://user-images.githubusercontent.com/43658658/117947073-d0fb1600-b34a-11eb-9251-73979b39d935.png)

``` python
#서버 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug = True)
```

+ 외부 서비스를 위한 기반을 위해 모든 IP에 대해 8080 포트로 바인딩하고 디버그 모드를 작동시킨다.
+ 만약 위의 코드로 오류가 난다면, host 번호를 127.0.0.1인 로컬 번호로 지정한다.

## 3) 프론트엔드 구현(9강)

> <h3>home.html, 홈페이지 구성

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>ftp_page</title>
  </head>

  <body>
    <center><h1>FTP Server</h1></center>
    <hr width="100%" color="black"/>

    <center>
    <form>
    <img src="{{ url_for('static',filename='images/upload.png') }}" width="50"
        style="margin-left: auto; margin-right: auto; display: block;" />
    <a href="./upload">파일 업로드</a><br><br>

    <img src="{{ url_for('static',filename='images/list.png') }}" width="50"
        style="margin-left: auto; margin-right: auto; display: block;" />
    <a href="./list">파일 목록</a><br><br><br>
    </form>
    </center>
  </body>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/117944904-b9bb2900-b348-11eb-819b-b5bca7937c72.png)

+ meta charset="UTF-8" : 페이지에 한글이 보이도록 하는 명령어.
+ hr : 너비 100%의 선을 생성.
+ img src : 이미지를 가져온다. width는 파일의 크기를 설정.
+ href : 하이퍼링크를 생성. "./upload"로 하면 현재 링크에서 upload가 추가된 URL로 이동한다.
+ br : 한 줄 띄우기.

> <h3>upload.html, 업로드 페이지 구성

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>pyftp</title>
  </head>

  <body>
    <center><h1>Upload Page</h1></center>
    <center><a href="/">홈페이지</a><br></center>
    <hr width="100%" color="black"/>
    <center><h3>Upload File!</h3></center>
    <hr width="100%" color="black"/>

    <img src="{{ url_for('static',filename='images/upload.png') }}" width="100"
        style="margin-left: auto; margin-right: auto; display: block;" />

    <br><br><center>
    <form action = "http://localhost:8080/fileUpload" method = "POST"
         enctype = "multipart/form-data">
    <input type = "file" name = "file" />
    <input type = "submit"/>
    </form></center>
  </body>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/117945735-93e25400-b349-11eb-822b-392ee50cbdd3.png)

+ form action = "http://localhost:8080/fileUpload" method = "POST" : POST 메서드 방식으로 해당 주소에 input을 보낸다.
+ enctype = "multipart/form-data" : 플라스크가 성공적으로 폼에 가져온 파일을 읽어내기 위해서는 entype 속성에 반드시 multipart/form-data 로 지정해야 한다. 
	+ 이는 파이썬 request를 이용해 파일을 업로드하는 구성이기 때문이다. 
	+ 제출을 누르면 /fileUpload 주소로 이동하면서 값을 넘긴다.
+ input type = "file" name = "file" : "파일 선택" 버튼과 선택한 파일 이름이 뜨는 공간이 생긴다.
+ input type = "submit" : 제출 버튼이 생긴다.

> <h3>check.html, 확인 페이지 구성

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>pyftp</title>
  </head>

  <body>
    <center><h1>Upload Page</h1></center>
    <center><a href="/">홈페이지</a><br><br><br></center>
    <center>
    <img src="{{ url_for('static',filename='images/checked.png') }}" width="100"
      style="margin-left: auto; margin-right: auto; display: block;" />
    </center>
      
    <center>
    <p>파일 업로드 성공!<p>
    </center>
  </body>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/117950271-fa697100-b34d-11eb-9da1-00374961824a.png)

+ p : p사이의 글자 출력

> <h3>파일 제출

![image](https://user-images.githubusercontent.com/43658658/117952554-3b628500-b350-11eb-8af2-3f74486e80ca.png)

+ 파일을 선택해 제출한 후 홈페이지의 파일 목록으로 가면 해당 파일이 저장된 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/43658658/117952693-5d5c0780-b350-11eb-9cc6-bf60ba773555.png)

+ 실제 uploads 폴더 내에도 저장되어 있음을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/43658658/117952850-84b2d480-b350-11eb-8b5f-1e8656236522.png)

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221859049633
+ https://github.com/neltia/flask-project/tree/master/01_File_Upload

---
# 10. 파이썬 플라스크 파일 다운로드 서버 구축

> <h3>학습 목표

+ 9강에 이어 파일 다운로드 기능을 추가해보자.

[자료]
+ [10강 자료 바로가기](https://github.com/khyup0629/Flask_Todo_List_App/tree/main/-%20Learn%20Flask/10%EA%B0%95%20%EC%9E%90%EB%A3%8C)

## 1) 정적 파일 구성(10강)

+ 먼저 다음과 같이 전체 프로젝트 폴더를 구성한다.

![image](https://user-images.githubusercontent.com/43658658/117937942-790be180-b341-11eb-977d-5c305eaf3495.png)

+ static내에 images 폴더를 만들고 사이트에 사용할 이미지를 담는다.
+ 픽토그램 사이트에서 무료 이미지를 다운 받을 수 있다.

=> https://www.flaticon.com/

![image](https://user-images.githubusercontent.com/43658658/118080304-e9276f80-b3f4-11eb-9efd-ced30a2d79f7.png)

## 2) 백엔드 서버 구현(10강)

> <h3>flask_server.py

``` python
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #파일 업로드 용량 제한 단위:바이트


# HTML 렌더링
@app.route('/')
def home_page():
	return render_template('home.html')


# 업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
	return render_template('upload.html')


# 파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		# 저장할 경로 + 파일명
		f.save('./uploads/' + secure_filename(f.filename))
		return render_template('check.html')


# 다운로드 HTML 렌더링
@app.route('/downfile')
def down_page():
	files = os.listdir("./uploads")
	return render_template('filedown.html',files=files)


# 파일 다운로드 처리
@app.route('/fileDown', methods = ['GET', 'POST'])
def down_file():
	if request.method == 'POST':
		sw=0
		files = os.listdir("./uploads")
		for x in files:
			if(x==request.form['file']):
				sw=1

		path = "./uploads/"
		return send_file(path + request.form['file'],
				attachment_filename = request.form['file'],
				as_attachment=True)


# 서버 실행
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
```

> <h3>코드 분석

+ 삭제된 부분 : 파일 리스트 코드
+ 추가된 부분 : 다운로드 관련 코드

``` python
# 다운로드 HTML 렌더링
@app.route('/downfile')
def down_page():
	files = os.listdir("./uploads")
	return render_template('filedown.html',files=files)
```

+ uploads에 있는 파일 목록들을 이용해 다운로드 페이지(filedown.html)을 렌더링한다.

``` python
# 파일 다운로드 처리
@app.route('/fileDown', methods = ['GET', 'POST'])
def down_file():
	if request.method == 'POST':
		path = "./uploads/"
		return send_file(path + request.form['file'],
				attachment_filename = request.form['file'],
				as_attachment=True)
```

+ uploads 폴더 내에 request된 파일이 있는지 확인한다.
+ send_file 함수는 지정한 경로에 있는 파일을 다운로드 받을 수 있도록 해준다.
	+ send_file(다운 받을 파일, 다운 받아지는 파일의 이름 설정)

## 3) 프론트엔드 구현(10강)

> <h3>home.html

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>ftp_page</title>
  </head>

  <body>
    <center><h1>FTP Server</h1></center>
    <hr width="100%" color="black"/>

    <center>
    <form>
    <img src="{{ url_for('static',filename='images/upload.png') }}" width="50"
        style="margin-left: auto; margin-right: auto; display: block;" />
    <a href="./upload">파일 업로드</a><br><br>

    <img src="{{ url_for('static',filename='images/download.png') }}" width="50"
        style="margin-left: auto; margin-right: auto; display: block;" />
    <a href="./downfile">파일 다운로드</a><br><br><br>
    </form>
    </center>
  </body>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/118084468-bdf44e80-b3fb-11eb-82d5-3106014ead05.png)

+ 변경된 부분 : 하이퍼링크를 "./downfile"로 가게해서 다운로드 페이지(filedown.html)이 열리도록 한다.
	+ 그림을 download.png를 가져오도록 한다.

> <h3>filedown.html

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>pyftp</title>
  </head>

  <body>
    <center><h1>Download Page</h1></center>
    <center><a href="/">홈페이지</a><br></center>
    <hr width="100%" color="black"/>
    <center><h3>Download File!</h3></center>
    <hr width="100%" color="black"/>

    <img src="{{ url_for('static',filename='images/download.png') }}" width="70" 
        style="margin-left: auto; margin-right: auto; display: block;" /><br><br>

    <center>
    <form action = "http://localhost:8080/fileDown" method = "POST"
         enctype = "multipart/form-data">
    <input type = "text" name = "file" />
    <input type = "submit"/>
    </form></center><br><br><br>

    <hr width="100%" color="black"/>
    <center><h3>File List</h3></center>
    <hr width="100%" color="black"/>

    <img src="{{ url_for('static',filename='images/list.png') }}" width="50" 
    style="margin-left: auto; margin-right: auto; display: block;" /><br>

    <ul>
         {% for n in files %}
         <li>{{n}}</li>
         {% endfor %}
    </ul>
  </body>
</html>
```

![image](https://user-images.githubusercontent.com/43658658/118084773-3824d300-b3fc-11eb-8c23-23b8a9c43c52.png)

``` html
	<form action = "http://localhost:8080/fileDown" method = "POST"
		 enctype = "multipart/form-data">
	<input type = "text" name = "file" />
	<input type = "submit"/>
```

+ POST 메서드 형식으로 text 형식, 이름이 'file'인 input을 /fileDown URL로 보내지도록 한다.
+ 서버 코드에서 request.form('file')을 다운로드(send_file)할 수 있다.

``` html
     <ul>
	{% for n in files %}
	<li>{{n}}</li>
	{% endfor %}
     </ul>
```

+ 서버 코드에서 uploads 폴더 내에 있는 파일 리스트와 함께 filedown.이 렌더링되는데 이때의 파일 리스트가 들어갈 자리가 {{n}}이다.
+ 즉, 페이지 아래에 uploads 폴더 내의 파일 리스트를 보여준다.
+ ul : 파일 리스트를 ●(bulleted) 리스트로 정리해서 보여준다. <li>와 같이 활용한다.
	+ ol : ordered list의 약자로 숫자(1, 2, 3)나 알파벳(a, b, c), 로마자(I, II, III, IV) 등의 순서가 있는 목록을 나타낸다.
	+ ul : unordered list의 약자로 순서가 없는 목록(●)을 나타낸다.
	+ dl : definition list의 약자로 사전처럼 용어를 설명하는 목록을 나타낸다.

> <h3>check.html, upload.html

+ check.html과 upload.html은 9강과 코드가 동일하다.

> <h3>동작 확인

+ 홈페이지에서 '파일 업로드'로 들어간다.
+ 바탕화면에 있는 'shield.png' 파일을 선택한 후 제출한다.

![image](https://user-images.githubusercontent.com/43658658/118084998-96ea4c80-b3fc-11eb-9fcd-a5b9e501a0f0.png)

+ 홈페이지로 돌아간 후 '파일 다운로드'로 들어간다.
+ 아래쪽 'File List'에 방금 업로드한 'shield.png' 파일이 확인된다.
+ 'shield.png'를 입력하고 '제출'을 누르면 파일이 정상적으로 다운로드 되는 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/43658658/118085175-e6c91380-b3fc-11eb-8b53-a9b3fba7c597.png)

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221868934940
+ https://github.com/neltia/flask-project/tree/master/02_File_Control

---
# 11. 파이썬 플라스크 에러와 로깅

> <h3>학습 목표

+ 페이지 에러에 관한 사용자 지정 페이지를 만들어보자.
+ 로그를 남기는 방법에 대해 알아보자.

## 1) 에러 처리

+ 플라스크는 HTTP 오류 코드에 대해 사용자 지정으로 처리하는 방식을 제공한다. 
+ HTTP 통신 응답 상태 코드(주요 상태 코드)
	+ 200 : 서버가 요청을 제대로 처리했다는 뜻.
	+ 403 : 서버는 요청은 이해했는데 권한이 없음.
	+ 404 : 서버가 요청한 페이지를 찾을 수 없음.
	+ 500 : 서버는 요청을 처리하는 과정에서 잘못된 요청을 보호하기 위해 기대하지 않은 조건 응답을 보여줌 요청 처리 과정에서 잘못된 요청을 보호하기 위해 기대함.
	+ 502 : 서버의 잘못된 게이트 웨이로 인한 에러.
	+ 503 : 서비스를 사용할 수 없음.

+ errorhandler 데코레이터를 사용하면 HTTP 오류 코드에 해당하는 페이지를 정의한다.
+ 다음과 같이 데코레이터를 설정하면 단순한 에러코드 화면이 아닌 사용자가 별도로 지정한 화면으로 처리한다.

``` python
@app.errorhandler(404)
def page_not_found(error):
     return render_template('page_not_found.html'), 404
```

+ 코드를 살펴보면 반환값이 두 개다. 뒤에 넘기는 인자 값인 404는 요청에 대한 응답값으로 404를 넘겨주지 않으면 없는 페이지에 대한 요청을 성공(200)으로 처리한다. 
+ 이처럼 errorhandler를 사용할 때는 뒤에 상응하는 에러코드를 적어야만 한다.

> <h3>flask_server.py

+ 앞서 실습했던 10강의 서버 코드에 없는 페이지의 에러에 대한 렌더링을 추가해보자.
+ 아래의 코드를 10강의 서버 코드에 추가한다.

``` python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

> <h3>page_not_found.html

+ 없는 페이지에 대한 에러(404)가 발생할 때 나타나는 페이지를 구성한다.

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
    <title>pyftp</title>
  </head>

  <body>
    <center><h1>Not Found Page</h1></center>
    <center><a href="/">홈페이지</a><br><center>
    <hr width="100%" color="black"/>
    <center><h3>404</h3></center>
    <hr width="100%" color="black"/>
  </body>
</html>
```

> <h3>동작 확인

+ 없는 페이지에 대한 URL을 입력하면 아래와 같이 page_not_found.html페이지 화면이 나타난다.

![image](https://user-images.githubusercontent.com/43658658/118089674-94d7bc00-b403-11eb-97b5-ac63469b4b50.png)

## 2) 로깅

+ 로깅은 로그를 남기는 작업이다. 어떠한 오류나 혹은 특정한 요청 등이 발생하면 이에 대한 로그를 남기고자 할 때 로깅을 사용한다. 
+ 애플케이션 객체가 생성된 상태에서 logger 인스턴스에 접근해 로깅한다. 
+ 다음은 로깅 예시다.

``` python
	app.logger.debug('A value for debugging') # 디버깅 메시지 로깅
	app.logger.warning('A warning ocurred (%d apples)', 42) # 경고 메시지 남기기
	app.logger.error('An error ocurred') # 에러 메시지 남기기
```

+ 로깅을 활용하면 디버그 기능 활성화 없이도 특정 상황에 처한 경우를 디버깅할 수 있고 로그 메시지를 직접 정해 출력한다는 점에서 디버그가 용이하다.
+ errorhandler에 logger 기능을 추가하면 아래와 같다.

``` python
@app.errorhandler(404)
def page_not_found(error):
     app.logger.error(error)
     return render_template('page_not_found.html'), 404
```

+ 없는 페이지로 이동하면 파이썬 개발환경의 터미널에 아래와 같이 에러가 발생한 시각과 어떤 에러가 발생했는지에 대한 데이터가 기록된다.

![image](https://user-images.githubusercontent.com/43658658/118090679-ce5cf700-b404-11eb-8c52-e3c17b590786.png)

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221871535831

---
# 12. 로그인과 세션, SQLite DB

> <h3>학습 목표

+ 플라스크 웹 프레임워크의 로그인 및 세션 처리를 알아보고 데이터베이스를 연결해 사용자 정보를 관리해보자.
+ 간단히 회원가입 및 로그인을 할 수 있는 폼을 만들고 데이터베이스로 로그인 기능을 만들어보자.
+ 로그인 여부에 따라 세션을 구현해 로그인을 해야만 서비스를 이용할 수 있게 해보자.
+ 회원 정보가 있을 경우 네이버 아이디를 입력받아 네이버 블로그를 열 수 있도록 해보자.

[자료]
+ [12강 자료 바로가기](https://github.com/khyup0629/Flask_Todo_List_App/tree/main/-%20Learn%20Flask/12%EA%B0%95%20%EC%9E%90%EB%A3%8C)

## 1) 라이브러리 설치 및 파일 구성

> <h3>라이브러리 설치

+ 로그인을 위한 데이터베이스 사용 및 소스코드를 실행하기 위해 다음 라이브러리를 설치한다.
+ 해당 라이브러리는 MySQL, MariaDB 등 MySQL 계열의 관계형 데이터베이스를 별도 사용하기 위해 설치한다.
+ 파이썬 IDE 터미널에 다음의 명령어를 입력한다.

```
pip install flask-sqlalchemy
```

> <h3>파일 구성

+ 다음과 같이 폴더와 파일을 구성한다.

![image](https://user-images.githubusercontent.com/43658658/118219746-1176a300-b4b5-11eb-9918-58b5d2382bec.png)

+ static 폴더 내 images 폴더를 만들고 안에 네이버 아이콘 이미지를 넣는다.

![image](https://user-images.githubusercontent.com/43658658/118219872-539fe480-b4b5-11eb-8c41-28ca17ae511d.png)

## 2) 회원가입 및 로그인 폼 만들기

> <h3>base.html

+ base.html은 모든 페이지의 베이스 코드다. 
+ 다른 페이지에서 이 페이지를 포함시키면 해당 페이지 내용 전 아래 페이지를 포함시켜 중복요소를 최소화시킨다. 
+ 브라우저 제목, 브라우저 내 제목, 홈 페이지의 하이퍼링크를 담는다.
+ 이 코드를 다른 html 문서에서 참조하게 되면 그 html가 보여주는 페이지 위에 항상 base.html이 구현한 이미지가 나타난다.

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
	<title>flask Service</title>
  </head>
  <body><center><div>
  	<h1>Service Page</h1>
  	<hr width="100%" color="black"/>
  	<center>
  		<img src="{{ url_for('static',filename='images/naver.png')}}"/>
  		<h3>Naver Blogpage Open</h3>
  	</center>
  	<hr width="100%" color="black"/>
  	<a href="/">홈페이지</a>
	</div></center>
	<hr>
	{% block content %}{% endblock %}
  </body>
</html>
```

> <h3>register.html

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		<p>또 가입하시게요?</p>
	{% else %}
	<center><div>
		<h2>Register</h2>
		<form action="/register/" method="POST">
		<input type="username" name="username" placeholder="Username"><br>
		<input type="password" name="password" placeholder="Password"><br>
		<input type="email" name="email" placeholder="email@naver.com">
		<br><br>
		<input type="submit" value="회원가입">
		</form>
	</div></center>
	{% endif %}
	{% endblock %}
</html>
```

+ 회원가입 페이지이다.
+ extends "base.html" : base.html을 참조해 위에 base.html의 구현된 이미지가 뜨게 한다.
+ if session['logged_in'] : 이미 로그인이 되어 있다면 '또 가입하시게요?'라는 문구가 뜨도록 한다.

``` html
<center><div>
	<h2>Register</h2>
	<form action="/register/" method="POST">
	<input type="username" name="username" placeholder="Username"><br>
	<input type="password" name="password" placeholder="Password"><br>
	<input type="email" name="email" placeholder="email@naver.com">
	<br><br>
	<input type="submit" value="회원가입">
	</form>
</div></center>
```

+ 회원가입 버튼을 누르면 POST 메서드로 '/register'페이지로 username, password, email 정보가 request 형태로 보내지도록 한다.
+ placeholder : 입력 박스에 아무것도 입력되어 있지 않을 때 뜨는 문구

> <h3>login.html

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		<p>이미 로그인하셨습니다.</p>
	{% else %}
	<center><div>
		<h2>Login</h2>
		<form action="/login" method="POST">
		<input type="username" name="username" placeholder="Username">
		<input type="password" name="password" placeholder="Password">
		<br><br>
		<input type="submit" value="로그인">
		</form>
	</div></center>
	{% endif %}
	{% endblock %}
</html>
```

+ 회원가입을 완료하거나 로그인했을 시에 나타나는 페이지이다.
+ 이미 로그인이 되어 있다면 '이미 로그인하셨습니다.'라는 문구가 뜨도록 한다.
+ '로그인'버튼을 누르면, POST 메서드 방식으로 '/login' URL로 username, password가 request 형태로 보내지도록 한다.

## 3) 데이터베이스 설정

+ 데이터베이스 설정을 위한 라이브러리 : SQLAlchemy

``` python
from flask_sqlalchemy import SQLAlchemy
```

+ 플라스크에서 데이터베이스를 설정해보자.
+ 플라스크 객체를 설정하고 app.config를 통해 데이터베이스 주소를 적는다.
+ test.db 데이터베이스 파일이 없으면 만들고 있으면 연결할 것이다.
+ 플라스크 객체를 위한 데이터베이스를 만든다.

``` python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
```

+ 회원 정보를 담는 데이터베이스의 파일 모델을 정의하자.
+ 가입 시 요구할 정보는 아이디, 비밀번호, 이메일이다.
+ **db.Column**으로 자료형 등을 정의한다.
+ id를 기본 데이터베이스 자료형으로 만들고 그 안에 username, password, email을 넣어 만든다.
	+ id : 기본 데이터베이스, 정수형으로 설정
	+ username, password, email : 문자형으로 설정
		+ username과 email은 고유값이므로 unique=True

``` python
class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))
	email = db.Column(db.String(80), unique=True)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
```

+ 다음과 같이 작성하면 정의한 클래스를 사용해 데이터베이스를 필터링한다.

``` python
User.query.filter_by(username=name) #데이터베이스에 인자 값을 기준으로 필터 쿼리 날리기
```

+ 다음은 데이터베이스 값 추가다.

``` python
db.session.add(User(username=request.form['username'], password=request.form['password'], 
	email=request.form['email']))
```

+ sqlite는 데이터베이스에 쿼리를 보냈다면 적용을 위해 commit 작업이 필요하다.

``` python
db.session.commit()
```

+ 프로그램이 시작 시 데이터베이스를 만들고 시작한다.

``` python
if __name__ == '__main__':
	db.create_all()
```

## 4) 세션 설정

+ 세션은 HTTP에서 로그인과 같은 인증 처리나 장바구니 같은 기능을 구현하기 위해 클라이언트와 서버 간 상태 값을 저장하는 기술이다.
+ 세션은 클라이언트(웹 브라우저)가 서버에 접속 시 서버에서 클라이언트에 부여하는 아이디값으로 표현된다.
+ 이 아이디값을 세션 아이디로 부르며 HTTP 헤더에 쿠키를 이용해 생성된다.

+ 웹에서의 쿠키는 HTTP 헤더에 포함되며 key=value 형태를 가진다. 
+ 웹 서버로부터 쿠키를 받은 웹 브라우저는 다시 웹 서버에 접속할 때 전 서버에서 받았던 쿠키를 헤더에 넣어 보내 현재 상태를 파악한다.

+ 기본 세션을 이용하려면 세션 모듈을 불러온다.

``` python
from flask import session
```

+ 플라스크 객체에 암호화 키를 시크릿키로 정의한다.

``` python
if __name__ == '__main__':
	db.create_all()
	app.secret_key = "123123123"
```

+ app.py에서 메인 페이지인 home 함수에는 다음과 같이 정의한다. 
+ 이는 세션을 가져와 로그인 여부를 확인한다. 로그인 여부를 확인해 index.html을 불러오고 상황에 따라 로그인 되었다면 사용자 아이디를 전달한다.

``` python
@app.route('/', methods=['GET', 'POST'])
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = request.form['username']
			return render_template('index.html', data=blogopen(username))
		return render_template('index.html')
```

> <h3>index.html

+ 로그인이 되어 있다면
	+ app.py에서 전달 받은 블로그 정보가 있다면 그것을 표시하고 
	+ 블로그 정보가 없다면 블로그에 대한 정보를 제출할 수 있도록 한다.
+ 로그인이 되어 있지 않다면
	+ 로그인 또는 회원 가입 링크를 띄운다.

``` python
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		{% if data %}
			<h3>{{ data }}</h3>
		{% else %}
		<center><div>
			<a href="/logout">Logout</a><br><br>
			<form action="" method="POST">
			<input type="username" name="username" placeholder="Blog id">
			<input type="submit" value="Open">
			</form>
		</div></center>
		{% endif %}

	{% else %}
	<center><div>
		<p>로그인하지 않은 상태입니다. </p>
		<p>서비스를 이용하려면 로그인해주세요.</p>
		<a href="/login">Login</a>
		<a href="/register">Register</a>
	</div></center>
	{% endif %}
	{% endblock %}
</html>
```

![image](https://user-images.githubusercontent.com/43658658/118230289-6243c700-b4c8-11eb-9b01-e7f3e949b5ea.png)
![image](https://user-images.githubusercontent.com/43658658/118230964-5b698400-b4c9-11eb-9136-e38ad3a582f4.png)

## 5) 블로그 페이지 오픈 설정

> <h3> service.py

+ 네이버 블로그 URL은 'https://blog.naver.com/' + '회원 아이디'로 정의된다.
+ '회원 아이디'에 해당하는 정보를 입력해서 제출하면 그 정보를 통해 블로그 페이지를 열어주는 blogopen이란 함수를 정의한다.

``` python
import webbrowser


def blogopen(url):
	link = 'https://blog.naver.com/%s'
	blog = link % (url)
	webbrowser.open(blog)
```

![image](https://user-images.githubusercontent.com/43658658/118230964-5b698400-b4c9-11eb-9136-e38ad3a582f4.png)

## 6) 서버 구현

> <h3>app.py

``` python
from flask import Flask, url_for, render_template
from flask import request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from service import blogopen

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(error):
     return render_template('page_not_found.html'), 404


class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))
	email = db.Column(db.String(80), unique=True)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email


@app.route('/', methods=['GET', 'POST'])
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = request.form['username']
			return render_template('index.html', data=blogopen(username))
		return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Dont Login'
		except:
			return "Dont Login"


@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'],
			email=request.form['email'])

		db.session.add(new_user)
		db.session.commit()
		return render_template('login.html')
	return render_template('register.html')


@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == '__main__':
	db.create_all()
	app.secret_key = "123123123"
	app.run(host='127.0.0.1', debug=True)
```

> <h3>코드 분석

+ 앞서 설명했던 부분들은 생략하고 분석한다.

```
@app.errorhandler(404)
def page_not_found(error):
     return render_template('page_not_found.html'), 404
```

+ 앞서 11강에서 설명한 요청한 페이지가 없을 때 사용자 지정된 페이지를 나타내는 코드이다.

``` python
@app.route('/', methods=['GET', 'POST'])
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = request.form['username']
			return render_template('index.html', data=blogopen(username))
		return render_template('index.html')
```

+ 홈페이지(index.html)로 들어갈 때 로그인이 되어 있지 않다면 바로 홈페이지(index.html)을 띄운다.
+ 로그인이 되어 있다면
	+ 로그인 페이지(login.html)에서 '로그인' 버튼을 눌러 홈페이지로 올 경우(POST) username을 통해 blogopen 함수를 보내면서 홈페이지(index.html)를 연다.
	+ 홈페이지 링크를 눌러서 들어올 경우(GET) 그냥 홈페이지(index.html)를 띄운다.

![image](https://user-images.githubusercontent.com/43658658/118230325-725ba680-b4c8-11eb-9b8d-e437959584c3.png)
![image](https://user-images.githubusercontent.com/43658658/118230964-5b698400-b4c9-11eb-9136-e38ad3a582f4.png)

``` python
@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Dont Login'
		except:
			return "Dont Login"
```

+ 홈페이지(index.html)에서 'Login' 링크를 누르면(GET) 로그인 페이지(login.html)를 띄운다.
+ 로그인 페이지(login.html)에서 '로그인' 버튼을 통해 제출하면(POST) 보내져 온 정보(username, password)를 통해 데이터베이스(User) 클래스를 필터링해서 찾는다.
+ 필터링한 정보가 존재하는 경우, 로그인 세션 상태를 True로 변경하고 홈페이지(index.html)로 보낸다.
+ 필터링한 정보가 존재하지 않는 경우, "Dont Login"이라는 문구가 뜨도록 한다.
+ 마찬가지로 로그인을 함에 있어 정상적인 로그인 외 예외적인 경우가 발생하면 "Dont Login" 문구가 뜨도록 한다.

![image](https://user-images.githubusercontent.com/43658658/118230831-32e18a00-b4c9-11eb-8f27-ac629cec868e.png)
![image](https://user-images.githubusercontent.com/43658658/118231271-dd59ad00-b4c9-11eb-984d-d6d5126d045a.png)

``` python
@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'],
			email=request.form['email'])

		db.session.add(new_user)
		db.session.commit()
		return render_template('login.html')
	return render_template('register.html')
```

+ 홈페이지(index.html)에서 'Register'링크를 누르면(GET) 'register.html' 페이지를 띄운다.
+ 'register.html' 페이지에서 '회원가입'버튼을 통해 '/register'로 오게 되면(POST)   
 회원에 대한 정보(username, password, email)을 Class 형태로 데이터베이스에 저장하고   
 로그인 페이지('login.html')를 띄운다.

![image](https://user-images.githubusercontent.com/43658658/118230390-90290b80-b4c8-11eb-9cfa-68851d80cb35.png)

``` python
@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))
```

+ '로그아웃' 링크를 누르면 로그인 세션을 False로 바꾸고 홈페이지(index.html)로 간다.

![image](https://user-images.githubusercontent.com/43658658/118230325-725ba680-b4c8-11eb-9b8d-e437959584c3.png)

> <h3>동작 확인

+ 제일 처음 접속하면 로그인이 되어 있지 않으므로 아래와 같이 나타난다.

![image](https://user-images.githubusercontent.com/43658658/118230325-725ba680-b4c8-11eb-9b8d-e437959584c3.png)

+ Register 버튼을 누른다.
+ 정보를 입력하고 '회원가입' 버튼을 누른다.

![image](https://user-images.githubusercontent.com/43658658/118230390-90290b80-b4c8-11eb-9cfa-68851d80cb35.png)

+ 정보가 데이터베이스에 저장된 후 로그인 페이지가 나타난다.
+ 회원 가입 했을 때의 username과 비밀번호를 이용해 로그인한다.

![image](https://user-images.githubusercontent.com/43658658/118230831-32e18a00-b4c9-11eb-8f27-ac629cec868e.png)

+ 블로그 아이디를 입력하는 페이지가 나온다.
+ 네이버 아이디를 입력하고 'Open'을 누르면 자신의 네이버 블로그를 연다.

![image](https://user-images.githubusercontent.com/43658658/118230964-5b698400-b4c9-11eb-9136-e38ad3a582f4.png)

+ 'Log out'을 누르면 홈페이지로 돌아가면서 로그 아웃 된다.

![image](https://user-images.githubusercontent.com/43658658/118230325-725ba680-b4c8-11eb-9b8d-e437959584c3.png)

+ 데이터베이스에 없는 정보로 로그인하려 하면 'Dont Login' 문구가 나타난다.

![image](https://user-images.githubusercontent.com/43658658/118231271-dd59ad00-b4c9-11eb-984d-d6d5126d045a.png)

+ 마찬가지로 아이디만 입력하고 비밀번호를 입력하지 않은 채로 로그인을 시도하면 'Dont Login' 문구가 나타난다.

![image](https://user-images.githubusercontent.com/43658658/118231363-fb271200-b4c9-11eb-8720-67462f326ad3.png)

[목차](#Learning-Flask)

---
[출처]
+ https://m.blog.naver.com/dsz08082/221874500996

---
# 13. 로그인 서비스 CSS 적용

> <h3>학습 목표

+ 플라스크에서 CSS 파일을 불러오는 법을 알아보자.
+ CSS를 적용시켜보자.

[자료]
+ [13강 자료]

## 1) 파일 구성

+ 이전 12강과 비교해서 HTML 템플릿과 서버 구현 코드와 내용은 크게 다르지 않고, CSS 파일이 추가되었다.
+ CSS 파일은 static 폴더에 추가한다.
	+ CSS 파일은 메모장에서 '.css' 형식으로 저장하면 생성된다.

![image](https://user-images.githubusercontent.com/43658658/118481397-6aad3380-b74e-11eb-802c-81572b5d732b.png)

+ static/images에 home.png 이미지를 추가한다.

![image](https://user-images.githubusercontent.com/43658658/118481459-7a2c7c80-b74e-11eb-921b-ff456fbaa518.png)

## 2) 플라스크 CSS 파일 불러오는 법

+ 플라스크에서 CSS 파일을 불러오려면 HTML 파일을 렌더링하되 HTML 파일 내에 작성한 CSS를 불러오는 태그를 작성하면 된다. 
+ CSS를 HTML 에 적용하는 방법은 **내부, 외부, 인라인** 스타일이 있으며 여기서는 **외부**를 사용한다.
+ 아래의 코드를 html의 head 사이에 넣으면 외부 방식으로 CSS 파일이 적용된다.

``` html
<link rel="stylesheet" type="text/css" href="이름.css"> #내부 작성한 css, 경로 지정.
```

## 3) 12강 자료에서 CSS 적용하기

+ 모든 템플릿에서 base.html을 불러오므로 작성한 CSS 파일을 base.html에서만 불러와도 다른 모든 템플릿에 적용된다.
+ base.html 에서 모든 템플릿 위에 쌓이는 상단 레이아웃에 쓰이는 이미지 크기를 변경했고, 집 모양을 누르면 메인 화면으로 돌아오도록 변경했다.

> <h3>base.html

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
  <head>
	<title>flask Service</title>
	<link rel="stylesheet" href="{{ url_for('static', filename='file.css') }}">
  </head>
  <body><center><div>
  	<hr width="100%" color="black"/>
  	<center>
  		<img src="{{ url_for('static',filename='images/naver.png')}}" width="50" />
  		<h3>Naver Blogpage Open</h3>
  	</center>
  	<hr width="100%" color="black"/>
    <a href="/"><img src="{{ url_for('static',filename='images/home.png')}}" width="30" /></a>
	</div>
  	</center>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>
```

> <h3>CSS 코드 분석

+ 사이트의 모든 버튼(로그인, 회원가입, 로그아웃)은 버튼 디자인 모음에서 가져왔다.
+ 버튼 디자인 모음 : 	
	+ https://nanati.me/css-button-design/
	+ https://codepen.io/

``` css
#btn {
   background-color: #c47135;
   border: none;
   color: #ffffff;
   cursor: pointer;
   display: inline-block;
   font-family: 'BenchNine', Arial, sans-serif;
   font-size: 1em;
   line-height: 1em;
   margin: 15px 40px;
   outline: none;
   position: relative;
   font-weight: 700;
   white-space:nowrap;
}

#btn:before,
#btn:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}

#btn:before {
  border-color: #c47135;
  border-right-width: 2px;
  border-top-width: 2px;
  right: -5px;
  top: -5px;
}
#btn:after {
  border-bottom-width: 2px;
  border-color: #c47135;
  border-left-width: 2px;
  bottom: -5px;
  left: -5px;
}
#btn:hover,
#btn:hover {
  background-color: #c47135;
}
#btn:hover:before,
#btn.hover:before,
#btn:hover:after,
#btn.hover:after {
  height: 100%;
  width: 100%;
}
```

![image](https://user-images.githubusercontent.com/43658658/118491342-dd6fdc00-b759-11eb-99d3-be8c8e314639.png)

+ 메인 화면 등 메시지를 표시할 부분은 메시지 상자를 위해 500 x 400 크기의 모서리가 5px만큼 둥근 테두리 상자를 넣었다.

``` css
#message {
    width:500px;
    height: 400px;
    border: 2px solid gray;
    border-radius: 5px;
}
```

![image](https://user-images.githubusercontent.com/43658658/118491317-d3e67400-b759-11eb-83fa-bf1a54c84be4.png)

+ 다음은 회원가입 폼을 만든다.
+ 기본적으로 메시지 박스와 동일하게 박스 내에 글자가 존재하도록 작성한다.
+ register-form label or input은 register-form 내에 label이나 input이 있을 경우 register-form을 적용하는 것만으로도 자동으로 label, input의 서식이 적용된다.
+ [type='submit']을 통해 input의 submit 타입만 따로 서식을 지정할 수 있다.
+ 테두리를 만들고 각 라벨과 버튼의 간격을 부여한다.

``` css
/* register-form */
#register-form {
    width:300px;
    border: 2px solid gray;
    border-radius: 5px;
}

#register-form input, #register-form label{
    display: block;
}

#register-form label{
    margin-top: 0px;
}

#register-form input{
    margin-top: 0px;
}

#register-form input[type='submit']{
    margin: 5px auto;
}
```

![image](https://user-images.githubusercontent.com/43658658/118491397-ee205200-b759-11eb-959f-014a62a3ced5.png)

+ 다음은 로그인 폼이다.

``` css
/* login form */
#login-form {
    width:300px;
    border: 2px solid gray;
    border-radius: 5px;
}

#login-form input, #login-form label{
    display: block;
}

#login-form label{
    margin-top: 10px;
}

#login-form input{
    margin-top: 5px;
}

#login-form input[type='submit']{
    margin: 10px auto;
}
```

![image](https://user-images.githubusercontent.com/43658658/118491223-b7e2d280-b759-11eb-837d-9d7716b40d13.png)

## 4) 템플릿 파일 코드 변경

> <h3>index.html

+ base.html에서 CSS 파일을 적용했으므로 extends "base.html"을 한 것만으로도 다른 모든 템플릿에서 CSS를 적용할 수 있다.
+ CSS 코드에서 이름지어줬던 '#btn'(버튼) '#message'(메시지 박스)를 id='적용할 서식 이름'을 통해 적용할 수 있다.
+ 즉, id="btn"로 버튼 서식을 적용할 수 있고, id="message"로 메시지 박스 서식을 적용할 수 있다.

+ 12강에서 **하이퍼링크** 형식으로 로그인, 회원가입, 로그아웃을 구현했다면,
+ 13강에서는 **버튼** 형식으로 CSS를 적용해 구현했다.

+ 여담으로 한 가지 의문점은 분명 'Register' 버튼을 누르면 '/register'로 이동하게 작성했는데 실제로 URL은 '/register/'로 이동한다는 것이다.

``` html
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		{% if data %}
			<h3>{{ data }}</h3>
		{% else %}
		<center>
			<button type="button" id="btn" onclick="location.href='/logout'">Logout</button>
			<form action="" method="POST" id="message">
			  <br><input type="username" name="username" placeholder="Blog id">
			  <input type="submit" value="Open">
			</form>
		</center>
		{% endif %}

	{% else %}
	<center>
		<button type="button" id="btn" onclick="location.href='/login'">Login</button>
		<button type="button" id="btn" onclick="location.href='/register'">Register</button>
		<div id="message">
			<p>로그인하지 않은 상태입니다. </p>
			<p>서비스를 이용하려면 로그인해주세요.</p>
		</div>
	</center>
	{% endif %}
	{% endblock %}
</html>
```

+ 로그인이 되어 있지 않다면

![image](https://user-images.githubusercontent.com/43658658/118487415-a5669a00-b755-11eb-9ed4-4a8ad1df97b1.png)

+ 로그인이 되어 있다면

![image](https://user-images.githubusercontent.com/43658658/118487559-cdee9400-b755-11eb-9774-01f0889ee749.png)

> <h3>register.html

+ id="register-form"을 통해 CSS 코드의 register-form 서식을 적용했다.

``` html
<!DOCTYPE html>
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		<p>또 가입하시게요?</p>
	{% else %}
	<center><div>
		<h2>Register</h2>
		<form action="/register/" method="POST" id="register-form">
		  <label class="legend">아이디</label>
		  <input type="username" name="username" placeholder="ID"><br>

		  <label class="legend">비밀번호</label>
		  <input type="password" name="password" placeholder="Password"><br>

		  <label class="legend">이메일</label>
		  <input type="email" name="email" placeholder="email@naver.com">
		  <br><br>
		  <input type="submit" value="회원가입">
		</form>
	</div></center>
	{% endif %}
	{% endblock %}
</html>
```

![image](https://user-images.githubusercontent.com/43658658/118490356-d399a900-b758-11eb-9d4a-d61a28692c42.png)

> <h3>login.html

+ register-form과 마찬가지로 login-form을 적용한다.

``` html
<!DOCTYPE html>
<html>
	{% extends "base.html" %}
	{% block content %}
	{% if session['logged_in'] %}
		<p>이미 로그인하셨습니다.</p>
	{% else %}
	<center><div class=login>
		<h2>Login</h2>
		<form action="/login" method="POST" id="login-form">
		  <label class="legend">아이디</label>
		  <input type="username" name="username" placeholder="ID">

		  <label class="legend">비밀번호</label>
		  <input type="password" name="password" placeholder="Password"><br><br>

		  <input type="submit" value="로그인">
		</form>
	</div></center>
	{% endif %}
	{% endblock %}
</html>
```

![image](https://user-images.githubusercontent.com/43658658/118491121-a13c7b80-b759-11eb-97a6-08eef5d00923.png)























