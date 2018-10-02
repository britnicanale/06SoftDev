#Britni Canale & Kyle Tau
#SoftDev1 pd 6
#K14 -- Do I Know You?
#2018-10-01

from flask import Flask, render_template, session, request, url_for, redirect
import os

app = Flask(__name__)


app.secret_key = os.urandom(32)               #generates random 32-bit secret_key

    
uname = "tom"                                 #HARDCODED USERNAME AND PASSWORD       
pword = "jerry"


@app.route("/")                               #root route, redirects to welcome if logged in, loads login page if not
def login():
    if "username" not in session:
        return render_template("login.html")
    return redirect(url_for("welcome"))

@app.route("/welcome")
@app.route("/welcome", methods=["POST"])      #welcome route (if logged in only), only accepts POST requests
def welcome():
    un = request.form["uname"]                #gets login info from form
    pw = request.form["pword"]
    if un == uname and pw == pword:           #checks username and password, if correct adds to session and renders welcome page
        session["username"] = uname
        return render_template("welcome.html")
    return render_template("error.html")      #displays error messages if something went wrong, has button to go back to login page


@app.route("/logout")                         #route for logging out
def go():
    if 'username' in session:                 #ends session
        session.clear()
    return redirect(url_for("login"))         #redirects to login page after logout


if __name__ == "__main__":
    app.debug = True
    app.run()
