#Britni Canale
#SoftDev1 pd6
#K25
#2018-11-13

from flask import Flask, render_template, request, flash
import json, urllib
import os


app = Flask(__name__)


app.secret_key = os.urandom(32)


@app.route("/")
def hello():
    lat = 0
    long = 0
    if "lat" not in request.args or "long" not in request.args:
        flash("You must fill out all fields")
    elif request.args["lat"] == "" or abs(float(request.args["lat"])) > 90:
        flash("Invalid Latitude")
    elif request.args["long"] == "" or abs(float(request.args["long"])) > 180:
        flash("Invalid Longitude")
    else:
        lat = request.args["lat"]
        long = request.args["long"]
    url = "https://api.darksky.net/forecast/a8cad3df213e3cf847b714ab33140b16/"+str(lat)+","+str(long)
    req = urllib.request.urlopen(url)
    file = req.read()
    dict = json.loads(file)
    print(dict)
    print("TIMEZONE" +dict["timezone"])

    return render_template("index.html",
        timezone = dict["timezone"],
        summary = dict["currently"]["summary"],
        icon = dict["currently"]["icon"],
        temp = dict["currently"]["temperature"],
        precipProb=dict["currently"]["precipProbability"])



if __name__== "__main__":
    app.debug = True
    app.run()
