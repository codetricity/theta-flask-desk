from app import app, base_url
import requests
from flask import render_template

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
    return render_template('video_size.html', response = response.text, title='options setting to 8K 10fps')

@app.route('/set8k5')
def set_8k_5():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 7680,"height": 3840, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 5}
                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting to 8K 5fps')

@app.route('/set8k2')
def set_8k_2():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 7680,"height": 3840, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 2}
                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting to 8K 2fps')

@app.route('/set57k2')
def set_57k_2():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 5760,"height": 2880, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 2}

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting to 5.7K 2fps')

@app.route('/set57k5')
def set_57k_5():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 5760,"height": 2880, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 5}

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting to 5.7K 5fps')

@app.route('/set57k30')
def set_57k_30():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "fileFormat": {"type": "mp4","width": 5760,"height": 2880, "_codec": "H.264/MPEG-4 AVC", "_frameRate": 30}

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting to 5.7K 30fps')

@app.route('/setmax7200')
def set_max7200():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "_maxRecordableTime": 7200

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting max recordable time to 2 hrs')

@app.route('/setmax1500')
def set_max1500():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "_maxRecordableTime": 1500

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting max recordable time to 25 mins')

@app.route('/setmax300')
def set_max300():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "_maxRecordableTime": 300

                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('video_size.html', response = response.text, title='options setting max recordable time to 5 mins')
