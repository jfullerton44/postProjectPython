#Credentials

In order for the program to run correctly a file must be inserted called emailcreds.py containing login information for a gmail address and a mongodb user.

The format of the file is as follows:
`````python
  login = <Gmail login>
  password= <Gmail password>
  mongoUser = <Mongo username>
  mongoPassword = <Mongo Password>
`````

The gmail login that you provide will be used to send out emails containing the information for the user to create a project and the mongo credientials will be used to store the data from the projcet so that it can be accessed by the front end react app when the projcet is going to be created.

Another essential file that is missing in this GitHub repository is a JSON file called “userSheet.json”. This file contains the secret API keys required to connect to the google sheet connected to the google form. This file can be generated on Google’s developer console.  This is an example of the template:

````json
  {"type": "service_account",
  "project_id": "PROJECT ID",
  "private_key_id": "PRIVATE KEY ID",
  "private_key": "PRIVATE KEY" ,
  "client_email": "CLIENT EMAIL",
  "client_id": "CLIENT ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "API URL"}
````

