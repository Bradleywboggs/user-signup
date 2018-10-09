from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def signup():
    return render_template("signup_form.html")

@app.route("/", methods=['POST'])
def validate_signup():
    username = request.form["username"]
    password = request.form["pw"]
    verifypw = request.form["verifypw"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    email_error = ''

#validate username
    if username == '':
        username_error = "This field is required"
        username = ''
    elif len(username) < 3:
        username_error = "Username is not valid"
    elif len(username) > 20:
        username_error = "Username is not valid"
        username = ''
    elif username[0] == " ":
        username_error = "Username is not valid"
        username = ''
    else:
        username = username
        username_error = ''
    
# validate Password
    if password == '':
        password_error = "This field is required"
        password = ''
        verifypw = ''
    elif len(password) < 3:
        username = username
        password_error = "Password is not valid"
        password = ''
        verifypw = ''
    elif len(password) > 20:
        username = username
        password_error = "Password is not valid"
        password = ''
        verifypw = ''
    elif password != verifypw:
        username = username
        password_error = "Passwords do not match"
        password = ''
        verifypw = ''
    else:
        username = username
        password = password
        verifypw = verifypw

    if not username_error and not password_error:
        return redirect(f"/welcome?username={username}")
    #render the page again with error descriptions
    else:
        return render_template("signup_form.html", username_error=username_error, 
        password_error=password_error, email_error=email_error, username=username,
        password='', verifypw='', email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)

app.run()