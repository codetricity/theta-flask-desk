from app import app, base_url
import requests
import json
from flask import render_template, jsonify

def create_response(protocol, name):
    if protocol == 'get':
        response = requests.get(base_url + name)
    elif protocol == 'post':
        response = requests.post(base_url + name)
    output = json.dumps(response.json(), indent=2)
    return render_template('response.html', response = output)

@app.route('/info')
def info():
    try:
        response = requests.get(base_url + 'info')
        return render_template('response.html', response = response.text)
    except:
        return render_template('response.html', response = 'error.  please true again')

@app.route('/state')
def state():
    try: 
        response = requests.post(base_url + 'state')
        return render_template('response.html', response = response.text)
    except:
        return render_template('response.html', response = 'error.  please true again')    