#Overview

When the program is run, it will check the google sheet for any new changes, and will run relevant tasks when the information has been changed. After the tasks have been run, the program will sleep  for a specified amount of time set in “main.py” (the default is 5 seconds). This loop is located in main.py and can also be found below.

``` python
  #import new sheet from google sheet api
    quickstart.newSheet()
    #open csv file to check for changes
    inputfile = csv.reader(open('results.csv', 'r'))
    #check for changes and if changes exist send email to user
    csvsearch.verification_check()
    
    print "Run Complete: " + str(datetime.datetime.now())
    sleep(5)
```

Upon finding changes in the google sheet the program will generate new json files for the project information, the schema, and the form for the supplied project. 

Curently the google api is limited to 50 writes per day on a free account.  This means that in theory only 50 projects can be created per day as after 50 writes the program will be unable to overwrite the 1 in the verified column and endless emails will be sent.

This project also contains a Dockerfile which allows for the project to run in an optimized docker container.  
