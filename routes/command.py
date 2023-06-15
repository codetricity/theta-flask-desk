from app import app, base_url
import requests, json
from flask import render_template, request
from .protocol import state

# def create_response(payload):
#     response = requests.post(base_url + 'commands/execute', json=payload)
#     output = json.dumps(response.json(), indent=2)
#     return render_template('response.html', response = output)

@app.route('/take_picture')
def take_picture():
    payload = {"name": "camera.takePicture"}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('index.html', response = response.text, title='taking picture')

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
    name = data["results"]["entries"][0]["name"]    
    return render_template('index.html', image_url = last_file_url, title= name + ' last image')

@app.route('/full_image')
def full_image():
    image_url = request.args.get('image_url')
    name = request.args.get('name')
    print(image_url, name)
    return render_template('image.html', image_url = image_url, title=name + ' image in camera')

@app.route('/ten_images')
def ten_images():
    url = f"{base_url}commands/execute"
    command_string = "camera.listFiles"
    payload = {
                "name": command_string,
                "parameters": {
                    "fileType": "image",
                    "entryCount": 10,
                    "maxThumbSize": 0

                }}
    resp = requests.post(
                        url,
                        json=payload)

    data = resp.json()
    entries = data["results"]["entries"]    
    return render_template('thumbs.html', entries = entries, title="Files on camera")

@app.route('/thirty_images')
def thirty_images():
    url = f"{base_url}commands/execute"
    command_string = "camera.listFiles"
    payload = {
                "name": command_string,
                "parameters": {
                    "fileType": "image",
                    "entryCount": 30,
                    "maxThumbSize": 0

                }}
    resp = requests.post(
                        url,
                        json=payload)

    data = resp.json()
    entries = data["results"]["entries"]    
    return render_template('thumbs.html', entries = entries, title="Files on camera")