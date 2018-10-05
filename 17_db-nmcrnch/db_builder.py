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
        reader = csv.DictReader(csvfile)  #creates sequence of dictionaries
        num = 0                           #used to determine if row is first row
        col1 = ""                         #initializes column strings
        col2 = ""
        col3 = ""
        for row in reader:                #goes through each row, adds to table
            if num == 0:                  #if row is first row, names columns based on csv file, uses list of keys to access header names
                col1 = list(row.keys())[0] 
                col2 = list(row.keys())[1]
                col3 = list(row.keys())[2]
                c.execute("CREATE TABLE " + filename[0:-4] + "(" +col1+ "  TEXT, " + col2+ " INTEGER, " +col3+" INTEGER)")  #creates table
                num = num + 1             #increments to indicate first row has been passed
            params = (row[col1],row[col2],row[col3])                                 #creates params for values using row dictionary and column names  
            c.execute("INSERT INTO " + filename[0:-4] + " VALUES(?, ?, ?)", params)  #inserts values in each row into the table


#==================Calling functions for file names used, saving changes=====================


#makeTable("courses.csv")
#makeTable("peeps.csv")
db.commit()       #save changes
#db.close()        #close database
