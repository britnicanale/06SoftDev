#smilesAndSilence -- Britni Canale && Thomas Lee
#SoftDev1 pd6
#K24 --  A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import json, urllib


app = Flask(__name__)


url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"

@app.route("/")
def hello():

    url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"

    request = urllib.request.urlopen(url)

    file = request.read()

    dict = json.loads(file)

    return render_template("index.html", url = dict["url"], explanation = dict["explanation"])

if __name__== "__main__":
    app.debug = True
    app.run()
