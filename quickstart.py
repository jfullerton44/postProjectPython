from __future__ import print_function
import gspread
import io
import csv

import httplib2
from googleapiclient import discovery, http
from googleapiclient.http import MediaIoBaseDownload
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json


def newSheet():
    SCOPE = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    SECRETS_FILE = "userSheet.json"
    SPREADSHEET = "results"

    json_key = json.load(open(SECRETS_FILE))
    # Authenticate using the signed key
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], SCOPE)
    gc = gspread.authorize(credentials)

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    http = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http)


 

    # print("The following sheets are available")
    # for sheet in gc.openall():
    #     print("{} - {}".format(sheet.title, sheet.id))

    # Open up the workbook based on the spreadsheet name
    workbook = gc.open(SPREADSHEET)
    # Get the first sheet
    sheet = workbook.sheet1
    # Extract all data into a dataframe
    data = pd.DataFrame(sheet.get_all_records())
    file_id = '14dduhfPnC8y9euY5pH7DKONmWR_wIV_UdOF0cSBPD9Q'

    filename = 'results.csv'
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(sheet.get_all_values())


def emailsentupdate(row):
