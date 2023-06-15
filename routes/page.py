from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='THETA Desk', heading = 'RICOH THETA Tester')

