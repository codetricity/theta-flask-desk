from app import app, base_url
import requests, json
from flask import render_template, request


@app.route('/set_image')
def set_image():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "captureMode": "image"

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('index.html', response = response.text, title='options setting to set image')

@app.route('/set_video')
def set_video():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "captureMode": "video"

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('index.html', response = response.text, title='options setting to set video')