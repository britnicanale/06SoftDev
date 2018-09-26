# HalfBaked - Joshua Weiner, Britni Canale
# SoftDev1 pd06
# K #06: StI/O: Divine your Destiny!
# 2018 - 09 - 13

import random
import csv
D = {}

def makeDict(filename):
    f = open(filename, 'r') #open csv
    lineSeparated = csv.reader(f) #separate by commas, but not those in quotes
    for line in lineSeparated:
        if line[0] != 'Job Class': #control for leading line
            if line[0] != 'Total': #control for last line
                titleKey = line[0]
                percentValue = float(line[1]) #save percent value as floating point
                D[titleKey] = percentValue
    weighted_array = [] #will be an weighted array populated by the jobs
    f.close() #close csv
    for job in D:
        for numTimes in range(int(D[job] * 10)):
            #Need to convert percentages to integers accurately to use the range() function,
            weighted_array.append(job)
            #populate an array of ~1000 values, because of the use of range
            #array populated by percentages
    print(random.choice(weighted_array)) #prints one of the jobs in the weighted array


makeDict("occupations.csv") #run program
