from app import app, base_url
import requests
from flask import render_template

@app.route("/set55")
def set_55():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "jpeg",
                    "width": 5504,
                    "height": 2752,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html", response=response.text, title="set image resolution to 5.5K",
        active_nav="set55"
    )

@app.route("/set11")
def set_11():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "jpeg",
                    "width": 11008,
                    "height": 5504,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html", response=response.text, title="set image resolution to 11K",
        active_nav="set11"
    )

@app.route("/nodelay")
def nodelay():
    payload = {
        "name": "camera._stopSelfTimer",
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="No delay",
        active_nav="nodelay",
    )

@app.route("/delay3")
def delay3():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureDelay": 3}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="self timer set to 3",
        active_nav="delay3",
    )


@app.route("/delay5")
def delay5():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureDelay": 5}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="self timer set to 5",
        active_nav="delay5",
    )

@app.route("/delay10")
def delay10():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureDelay": 10}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="self timer set to 10",
        active_nav="delay10",
    )

@app.route("/evneg20")
def evneg20():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureCompensation": -2.0}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="EV -2.0",
        active_nav="evneg20",
    )

@app.route("/ev0")
def ev0():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureCompensation": 0.0}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="EV 0.0",
        active_nav="ev0",
    )

@app.route("/ev20")
def ev20():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"exposureCompensation": 2.0}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="EV 2.0",
        active_nav="ev20",
    )

@app.route("/vol0")
def vol0():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_shutterVolume": 0}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="Shutter volume 0",
        active_nav="vol0",
    )

@app.route("/vol40")
def vol40():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_shutterVolume": 40}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="Shutter volume 40",
        active_nav="vol40",
    )

@app.route("/vol100")
def vol100():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_shutterVolume": 100}},
    }
    # response = create_response(payload)
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "image_settings.html",
        response=response.text,
        title="Shutter volume 100",
        active_nav="vol100",
    )

