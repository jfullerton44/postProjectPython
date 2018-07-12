# postProjectPython

This project will use the results of a google form which gathers the information needed to create an ixo project. The project will parse the results of this google form in the linked google sheet and will export the data to a local csv file called “results.csv”. The project will then be verified by a staff member who will enter the number 1 in the google form spreadsheet results in the column titled “Verified”. Once a single row is detected to contain the number 1 in the “Verified” column, the client will then receive an email with the relevant information to complete the creation of their project.

An essential file that is missing in this GitHub repository is a JSON file called “userSheet.json”. This file contains the secret API keys required to connect to the google sheet connected to the google form. This file can be generated on Google’s developer console.  This is an example of the template:

```
  {"type": "service_account",
  "project_id": “PROJECT ID,
  "private_key_id": “PRIVATE KEY ID”,
  "private_key": “PRIVATE KEY” 
  "client_email": “CLIENT EMAIL”,
  "client_id": “CLIENT ID“,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "API URL"}
  ```


When the program is run, it will check the google sheet for any new changes, and will run relevant tasks when the information has been changed. After the tasks have been run, the program will sleep  for a specified amount of time set in “main.py” (the default is 5 seconds). 

This project also contains a Dockerfile which allows for the project to run in an optimized docker container.  
