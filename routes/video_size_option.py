from app import app, base_url
import requests
from flask import render_template


@app.route("/set8k10")
def set_8k_10():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 7680,
                    "height": 3840,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 10,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 8K 10fps",
        active_nav="set8k10"
    )


@app.route("/set8k5")
def set_8k_5():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 7680,
                    "height": 3840,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 5,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 8K 5fps",
        active_nav="set8k5"
    )


@app.route("/set8k2")
def set_8k_2():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 7680,
                    "height": 3840,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 2,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 8K 2fps",
        active_nav="set8k2"
    )

@app.route("/set57k2")
def set_57k_2():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 5760,
                    "height": 2880,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 2,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 5.7K 2fps",
        active_nav="set57k2"
    )


@app.route("/set57k5")
def set_57k_5():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 5760,
                    "height": 2880,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 5,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 5.7K 5fps",
        active_nav="set57k5"
    )


@app.route("/set57k10")
def set_57k_10():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 5760,
                    "height": 2880,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 10,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 5.7K 10fps",
        active_nav="set57k10"
    )


@app.route("/set57k30")
def set_57k_30():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 5760,
                    "height": 2880,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 30,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 5.7K 30fps",
        active_nav="set57k30"
    )


@app.route("/setmax7200")
def set_max7200():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_maxRecordableTime": 7200}},
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html",
        response=response.text,
        title="options setting max recordable time to 2 hrs",
        active_nav="setmax7200"
    )


@app.route("/setmax1500")
def set_max1500():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_maxRecordableTime": 1500}},
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html",
        response=response.text,
        title="options setting max recordable time to 25 mins",
        active_nav="setmax1500"
    )


@app.route("/setmax300")
def set_max300():
    payload = {
        "name": "camera.setOptions",
        "parameters": {"options": {"_maxRecordableTime": 300}},
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html",
        response=response.text,
        title="options setting max recordable time to 5 mins",
        active_nav="setmax300"
    )


@app.route("/set4k30")
def set_4k_30():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 3840,
                    "height": 1920,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 30,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 4K 30fps",
        active_nav="set4k30"
    )


@app.route("/set4k60")
def set_4k_60():
    payload = {
        "name": "camera.setOptions",
        "parameters": {
            "options": {
                "fileFormat": {
                    "type": "mp4",
                    "width": 3840,
                    "height": 1920,
                    "_codec": "H.264/MPEG-4 AVC",
                    "_frameRate": 60,
                }
            }
        },
    }
    response = requests.post(base_url + "commands/execute", json=payload)
    return render_template(
        "video_size.html", response=response.text, title="options setting to 4K 60fps",
        active_nav="set4k60"
    )
