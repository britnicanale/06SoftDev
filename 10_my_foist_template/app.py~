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
    f = open(filename, 'r')                                                      
    lineSeparated = csv.reader(f) 
    for line in lineSeparated:
        if line[0] == 'Job Class': #exception for first, doesn't store value as float, used for heading of table
            titleKey = line[0]
            val = line[1]
            occs[titleKey] = val
        if line[0] != 'Job Class':#includes total to be used for end of table
            titleKey = line[0]
            percentValue = float(line[1])
            occs[titleKey] = percentValue

@app.route("/")
def hello_world():
    return "This is the home page"

@app.route("/my_foist_template")
def hello_temp():
    getOcc("static/occupations.csv") #calls function that created dictionary out of the csv file
    return render_template("temp.html", ttl = "Random Stuff", rand = list(occs.keys())[random.randint(1, len(list(occs.keys())) - 2)], dict = occs)
#                          filename     title of page         random occupation                                                        dictionary of occupations


if __name__ == "__main__":
    app.debug = True
    app.run()
