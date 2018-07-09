import csv
import json


def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        else:
            f.write(json.dumps(data))

def opencsv():
    csv_rows = []
    with open('results.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]: row[title[i]] for i in range(len(title))}])
    lastrow = csv_rows[len(csv_rows)-1]
    write_json(lastrow, 'results.json', 'pretty')
    return lastrow['Email Address']
