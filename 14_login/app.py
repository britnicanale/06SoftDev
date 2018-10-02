#Britni Canale
#SoftDev1 pd 6
#K -- 
#

from flask import Flask, render_template, session, request, url_for, redirect
import os

str = os.urandom(32)
app = Flask(__name__)

app.secret_key = str
session["bcanale"] = "hi"


@app.route("/")
def hello_world():
    if request.form["uname"] in session:
        return redirect(url_for("welcome"))
    return render_template("login.html")


@app.route("/welcome")
@app.route("/welcome", methods=["POST", "GET"])
def welcome():
    print(request.args)
    print(request.method)
    if request.form["uname"] in session and request.form["pword"] == session[request.form["uname"]]:
        return render_template("welcome.html", uname = request.form["uname"])

if __name__ == "__main__":
    app.debug = True
    app.run()
