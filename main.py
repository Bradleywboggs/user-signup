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

    if username == '':
        username_error = "This field is required"
        username = ''
    elif len(username) < 4:
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
    
    if not username_error:
        return redirect(f"/welcome?username={username}")
    else:
        return render_template("signup_form.html", username_error=username_error, 
        password_error=password_error, email_error=email_error, username=username,
        password='', verifypw='', email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return f"<h2>Welcome, {username}!<h2>"

app.run()