#to be decided-Michelle Tang && Britni Canale
#SoftDev1 pd 6
#K17: Average
#10/7/18

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="database.db" #it will create this
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#INSERT YOUR POPULATE CODE IN THIS ZONE
#==========================================================

# creates and execute a table with headers code, mark, and id
create = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(create)


with open("data/courses.csv","r") as csvFile: # use with to open/close file 
    csvReader = csv.DictReader(csvFile) # reads the csv file
    # iterate through the csv file, add a row!
    for line in csvReader:
        code = line["code"]
        mark = line["mark"]
        idNum = line["id"]
        command2 = "INSERT INTO courses VALUES('" + code + "', " + mark + ", " + idNum + ")"
       # command2="SELECT code FROM courses;"
        c.execute(command2)

# creates and execute a table with headers name, age, and id
create1 = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);"
c.execute(create1)

with open("data/peeps.csv","r") as csvfile: # use with to open/close file 
    reader = csv.DictReader(csvfile) # reads the csv file
    # iterate through the csv file, add a row!
    for line in reader:
        name = line['name']
        age = line['age']
        idNum = line['id']
        command = "INSERT INTO peeps VALUES('" + name + "', " + age + ", " + idNum + ")"
        c.execute(command)
#==========================================================

db.commit() #save changes
db.close()  #close database

