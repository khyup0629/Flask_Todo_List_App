+ [html 용어 정리](#html-용어-정리)
+ [flask_wtf](#flask_wtf)

# html 용어 정리

> <h3>base.html

meta name="viewport" content="width=device-width, initial-scale=1.0"
i
div
% extends %
% include %
% block content %
% endblock %

> <h3>nav.html

button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#myNavbar"
span class="navbar-toggler-icon"

nav
a
ul, li

> <h3>footer.html

footer

> <h3>index.html

select, option

> <h3>list.html

tr
class
thead : table의 head 부분
tbody : table의 body 부분
td
th

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
