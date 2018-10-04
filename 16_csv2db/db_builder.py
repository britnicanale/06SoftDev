#Britni Canale
#SoftDev1 pd 6
#K -- 
#

import sqlite3
import csv

DB_FILE="database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()


def makeReader(filename):
    try:
        f = open(filename, 'r')
        reader = csv.DictReader(f)
        print("yay")
        print(reader)
        return reader
    except:
        print("FAIL")
        return

def makeTable(c, reader):
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
    for row in reader:
        print(row)
        command = ("INSERT INTO courses  VALUES( " + row['code'] + ", " + row['mark'] + ", " + row['id'] + ")")
        print(command)
        c.execute(command)

reader = makeReader('courses.csv')
makeTable(c, reader)

#print(reader)

#==========================================================

db.commit() #save changes
db.close()  #close database
