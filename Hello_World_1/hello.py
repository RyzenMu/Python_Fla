from flask import Flask

app = Flask(__name__)

@app.route("/")
def fun():
    return "<h1> Flask is Working</h1>"


