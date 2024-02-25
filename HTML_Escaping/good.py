from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def fun(name):
    return f"Hello , {escape(name)}"