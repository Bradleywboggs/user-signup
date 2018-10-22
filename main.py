from flask import Flask, request, redirect, render_template
import re

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
    verifypw_error = ''
# Regex pattern checks for at alphanumeric characters - minumum 6, maximum 20
    un_pattern = re.compile(r"[\w]{6,20}")
    un_matched = un_pattern.match(username)
# Regex pattern checks for non-white space characters - minimum 8, maximum 20
    pw_pattern = re.compile(r"[^\s]{8,20}")
    pw_matched = pw_pattern.match(password)
# Regex pattern looks for alphanumeric characters - minimum 3, no max; "@" symbol, 
#at least one alphanumeric, ""."", at least 2 alphas(case insensitive)
    email_pattern = re.compile(r"[\w]{3,}[@][\w]+[.][a-zA-Z]{2,}")
    email_matched = email_pattern.match(email)

#validate username
    if username == '':
        username_error = "This field is required."
        username = ''
    elif not un_matched:
        username_error = "Username is not valid."
    else:
        username = username
        username_error = ''
    
# validate password
    if password == '':
        password_error = "This field is required."
        password = ''
        verifypw = ''      
    elif not pw_matched:
        password_error = "This password is not valid"
        password = ''
        verifypw = ''    
# verify both passwords match
    elif password != verifypw:
        verifypw_error = "Passwords do not match."
        password = ''
        verifypw = ''
    else:
        username = username
        password = password
        verifypw = verifypw
 
        
    
# validate email
    if email == '':
        email_error = ''
        email = email
    elif not email_matched:
        email_error = 'Email not valid'
        email = ''
    else:
        email_error = ''
        email = email

    if not username_error and not password_error and not email_error and not verifypw_error:
        return redirect(f"/welcome?username={username}")
    #render the page again with error descriptions
    else:
        return render_template("signup_form.html", username_error=username_error, 
        password_error=password_error, email_error=email_error, verifypw_error=verifypw_error, username=username,
        password='', verifypw='', email=email)


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)

app.run()