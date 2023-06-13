from flask import Flask
from flaskwebgui import FlaskUI

dev_mode = False
app = Flask("__main__")
# base_url = "https://fake-theta-alpha.vercel.app/osc/"
base_url = "http://192.168.1.1/osc/"

from routes.page import *
from routes.protocol import *
from routes.command import *


if __name__ == "__main__":
    if dev_mode:
        app.run(debug=True)
    else:
        ui = FlaskUI(app=app, server="flask", width=800, height=600)
        ui.run()