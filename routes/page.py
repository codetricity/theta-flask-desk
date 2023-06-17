from app import app, base_url
from flask import render_template
import requests
from time import sleep


@app.route("/")
@app.route("/index")
def home():
    return render_template(
        "index.html",
        title="THETA Desk",
        heading="RICOH THETA Tester",
        active_nav="none",
    )


@app.route("/video_size")
def video_size():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"captureMode": "video"}},
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    sleep(0.75)
    return render_template("video_size.html", title="video size format")


@app.route("/image_settings")
def image_settings():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"captureMode": "image"}},
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    sleep(0.75)
    return render_template("image_settings.html", title="image settings")
