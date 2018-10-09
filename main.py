from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def signup():
    return render_template("signup_form.html")

app.run()