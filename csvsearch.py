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

def convert_json():
    in_file = open('results.json', 'r')
    out_file = open('project.json', 'w')

    data_file = in_file.read()
    data = json.loads(data_file)

    data['socialMedia'] = {}
    data['founder'] = {}

    for key in data.keys():

        if key == 'What is the name of your new project?':
            newKey = 'title'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Your name':
            newKey = 'ownerName'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Email Address':
            newKey = 'ownerEmail'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Please describe your project in a short sentence':
            newKey = 'shortDescription'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Now describe your project in full detail':
            newKey = 'longDescription'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'How will you measure your project claims e.g. trees planted, books donated, bags of rubbish collected':
            newKey = 'impactAction'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'In which country is your project located?':
            newKey = 'projectLocation'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Please add your SDG target and indicator (e.g. 15.1 or 2.1.1)':
            newKey = 'sdgs'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'How many claims are required to complete project e.g. 100':
            newKey = 'requiredClaims'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'What is the evaluator pay per claim?':
            newKey = 'evaluatorPayPerClaim'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Facebook':
            newKey = 'facebookLink'
            data['socialMedia'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Instagram':
            newKey = 'instagramLink'
            data['socialMedia'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Twitter':
            newKey = 'twitterLink'
            data['socialMedia'][newKey] = data[key]
            data.pop(key, None)

        elif key == "Website":
            newKey = 'webLink'
            data['socialMedia'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'socialMedia':
            pass

        elif key == 'A picture is worth a thousand words. Send us a high quality picture that best describes your project':
            newKey = 'imageLink'
            data[newKey] = data[key]
            data.pop(key, None)

        elif key == 'Project founder name':
            newKey = 'name'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Founder email':
            newKey = 'email'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Project founder country of origin':
            newKey = 'countryOfOrigin'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Short description ':
            newKey = 'shortDescription'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Website URL':
            newKey = 'websiteURL'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'Would you like to include the logo?':
            newKey = 'logoLink'
            data['founder'][newKey] = data[key]
            data.pop(key, None)

        elif key == 'founder':
            pass

        else:
            data.pop(key, None)

    claim = {'schema': '', 'form': ''}
    data['templates'] = claim

    out_file.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))


convert_json()

