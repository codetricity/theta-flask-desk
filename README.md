# Python Demonstration for THETA

## packages

* requests - for http requests to THETA
* flask - backend web framework

## for desktop

* [flaskwebgui](https://github.com/ClimenteA/flaskwebgui/tree/master)

## build

### windows

```text
pyinstaller -F --add-data "templates;templates" --add-data "static;static"  --icon=assets/logo.ico app.py
```

### linux

```text
pyinstaller -w -F  --add-data "templates:templates" --add-data "static:static" app.py
```

* no icon support

## application responsiveness

* Using [waitress](https://pypi.org/project/waitress/)
* example [FlaskUI setuo](https://github.com/ClimenteA/flaskwebgui/blob/master/examples/flask-desktop/main.py)

## Windows Tips

* [pipenv shell and PowerShell configuration](https://github.com/pypa/pipenv/issues/4264#issuecomment-845445399)
