'''MmmmmmChocolate-Britni Canale & Mohammad Uddin
SoftDev1 pd6
K10 -- Jinja Tuning
2018-09-22'''

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
            key = line[0]
            val = line[1]
            occs[key] = val
        else:
            key = line[0]
            percent = float(line[1])
            occs[key] = percent

def getRandOcc():  #returns a random occupation
    randList = list(occs.keys())
    randList.pop(0)
    randList.pop()
    return random.choice(randList)

@app.route("/")
def hello_world():
    return "This is the home page<br><a href = \"/occupations\"> Here </a> is a link to a page with information regarding occupations"

@app.route("/occupations")
def hello_temp():
    getOcc("data/occupations.csv") #calls function that created dictionary out of the csv file
    return render_template("temp.html", ttl = "Occupations in the United States", rand = getRandOcc(), dict = occs, header = 'Job Class', footer = 'Total')
#                          filename     title of page                             random occupation    dictionary of occupations


if __name__ == "__main__":
    app.debug = True
    app.run()
