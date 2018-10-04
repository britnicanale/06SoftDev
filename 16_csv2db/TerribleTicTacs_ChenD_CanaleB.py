#TerribleTicTacs-Dennis Chen && Britni Canale
#SoftDev1 pd 6
#K16: No Trouble
#10/4/18

import sqlite3
import csv


#========Initializing Files========

DB_FILE="database.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()                           #allows sqlite to be used on database.db


#==========Function for making a table from csv==========

def makeTable(filename):
    with open(filename, 'r') as csvfile:  #opens database
        reader = csv.DictReader(csvfile)  #creates sequence of dictionaries, creates a table
        c.execute("CREATE TABLE " + filename[0:-4] + "(code TEXT, mark INTEGER, id INTEGER)")
        for row in reader:                #goes through each row, creates variables for columns depending on file input    
            col1 = list(row.keys())[0] 
            col2 = list(row.keys())[1]
            col3 = list(row.keys())[2]
            params = (row[col1],row[col2],row[col3])
            c.execute("INSERT INTO " + filename[0:-4] + " VALUES(?, ?, ?)", params)  #inserts values in each row into the table


#==================Calling functions for file names used, saving changes=====================


makeTable("courses.csv")
makeTable("peeps.csv")
#print(c.execute("SELECT * FROM cour"))
db.commit()       #save changes
db.close()        #close database
