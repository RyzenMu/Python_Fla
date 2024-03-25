from flask import Blueprint , render_template, request, flash

auth = Blueprint('auth', __name__) 

@auth.route("/login", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", bool1=7)

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 2 characters', category='error')
        elif password1 != password2 :
            flash('password not matching', category='error')
        elif len(password1) < 7:
            flash('lenth of password is too short', category='error')
        else:
            # add user to database
            flash('account activated', category='success')
    return render_template("sign_up.html")