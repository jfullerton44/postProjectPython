import csv
import json
from time import sleep
import quickstart
import emailsend
import csvsearch
import datetime

numRows= 0
firstRun = True
while 1:
    if firstRun:
        print "Starting"
        firstRun = False
    #import new sheet from google sheet api
    quickstart.newSheet()
    #open csv file to check for changes
    inputfile = csv.reader(open('results.csv', 'r'))
    #check for changes and if changes exist send email to user
    csvsearch.verification_check()
    
    print "Run Complete: " + str(datetime.datetime.now())
    sleep(5)
