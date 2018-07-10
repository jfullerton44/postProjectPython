import csv
import json
from time import sleep
import quickstart
import emailsend
import csvsearch

def makeNewJSON():
    emailaddr = csvsearch.opencsv()

    csvsearch.convert_json()
    emailsend.sendMail(emailaddr)


numRows= 0
firstRun = True
while 1:
    lastRows = numRows
    quickstart.newSheet()
    inputfile = csv.reader(open('results.csv', 'r'))
    i=0
    for row in inputfile:
        i=i+1
    numRows=i
    if not firstRun:
        if lastRows != numRows:
            makeNewJSON()
            print "Updating"
    firstRun = False
    sleep(5)
