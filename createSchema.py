import json
import csvsearch


def createschema():
    # get json from googleDoc
    project = json.load(open("results.json"))

    # load the blank schema
    skeleton = json.load(open("claimSchema.json"))

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
    num = 0
    try:
        num_reqs = int(num_reqs)
        num_reqs += 1
        num_reqs -= 1
        num = num_reqs
    except:
        if num_reqs == "One" or num_reqs == "one" or num_reqs == "1":
            num = 1
        elif num_reqs == "Two" or num_reqs == "two" or num_reqs == "2":
            num = 2
        elif num_reqs == "Three" or num_reqs == "three" or num_reqs == "3":
            num = 3
    while i < num:
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
    csvsearch.write_json(skeleton, 'newSchema.json',
                         'pretty')
