from app import app, base_url
import requests, json
from flask import render_template
from .protocol import state

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

@app.route('/last_image')
def last_image():
    url = f"{base_url}commands/execute"
    command_string = "camera.listFiles"
    payload = {
                "name": command_string,
                "parameters": {
                    "fileType": "image",
                    "entryCount": 1,
                    "maxThumbSize": 0

                }}
    resp = requests.post(
                        url,
                        json=payload)

    data = resp.json()
    last_file_url = data["results"]["entries"][0]["fileUrl"]    
    return render_template('image.html', last_file_url = last_file_url)
