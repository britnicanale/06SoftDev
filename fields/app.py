#Britni Canale
#SoftDev1 pd 6
#K -- 
#

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(app)
    return render_template("temp.html")


@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "Waaaa hooo HAAAH"


if __name__ == "__main__":
    app.debug = True
    app.run()
