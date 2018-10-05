#TEAMNAME - Britni Canale & Michelle Tang\
#SoftDev1 pd06
#K17 - 
#2018-10-5

import sqlite3
import db_builder

db_builder.makeTable("courses.csv")
db_builder.makeTable("peeps.csv")


DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()

def findGrades(name):
    c.execute("SELECT * FROM peeps;")
    NAMES = c.fetchall()
    print(NAMES)
    for n in NAMES:
        print(n)

findGrades("alison")

db.commit()
db.close()

'''
def computeAvg(grades):


def display(name):


def createTable(
'''
