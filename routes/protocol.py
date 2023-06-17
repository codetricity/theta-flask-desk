from app import app, base_url
import requests
import json
from flask import render_template, jsonify


@app.route("/info")
def info():
    response = requests.get(base_url + "info")
    return render_template(
        "index.html", response=response.text, title="camera info", active_nav="info"
    )


@app.route("/state")
def state():
    response = requests.post(base_url + "state")
    return render_template(
        "index.html", response=response.text, title="camera state", active_nav="state"
    )
