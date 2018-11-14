#smilesAndSilence -- Britni Canale && Thomas Lee
#SoftDev1 pd6
#K24 --  A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import json, urllib


app = Flask(__name__)


url = "https://api.getchute.com/v2"

@app.route("/")
def hello():

    url = "https://api.getchute.com/v2"

    request = urllib.request.urlopen(url)

    file = request.read()

    dict = json.loads(file)

    print(dict)

    return render_template("index.html")

if __name__== "__main__":
    app.debug = True
    app.run()
