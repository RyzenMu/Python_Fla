from flask import Flask

app = Flask(__name__)

@app.route("/")
def fun():
    return '''<h1>Good Evening All</h1>
            <p>I Am a agent</p>
            <hr>
            <h2> This is Heading 2 </h2>
            <hr>
            <h3>Super bro</h3>
            '''