from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime


# csrf로 보호된, 빈 문자열인지 검사하는 문자열 필드의 content를 담은 Form 생성
class TextForm(FlaskForm):
    content = StringField('내용', validators=[DataRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
# mongoDB에 연결
connection = MongoClient('localhost', 27017)  # ip, port
# mongoDB에 접근, 변수.DB이름
db = connection.project
# Collection에 접근
todos = db.todo


# Error Process
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not.html'), 404


# home
@app.route("/")
@app.route("/about")
def home_page():
    return render_template('about.html')


# All list page
@app.route("/all")
def all_page():
    stat = "All list"
    # Collection(todos)의 모든 Document 들을 최근 날짜 순으로 정렬해서 todolist 로 만든다.
    todolist = todos.find().sort('date', -1)
    form = TextForm()
    return render_template('index.html', todos=todolist, stat=stat, form=form)


# Active item list
@app.route("/active")
def active_page():
    stat = "Active list"
    # Collection(todos) 중에서 {done:no} 인 Document 들을 최근 날짜 순으로 정렬해서 todolist 로 만든다.
    todolist = todos.find({"done": "no"}).sort('date, -1')
    form = TextForm()
    return render_template('index.html', todos=todolist, stat=stat, form=form)


# Completed item list
@app.route("/completed")
def complete_page():
    stat = "Completed list"
    # Collection(todos) 중에서 {done:yes} 인 Document 들을 최근 날짜 순으로 정렬해서 todolist 로 만든다.
    todolist = todos.find({"done": "yes"}).sort('date', -1)
    form = TextForm()
    return render_template('index.html', todos=todolist, stat=stat, form=form)


# Update memo
@app.route("/update")
def update_page():
    id = request.values.get("_id")
    task = todos.find({"_id": ObjectId(id)})[0]
    form = TextForm()
    return render_template('update.html', task=task, form=form)


# New memo
@app.route("/action", methods=['GET', 'POST'])
def action_add():
    form = TextForm()
    if form.validate_on_submit():
        contents = request.form['content']  # 내용 : 해야 할 내용
        date = datetime.today()  # 오늘 날짜
        primary = request.values.get('primary')  # 중요도 : High, Medium, Low
        # 초기 done 값은 할 일을 하지 않았으므로 no
        # document 형식 : {내용, 오늘 날짜, 중요도, done}
        todos.insert_one({"contents": contents, "date": date, "primary": primary, "done": "no"})
        return """<script>
            window.location = document.referrer;
            </script>"""  # 현재의 페이지를 다시 띄운다.(새로고침 효과)


# Done memo change
@app.route("/done")
def done_add():
    # URL로 보내져오는 _id 정보(./done?_id=' ')
    id = request.values.get("_id")
    # _id가 id인 Document 를 task 에 넣는다.
    task = todos.find({"_id": ObjectId(id)})
    # task = [{    }] 형태이다.
    if task[0]["done"] == "yes":  # {done: yes}일 경우 {done: no}로 value를 변경한다.
        todos.update_one({"_id": ObjectId(id)}, {"$set": {"done": "no"}})
    else:
        todos.update_one({"_id": ObjectId(id)}, {"$set": {"done": "yes"}})
    return """<script>
        window.location = document.referrer;
        </script>"""


# Delete memo
@app.route("/delete")
def action_delete():
    id = request.values.get("_id")
    todos.delete_one({"_id": ObjectId(id)})
    return """<script>
        window.location = document.referrer;
        </script>"""


# Done memo update
@app.route("/action2", methods=['GET', 'POST'])
def done_update():
    if request.method == 'POST':
        id = request.values.get('_id')
        contents = request.form['content']
        primary = request.values.get('primary')
        todos.update_one({"_id": ObjectId(id)}, {'$set': {'contents': contents, 'primary': primary}})
        # url_for('함수')
        return redirect(url_for('all_page'))  # 모든 항목 페이지로 이동한다.
    else:
        return render_template('page_not.html')


if __name__ == "__main__":
    app.run()
