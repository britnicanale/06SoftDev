#Britni Canale
#SoftDev1 pd 6
#K -- 
#

from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("login.html")

@app.route("/welcome")
@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html", uname = request.args["uname"])

if __name__ == "__main__":
    app.debug = True
    app.run()
