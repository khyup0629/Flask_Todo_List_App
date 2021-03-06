# Main Project 이론 정리

+ [html 태그 정리](#html-태그-정리)
+ [flask_wtf](#flask_wtf)
+ [MongoDB](#MongoDB)

# html 태그 정리

> <h3>base.html

+ meta name="viewport" content="width=device-width, initial-scale=1.0" : 웹 프레임의 크기에 맞춰서 페이지의 크기가 변경되도록 하는 기능
+ i class : 아이콘 삽입, **Bootstrap 기능**
	+ 일반적으로 HTML에서는 이태릭체나 다른 텍스트 서식으로 변경하기 위해 사용한다.
+ div : Division의 약자로, 레이아웃을 나누는데 주로 쓰인다.
	+ 가상의 레이아웃을 설계하는데 쓰이며, 주로 CSS와 연동하여 쓰인다.
+ block content, endblock : 'base.html'에서 다른 html 문서의 내용이 들어갈 부분에 block content~endblock을 써준 뒤 다른 html 문서의 상단에 extends "base.html"을 통해 확장하고, block content와 endblock 사이에 들어갈 내용을 입력해준다. 
+ extends "base.html" : 다른 html 문서에서 작성한 내용이 base.html 문서에 포함된다. 부모 템플릿을 불러온다고 이해.
+ include "nav.html" : nav.html 문서가 현재 html 문서에 포함된다. 자식 템플릿을 불러온다고 이해. 

> <h3>nav.html

+ button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#myNavbar" : data-target의 내용을 숨기는 버튼을 생성한다.
	+ data-toggle="collapse" : 내용을 숨기는 기능, **Bootstrap 기능**
+ span : div와 비슷하게 CSS와 함께 쓰인다. div 태그와 차이점은 block으로 나누는 것이 아닌 inline으로 나눈다는 것이다. 즉, div는 줄 바꿈이 되지만, span은 줄 바꿈이 안된다. 

+ nav : 다른 페이지 또는 현재 페이지의 다른 부분과 연결되는 네비게이션 링크(navigation links)들의 집합을 정의할 때 사용한다.
	+ 일반적인 예로는 메뉴, 목차, 인덱스 등이 있다.
+ a : 문자열에 링크(href)를 걸 수 있다.
+ li : ol 또는 ul 속에 속해서 리스트를 열거할 때 사용한다.
	+ ol : 순서가 있는 리스트
	+ ul : 순서가 없는 리스트

> <h3>footer.html

+ footer : 문서나 특정 섹션(section)의 푸터(footer)를 정의할 때 사용한다.
+ 푸터(footer)는 보통 footer 요소가 포함되어 있는 문서나 섹션에 대한 아래와 같은 정보를 포함합니다.
	- 저자(author) 정보
	- 저작권 정보
	- 연락처
	- 사이트맵(sitemap)
	- 페이지 맨 위로 되돌아갈 수 있는 Top 버튼
	- 연관 페이지 등

> <h3>index.html

+ select, option : 옵션 메뉴를 제공하는 드롭다운 리스트(drop-down list)를 정의할 때 사용.
	+ 내부의 option 요소는 드롭다운 리스트(drop-down list)에서 사용되는 각각의 옵션을 정의한다.
	+ 이러한 select 요소는 사용자로부터 입력을 받기 위한 폼(form)에 사용될 수 있습니다.

> <h3>list.html

+ table : 데이터를 포함하는 셀(cell)들의 행과 열로 구성된 2차원 테이블을 정의할 때 사용한다.
	+ tr : 테이블의 각 행(row)
	+ thead : table의 head(열의 최상단) 부분
		+ th : 각 열의 제목
	+ tbody : table의 body(열의 최상단을 제외한 나머지) 부분
		+ td : 하나의 테이블 셀(cell)

+ 알림창(modal)
	+ div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"
	+ tabindex="-1" : 해당 작업이 끝나기 전까지 모든 link들의 기능을 비활성화한다.
	+ modal 관련 정보(Bootstrap에서 사용하는 형식)

	=> https://getbootstrap.com/docs/4.0/components/modal/#accessibility

# flask_wtf

+ flask_wtf 는 플라스크 프레임 워크의 form 검증 모듈로, 쉽게 form을 생성 할 수 있으며, json 데이터 상호 작용을 위한 검증 도구로도 사용할 수 있다.

## 설치

```
pip install Flask-WTF
```

+ **flask_wtf, wtforms, wtforms.validators 모듈**이 한 번에 설치된다.

## flask_wtf 필드 정의

+ flask_wtf는 **wtforms 모듈**의 필드 모델을 사용한다.
+ core와 simple로 구분된다.
	+ core : 일반적으로 사용 되는 필드를 정의.
	+ simple : core 모듈을 기반으로 일부 필드를 확장. 

``` python
# core.py
__all__ = (
    'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
    'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
    'SelectMultipleField', 'StringField',
)

BooleanField ： True or False
StringField  ： 문자열
DecimalField ： 소수점 텍스트 필드 ex)‘1.23’
DateField    : 날짜 필드,형식：'%Y-%m-%d'
DateTimeField: 날짜 필드,형식：'%Y-%m-%d %H:%M:%S'
FloatField   : 부동소수점 유형
IntegerField ： 정수
SelectMultipleField：체크박스
RadioField   ： 라디오박스

# simple.py
TextAreaField : 텍스트 필드(여러줄 입력)
PasswordField ： 패스워드(보여지지 않음)
FileField     ：파일을 업로드(파일 확인은 하지 않으며, 확인은 수동으로 처리해야함)
HiddenField：숨겨진 필드
SubmitField：제출 필드
```

+ flask_wtf는 wtforms.validators 모듈을 이용해 선택적 필드 유효성 검사를 진행한다.

``` python
__all__ = (
    'DataRequired', 'data_required', 'Email', 'email', 'EqualTo', 'equal_to',
    'IPAddress', 'ip_address', 'InputRequired', 'input_required', 'Length',
    'length', 'NumberRange', 'number_range', 'Optional', 'optional',
    'Required', 'required', 'Regexp', 'regexp', 'URL', 'url', 'AnyOf',
    'any_of', 'NoneOf', 'none_of', 'MacAddress', 'mac_address', 'UUID'
)

# 대문자/소문자 모드
DataRequired/data_required : 데이터가 실제로 존재하는지 확인. 즉, 비어있지 않은지, 공백이 아닌 문자열인지 확인. 그렇지 않으면 StopValidation 오류가 트리거가된다.
InputRequired/input_required ：DataRequired와의 차이점은 빈 문자열 일 수 있다는 것.
Required/required : data_required의 별칭
Email/email ：가장 기본적인 이메일 형식
EqualTo/equal_to : 비밀번호와 비밀번호 확인과 같은 두 필드의 값을 비교. 두 필드가 같지 않으면 오류 발생. equal_to(field, message), 다른 필드의 이름을 입력해야함.
IPAddress/ip_address : IP 주소인지 확인(기본적으로 IPV4 주소가 확인됨)
MacAddress/mac_address : Mac 형식을 준수하는지 확인
UUID：uuid 형식인지 여부.
URL/url : URL 형식을 준수하는지 확인
Regexp/regexp : 제공된 정규식을 사용하여 필드 유효성 검사, Regexp (r "")
Length/length : 필드 값의 길이를 설정, Length (min, max);
NumberRange/number_range : 숫자 필드의 값 범위를 설정(부동 소수점 숫자 및 소수일 수도 있음) NumberRange(min, max)
Optional/optional :
NoneOf/none_of :
Anyof/any_of :
```

## FlaskForm

+ flask_wtf는 Form에 필요한 모든 속성과 메서드를 제공하는 Form 객체의 하위 클래스 **FlaskForm**을 사용할 것을 권장한다. 

``` python
class FlaskForm(Form):
    class Meta(DefaultMeta):
        def wrap_formdata(self, form, formdata):
            pass

    def __init__(self, formdata=_Auto, **kwargs):
        csrf_enabled = kwargs.pop('csrf_enabled', None)
        pass
    def is_submitted(self):
        pass
    def validate_on_submit(self):
        pass
    def hidden_tag(self, *fields):
        pass
    def validate(self):
        pass
```

+ FlaskForm은 내부에 Meta 클래스를 정의하여 **csrf로 보호**되는 일부 메서드를 추가하므로 양식을 만들 때 Form 대신 FlaskForm을 가져와야한다.
	+ is_submitted : 활성 요청 요청이 있는지 확인한다.
	+ validate_on_submit : is_submitted 및 validate 메소드를 호출하고 bool 값을 반환하여 양식이 제출되었는지 여부를 확인한다.
	+ validate : 필드 수준 유효성 검사. 각 필드에는 유효성 검사 메서드가 있다. FlaskForm은 모든 필드에 대한 유효성 검사 메서드를 호출하기 위해 validate를 호출한다. 모든 유효성 검사가 통과되면 True를 반환하고 그렇지 않으면 예외가 발생한다.
	+ hidden_tag : 양식의 숨겨진 필드를 가져온다.
	+ wrap_formdata : 요청에서 양식 가져오기, 이 함수는 요청에서 양식을 가져 오기 위해 양식 객체가 초기화 될 때마다 실행된다.
+ 중요한 속성
	+ form.data     :필드 이름과 값의 사전
	+ form.errors   ：유효성 검사에 실패한 정보 사전(validate_on_submit 메서드를 호출 한 후 유효)
	+ form.name.data：필드 이름의 값
	+ form.name.type：필드 이름 유형

## form = Form()

+ flask_wtf 의 FlaskForm 으로 만들었다면, FlaskForm은 요청 객체에서 request.form 및 request.get_json() 메서드를 자동으로 호출하여 데이터를 수신한다.

## csrf_token

+ flask_wtf의 FlaskForm 을 만들었다면 자동으로 csrf 보호가 활성화 되어있다.
+ 그러므로 html 안에는 {{ form.csrf_token }} 을 추가해야 한다.
+ csrf_token 를 비활성화 하기 위해서는 아래와 같은 방법을 사용하면 된다.

``` python
# form을 받을 때 비활성화
form = Form(csrf_enabled=False)

# config.py 안에 아래와 같은 코드 삽입
WTF_CSRF_ENABLED = False
```

---
출처
+ https://velog.io/@insutance/FlaskWTF

---
# MongoDB

## 설치

+ 아래의 링크로 들어가 MongoDB의 가장 최신 버전을 windows, msi 버전으로 다운 받는다.

=> https://www.mongodb.com/try/download/community

+ 그냥 pymongo만 다운 받게 되면 서버가 mongoDB에 접근하지 못해 [win 10061] 에러가 발생하게 된다.

```
pip install pymongo
```

+ 파이썬 IDE의 터미널을 통해 파이썬에서 사용할 수 있는 mongoDB 모듈인 pymongo를 설치해준다.

## DB연결 - MongoClient

+ MongoDB에 연결하는 방법은 두 가지가 있다.
	+ 첫 번째 방법은 실행 중인 MongoDB 서버의 URI를 MongoClient의 파라미터로 입력하는 것이고,
	+ 두 번째 방법은 DB 서버의 IP와 포트 번호 두 가지 값을 각각 파라미터로 입력하는 것이다. 

``` python
from pymongo import MongoClient

# 방법1 - URI
# mongodb_URI = "mongodb://localhost:27017/"
# client = MongoClient(mongodb_URI)

# 방법2 - IP, PORT
client = MongoClient('localhost', 27017)

print(client.list_database_names())
```

[출력]

``` python
['admin', 'config', 'local']
```

## DB 접근

+ DB에 접근하는 방법도 두 가지가 있다.
	+ 하나는 메서드 형태로 . 뒤에 db명을 입력하는 것이고,
	+ 다른 하나는 str 형식으로 대괄호 안에 db명을 입력하는 것이다.

``` python
# DB 접근
# 방법1
# db = client.mydb

# 방법2
db = client['mydb']
```

## Collection 접근

+ Collection 접근 방법도 DB 접근 방법과 유사하다.

``` python
# Collection 접근
# 방법1
# collection = db.myCol
# 방법2
collection = db['myCol']
```

## Documents

> <h3>Document 생성

+ MongoDB는 Data를 JSON 스타일의 Document로 저장한다.
+ JSON과 유사한 Python Dictionary 데이터를 MongoDB Collection에 Document로 저장할 수 있다.

``` python
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
print(post)
```

[출력]

``` python
{'author': 'Mike',
 'text': 'My first blog post!',
 'tags': ['mongodb', 'python', 'pymongo'],
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217943)}
```

> <h3>Collection 접근 및 Document 추가

+ posts라는 Collection에 접근하여 위에서 만든 Dictionary 데이터를 추가한다. 
+ 이 때, 데이터 추가 후 자동으로 생성되는 _id 값을 post_id에 저장한다.
+ (document에는 별도로 지정해주지 않아도 생성하면 고유 _id가 문자열 형태로 생성된다.)

[Collection 접근 - 'posts' Collection]

``` python
posts = db.posts

# Document 추가 - insert_one() 메서드 이용
post_id = posts.insert_one(post).inserted_id
print(post_id)
```

[출력]

``` python
5fa2a1d5a7bd62cd633fdb5b
```

[Collection 리스트 조회]

``` python
db.list_collection_names()
```

[출력]

```
['posts']
```

> <h3> 단일 Document 조회 - find_one() 메서드 이용

[Collection 내 단일 Document 조회]

``` python
import pprint
pprint.pprint(posts.find_one())
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
```

[쿼리를 통한 Documents 조회]

``` python
pprint.pprint(posts.find_one({"author": "Mike"}))
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
```

[_id를 통한 Documents 조회 - _id는 binary json 타입으로 조회해야 함]

``` python
# _id를 통한 Documents 조회 - _id는 binary json 타입으로 조회해야 함
pprint.pprint(posts.find_one({"_id": post_id}))
print(type(post_id))
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
<class 'bson.objectid.ObjectId'>
```

[_id 값이 str인 경우 조회 안 됨.]

``` python
# _id 값이 str인 경우 조회 안 됨.
post_id_as_str = str(post_id)
pprint.pprint(posts.find_one({"_id": post_id_as_str}))
```

[출력]

```
None
```

[_id 값이 str인 경우 bson(binary json) 변환 후 조회]

``` python
# _id 값이 str인 경우 bson(binary json) 변환 후 조회
from bson.objectid import ObjectId

bson_id = ObjectId(post_id_as_str)
pprint.pprint(posts.find_one({"_id": bson_id}))
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
```

> <h3>여러 Documents 추가 - insert_many() 메서드 이용

``` python
# Bulk Insert

new_posts = [
    
    {
     "author": "Mike",
     "text": "Another post!",
     "tags": ["bulk", "insert"],
     "date": datetime.datetime(2009, 11, 12, 11, 14)
    },
     
    {
     "author": "Eliot",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
    
]

result = posts.insert_many(new_posts)
result.inserted_ids
```

[출력]

```
[ObjectId('5fa2a1eda7bd62cd633fdb5c'), ObjectId('5fa2a1eda7bd62cd633fdb5d')]
```

> <h3>여러 Documents 조회 - find() 메서드 이용

[Collection 내 모든 Documents 조회]

``` python
# Collection 내 모든 Documents 조회
for post in posts.find():
    pprint.pprint(post)
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
{'_id': ObjectId('5fa2a1eda7bd62cd633fdb5c'),
 'author': 'Mike',
 'date': datetime.datetime(2009, 11, 12, 11, 14),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
{'_id': ObjectId('5fa2a1eda7bd62cd633fdb5d'),
 'author': 'Eliot',
 'date': datetime.datetime(2009, 11, 10, 10, 45),
 'text': 'and pretty easy too!',
 'title': 'MongoDB is fun'}
```

[쿼리를 통한 Documents 조회]

``` python
# 쿼리를 통한 Documents 조회
for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)
```

[출력]

```
{'_id': ObjectId('5fa2a1d5a7bd62cd633fdb5b'),
 'author': 'Mike',
 'date': datetime.datetime(2020, 11, 4, 12, 42, 56, 217000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
{'_id': ObjectId('5fa2a1eda7bd62cd633fdb5c'),
 'author': 'Mike',
 'date': datetime.datetime(2009, 11, 12, 11, 14),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
```

> <h3>카운팅

[Collection 내 Document 수 조회]

``` python
# 컬렉션 내 Document 수 조회
posts.count_documents({})
```

[출력]

```
3
```

[쿼리를 통한 Document 수 조회]

``` python
# 쿼리를 통한 Document 수 조회
posts.count_documents({"author": "Mike"})
```

[출력]

```
2
```

> <h3>범위 쿼리

[범위 쿼리]

``` python
# 범위 쿼리
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)
```

[출력]

```
{'_id': ObjectId('5fa2a1eda7bd62cd633fdb5d'),
 'author': 'Eliot',
 'date': datetime.datetime(2009, 11, 10, 10, 45),
 'text': 'and pretty easy too!',
 'title': 'MongoDB is fun'}
{'_id': ObjectId('5fa2a1eda7bd62cd633fdb5c'),
 'author': 'Mike',
 'date': datetime.datetime(2009, 11, 12, 11, 14),
 'tags': ['bulk', 'insert'],
 'text': 'Another post!'}
```

> <h3>인덱싱

[두 개의 인덱스 확인]

``` python
import pymongo
# Indexing
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)

# 두 개의 인덱스 확인
sorted(list(db.profiles.index_information()))
```

[출력]

```
['_id_', 'user_id_1']
```

[이미 Collection에 있는 user_id인지]

``` python
# 유저 정보 관련 Document 생성
user_profiles = [
    
    {"user_id": 211, "name": "Luke"},
    {"user_id": 212, "name": "Ziltoid"}
    
]

# Document 추가
result = db.profiles.insert_many(user_profiles)

# 이미 컬렉션에 있는 user_id이면 추가 안 됨
new_profile = {"user_id": 213, "name": "Drew"}
duplicate_profile = {"user_id": 212, "name": "Tommy"}

# user_id 신규 이므로 정상 추가 됨
result = db.profiles.insert_one(new_profile)

try:
    # user_id 기존에 있으므로 추가 안 됨
    result = db.profiles.insert_one(duplicate_profile)
except:
    print("Error")
```

[출력]

```
Error
```

[Collection 내의 Document 모두 출력]

``` python
for doc in db.profiles.find():
    pprint.pprint(doc)
```

[출력]

```
{'_id': ObjectId('5fa2a1f4a7bd62cd633fdb5e'), 'name': 'Luke', 'user_id': 211}
{'_id': ObjectId('5fa2a1f4a7bd62cd633fdb5f'), 'name': 'Ziltoid', 'user_id': 212}
{'_id': ObjectId('5fa2a1f5a7bd62cd633fdb60'), 'name': 'Drew', 'user_id': 213}
```

> <h3>Document의 value 변경 - update_one() 메서드, bson 모듈의 ObjectId() 이용
	
+ Document 를 생성하면 자동으로 고유 _id가 같이 생성된다.
+ {"_id":문자열} 형태로 Document 의 원소로 들어간다.
+ ObjectId()를 통해 문자열 value를 읽을 수 있으므로 _id 값을 읽을 수 있다.

+ **collection.update_one({"_id": ObjectId(_id)}, {"$set": {"key": "value"}})**

``` python
# _id가 _id인 Document 를 task 에 넣는다.
task = todos.find({"_id": ObjectId(_id)})
# task = [{    }] 형태이다.
if task[0]["done"] == "yes":  # {done: yes}일 경우 {done: no}로 value를 변경한다.
	todos.update_one({"_id": ObjectId(id)}, {"$set": {"done": "no"}})
else:  # {done: no}일 경우 {done: yes}로 value를 변경한다.
	todos.update_one({"_id": ObjectId(id)}, {"$set": {"done": "yes"}})
```

> <h3>Document의 key:value 삭제 - delete_one() 메서드, bson 모듈의 ObjectId() 이용

+ Document의 고유 id를 이용해 원소를 삭제할 수 있다.

``` python
id = request.values.get("_id")
todos.delete_one({"_id": ObjectId(id)})
```

---
[참조]
+ https://getbootstrap.com/ (Bootstrap 활용법에 대한 정보)
+ http://tcpschool.com/ (HTML 태그 관련 정보)
+ https://wooiljeong.github.io/python/mongodb-01/
+ https://github.com/neltia/Flask-Todo-app

---
