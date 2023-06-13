from flask import Flask
from flaskwebgui import FlaskUI
from waitress import serve

dev_mode = False
app = Flask("__main__")
# base_url = "https://fake-theta-alpha.vercel.app/osc/"
base_url = "http://192.168.1.1/osc/"

from routes.page import *
from routes.protocol import *
from routes.command import *

def start_flask(**server_kwargs):
    app = server_kwargs.pop("app", None)
    server_kwargs.pop("debug", None)

    try:
        import waitress

        waitress.serve(app, **server_kwargs)
    except:
        app.run(**server_kwargs)



if __name__ == "__main__":
    if dev_mode:
        app.run(debug=True)
        # print('starting on http://localhost:5000')
        # serve(app, host='0.0.0.0', port=5000)
    else:
        # ui = FlaskUI(app=app, server="flask", width=800, height=600)
        # ui.run()
        # serve(ui, host='0.0.0.0', port=13195)
        FlaskUI(
            server=start_flask,
            server_kwargs={
                "app": app,
                "port": 3000,
                "threaded": True,
            },
            width=800,
            height=600,
        ).run()
