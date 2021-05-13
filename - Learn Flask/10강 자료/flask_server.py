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
	return render_template('filedown.html', files=files)


# 파일 다운로드 처리
@app.route('/fileDown', methods=['GET', 'POST'])
def down_file():
	if request.method == 'POST':
		path = "./uploads/"
		return send_file(path + request.form['file'],
				attachment_filename=request.form['file'],
				as_attachment=True)


# 서버 실행
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
