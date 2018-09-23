'''Britni Canale
SoftDev1 pd6
K8 -- Fill Yer Flask
2018-09-19'''

import random
import csv

from flask import Flask, render_template

app = Flask(__name__)


occs = {}

def getOcc(filename):
    f = open(filename, 'r') #open csv                                                      
    lineSeparated = csv.reader(f) #separate by commas, but not those in quotes             
    for line in lineSeparated:
        if line[0] != 'Job Class': #control for leading line                               
            if line[0] != 'Total': #control for last line
                titleKey = line[0]
                print(titleKey)
                percentValue = float(line[1]) #save percent value as floating point        
                occs[titleKey] = percentValue

@app.route("/")
def hello_world():
    return "This is the home page"

@app.route("/my_foist_template")
def hello_temp():
    getOcc("static/occupations.csv")
    return render_template("temp.html", ttl = "Random Stuff", rand = random.choice(list(occs.keys())), dict = occs)#len = len(keys), k = keys, v = vals)


if __name__ == "__main__":
    app.debug = True
    app.run()
