from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='THETA Desk', heading = 'RICOH THETA Tester')

@app.route('/video_size')
def video_size():
    return render_template('video_size.html', title='video size format')

@app.route('/image_settings')
def image_settings():
    return render_template('image_settings.html', title='image settings')