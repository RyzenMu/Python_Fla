 
from flask import Blueprint , render_template

views = Blueprint('views', __name__)

# @views.route("/")
# def home():
#     return "<h1>TEST</h1>"

@views.route("/")
def home():
    return render_template("home.html", variable1="This is variable 1", user1="muruga")


