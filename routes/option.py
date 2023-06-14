from app import app, base_url
import requests, json
from flask import render_template, request


@app.route('/set8k10')
def set_8k_10():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 7680,"height": 3840, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 10}
                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('response.html', response = response.text, title='options setting to 8K 10fps')