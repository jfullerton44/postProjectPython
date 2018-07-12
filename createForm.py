import json
import csvsearch


def createform():
    # load the claim form skeleton
    form_skeleton = json.load(open("claimForm.json"))

    # load project and find number of requirements project has
    project = json.load(open("results.json"))
    num_reqs = project["How many requirements for completion does your project have?"]

    # for each project requirement, create a corresponding section on the form
    i = 0
    num = 0
    try:
        num_reqs = int(num_reqs)
        num_reqs += 1
        num_reqs -= 1
        num = num_reqs
    except TypeError:
        if num_reqs == "One" or num_reqs == "one" or num_reqs == "1":
            num = 1
        elif num_reqs == "Two" or num_reqs == "two" or num_reqs == "2":
            num = 2
        elif num_reqs == "Three" or num_reqs == "three" or num_reqs == "3":
            num = 3


    while i < num:
        fields = form_skeleton["fields"]
        fields.append({
            "label": "",
            "name": "",
            "type": "text"
        })
        fields[i]["label"] = project["Requirement #" + str(i + 1)]
        fields[i]["name"] = project["Requirement #" + str(i + 1)]
        i += 1

    # print form_skeleton

    # create a new json file of completed form
    csvsearch.write_json(form_skeleton,
                         'newForm.json',
                         'pretty')

