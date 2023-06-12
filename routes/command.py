from app import app, base_url
import requests, json
from flask import render_template

def create_response(payload):
    response = requests.post(base_url + 'commands/execute', json=payload)
    output = json.dumps(response.json(), indent=2)
    return render_template('response.html', response = output)

@app.route('/take_picture')
def take_picture():
    payload = {"name": "camera.takePicture"}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('response.html', response = response.text)
