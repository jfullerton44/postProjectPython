import pymongo
import emailcreds

def addToDB(schema, form, project):
    client = pymongo.MongoClient("mongodb+srv://newuser:"+emailcreds.mongoPassword+"@ixocreateproject-f68an.mongodb.net/test?retryWrites=true")
    db = client.trustlab
    posts = db.projects
    post_data = {
        'schema': schema,
        'form': form,
        'project': project
    }
    result = posts.insert_one(post_data)
    print format(result.inserted_id)
    return format(result.inserted_id)