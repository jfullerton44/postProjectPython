import json
import csvsearch


def createschema():
    # get json from googleDoc
    project = json.load(open("C:\\Users\\George Magloire\\OneDrive\TrustLab\\postProjectPython\\results.json"))

    # load the blank schema
    skeleton = json.load(open("C:\Users\George Magloire\OneDrive\TrustLab\postProjectPython\claimSchema.json"))

    # define what a requirement looks like
    requirement = {
        "$id": "/properties/payload/properties/data/properties/projectDid",
        "type": "string",
        "title": "The project did",
        "default": "",
        "examples": [
        ]
    }

    # add project completion requirements to schema of project
    num_reqs = project["How many requirements for completion does your project have?"]
    i = 0
    while i < int(num_reqs):
        new_req_name = project["Requirement #" + (str(i + 1))]
        print ("Requirement name: " + new_req_name)
        skeleton["properties"]["payload"]["properties"]["data"]["properties"][new_req_name] = requirement
        skeleton["properties"]["payload"]["properties"]["data"]["properties"][new_req_name]["title"] = new_req_name
        print skeleton["properties"]["payload"]["properties"]["data"]["properties"][new_req_name]

        # add the title of these requirements to "required" property in json
        skeleton["properties"]["payload"]["properties"]["data"]["required"].append(new_req_name)
        i += 1

    # test output
    print("Requirements: " + str(skeleton["properties"]["payload"]["properties"]["data"]["required"]))

    # create a new json file of completed template
    csvsearch.write_json(skeleton, 'C:\\Users\\George Magloire\\OneDrive\\TrustLab\\postProjectPython\\newSchema.json.',
                         'pretty')


createschema()
