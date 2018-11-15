#Britni Canale
#SoftDev1 pd6
#K25
#2018-11-13

from flask import Flask, render_template
import json, urllib


app = Flask(__name__)

@app.route("/")
def hello():
    APIKEY = "xaiLZ92GWmDBC3zKToFvpvz6rfrR8MeS"

    req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer xaiLZ92GWmDBC3zKToFvpvz6rfrR8MeS')
    response = urllib.request.urlopen(req)
    print(response)
    return render_template("index.html")

if __name__== "__main__":
    app.debug = True
    app.run()
