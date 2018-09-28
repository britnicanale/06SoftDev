#Britni Canale
#SoftDev1 pd 6
#K13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(app)
    return render_template("form.html")


@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return render_template("echo.html", req = request.method, first = request.args["fname"], last = request.args["lname"])


if __name__ == "__main__":
    app.debug = True
    app.run()
