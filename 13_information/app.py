#Britni Canale
#SoftDev1 pd 6
#K13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")                         #home route
def hello_world():
    print(app)                          #info for debugging/informational purposes
    return render_template("form.html") #renders template for form, which has fields for names and submit button


@app.route("/auth")
@app.route("/auth", methods=["POST"])                     #route for echo
def authenticate():                     #enders echo template, uses request to get info from forms and request type, which is put into echo temp
    print(app)                          #info for debugging/informational purposes
    print(request)
    print(request.args)
    return render_template("echo.html", req = request.method, first = request.args["fname"], last = request.args["lname"]) 


if __name__ == "__main__":              #runs app
    app.debug = True
    app.run()
