'''MmmmmmChocolate-Britni Canale & Mohammad Uddin                               
SoftDev1 pd6                                                                    
K10 -- Jinja Tuning                                                             
2018-09-22'''

import random
import csv


#--------Functions for creating dictionary and selecting random occupation----------

occs = {}                          #initialized dictionary of occupations  

def getOcc(filename):
    f = open(filename, 'r')
    lineSeparated = csv.reader(f)
    for line in lineSeparated:
        if line[0] == 'Job Class': #exception for first, doesn't store value as float, used for heading of table
            key = line[0]          #breaks down each line into key (occupation) and value (percentage)        
            val = line[1]
            occs[key] = val
        else:
            key = line[0]
            percent = float(line[1])
            occs[key] = percent

def getRandOcc():                   #returns a random occupation                                     
    randList = list(occs.keys())    #creates a list of keys (occupations) to get the random from     
    randList.pop(0)                 #removes the first element ("Job Class")                 
    randList.pop()                  #removes the last element ("Total")                                  
    return random.choice(randList)  #returns a random occupation
