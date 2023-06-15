from app import app, base_url
import requests
from flask import render_template

@app.route('/delay3')
def delay3():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "exposureDelay": 3
                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('image_settings.html', response = response.text, title='self timer set to 3')

@app.route('/delay5')
def delay5():
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "exposureDelay": 5
                   }
               }}
    # response = create_response(payload)
    response = requests.post(base_url + 'commands/execute', json=payload)
    return render_template('image_settings.html', response = response.text, title='self timer set to 5')