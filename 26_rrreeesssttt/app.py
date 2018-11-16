#Britni Canale
#SoftDev1 pd 6
#K26 -- Getting More REST
#2018-11-15


from flask import Flask, render_template, session, request, url_for, redirect, flash
from urllib.request import urlopen, Request
import json, requests

app = Flask(__name__)

@app.route("/")
def hello():
    dog = "https://dog.ceo/api/breeds/image/random"
    req = urlopen(dog)
    dogdict = json.loads(req.read())
    dogpic = dogdict["message"]
    print(dogpic)
    breed = dogpic[30:dogpic.rindex("/")]
    print(breed)

    #url = 'http://api.repo.nypl.org/api/v1/items/search?q=cats&publicDomainOnly=true'



    dogfacts = 'http://api.repo.nypl.org/api/v1/items/search?q='+breed
    auth = 'Token token=ekujifnuvmrzwzuk'
    call = requests.get(dogfacts, headers={'Authorization': auth})

    #r = requests.get(dogfacts)
    #logger.info(type(r))
    #request =  Request(dogfacts, values.encode("utf-8"))
    #openrequest = urlopen(request)
    #readrequest = openrequest.read()
    #print(r.text)
    #factsdict = json.loads(r.text)
    #print(factsdict)
    return render_template("index.html", ttl = "DOGS AND STUFF", DOG = dogpic, breed = breed)

if __name__ == "__main__":
    app.debug = True
    app.run()
