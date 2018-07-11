import csv
import json
from time import sleep
import quickstart
import emailsend
import csvsearch
import datetime

def makeNewJSON():
    emailaddr = csvsearch.opencsv()
    emailsend.sendMail(emailaddr)


numRows= 0
firstRun = True
while 1:
    if firstRun:
        print "Starting"
        firstRun = False
    quickstart.newSheet()
    inputfile = csv.reader(open('results.csv', 'r'))
    csvsearch.verification_check()
    print "Run Complete: " + str(datetime.datetime.now())
    #sleep(5)
