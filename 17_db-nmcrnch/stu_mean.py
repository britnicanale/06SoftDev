#TangyCannoli-Michelle Tang && Britni Canale
#SoftDev1 pd 6
#K17: Average
#10/7/18

import sqlite3
import csv
import db


#========Initializing Files========

DB_FILE="database.db"
dbs = sqlite3.connect(DB_FILE)
c = dbs.cursor()                           #allows sqlite to be used on database.db


#==================Calling functions for file names used, saving changes=====================


#Returns string with student's grades
def studentGrades(ID): 
    search = "SELECT name, code, mark FROM peeps, courses WHERE peeps.id="+str(ID) + " AND courses.id=peeps.id "
   # print (grades)
    c.execute(search)
    listing = c.fetchall()                        #Returns a 2D list of selected fields
    strList= "Name : " + listing[0][0] + "\n"     #displays name
    for item in listing:                          #displays averages for each course the student is enrolled in 
    	strList += "Course: " + item[1] + " Grade: "+ str(item[2]) + "\n"
    return strList


#Calculates average based on list of grades
def average(grades):
    sum = 0.0
    for grade in grades:
        sum += grade
    return sum / len(grades)
    
    
#Calculates average based on student name
def studentAverages(ID):                          #Takes only grades from student with given id
    search = "SELECT mark FROM peeps, courses WHERE peeps.id="+str(ID) + " AND courses.id=peeps.id "
    c.execute(search)
    grades= c.fetchall()                          #returns 2d list of grades 
    sum = 0.0
    for grade in grades:
		#print(grade[0])
        sum += grade[0]
    average= sum / len(grades)
    return average

print (studentAverages(1))

def display():
    search = "SELECT name , id FROM peeps"        #takes name and id from peeps table
    c.execute(search)
    listing= c.fetchall()
    strList = ""
    for entry in listing:                         #displays name and ID, uses studentAverages() to calculate average
        strList += ("Name: " + str(entry[0]) + " ID: " + str(entry[1]) + " Average: " + str(studentAverages(entry[1])) + "\n")
    return strList



#Creates table of ids and associated averages
def avgTable():
    search = "SELECT id FROM peeps"               #selects IDs
    c.execute(search)
    ids = c.fetchall()
    create = "CREATE TABLE peeps_avg (id INTEGER, average REAL)"  #Creates new table for averages
    c.execute(create)
    for id in ids:                                #Adds id with associated average (calculated using studentAverages()) to new table
        command = "INSERT INTO peeps_avg VALUES ( " + str(id[0])+ ", " + str(studentAverages(id[0]))+" )"
        c.execute(command)


#facilitates adding new rows to courses table
def addCourses(code, mark, id):
    add = "INSERT INTO courses VALUES(?, ?, ?)"
    params = (code, mark, id)
    c.execute(add, params)



#quickadd, takes 2d list of courses to add all at once
def quickaddCourses(newcourses):
    for row in newcourses:
        params = (row[0], row[1], row[2])
        add = "INSERT INTO courses VALUES(?, ?, ?)"
        c.execute(add, params)






#=================FOR TESTING PURPOSES================

print(studentGrades(10))
print(studentAverages(10))
print (display())
quickaddCourses(newcourses)
addCourses("MATH", 50, 10)






#================Saving Changes====================

dbs.commit()       #save changes    
dbs.close()        #close database 





