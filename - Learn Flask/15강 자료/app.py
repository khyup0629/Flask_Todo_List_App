from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "khyup0629@gmail.com"  # 형식은 이메일@gmail.com
app.config['MAIL_PASSWORD'] = 'rlaguq09!@'  # 구글 계정 비밀번호 입력
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)  # 설정한 사항들을 메일 객체에 담는다.


def send_email(title, senders, receiver, content):
    msg = Message(title, sender=senders, recipients=receiver)
    msg.body = content
    mail.send(msg)


@app.route('/email', methods=['post', 'get'])
def email_test():
    if request.method == 'POST':
        title = request.form['email_title']
        senders = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = request.form['email_content']
        receiver = receiver.split(',')

        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()

        print(receiver)

        result = send_email(title, senders, receiver, content)

        if not result:
            return render_template('email.html', content="Email is sent")
        else:
            return render_template('email.html', content="Email is not sent")

    else:
        return render_template('email.html')


if __name__ == "__main__":
    app.secret_key = "123123123"
    app.run(debug=True)
