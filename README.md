# postProjectPython

This project will parse the results of a google form called "results" and export all the data to a local csv file. Then whenever a row is given the value of 1 in the "Verified" column the user will be sent an email with all the informtaion needed to create a project.

In order for this project to run correctly, the folder must contain a file called userSheet.json that contains the secret api keys in order to connect to the specific google sheet. This can be generated on googles developer console.

When running the program will check the input google sheet for any changes and run tasks based on what information has changed. After these processes complete, the program will sleep for a specified amount of time set in main.py. The current default value is 5 seconds but it can easily be adjusted.  

This project also contains a dockerfile which allows for the project to run in an optimised docker container.  

