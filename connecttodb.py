import pymongo
import emailcreds

def addToDB(schema, form, project):
    #define mongodb client url
    client = pymongo.MongoClient("mongodb+srv://newuser:"+emailcreds.mongoPassword+"@ixocreateproject-f68an.mongodb.net/test?retryWrites=true")
    #define database and collection
    db = client.trustlab
    posts = db.projects
    #add data to post
    post_data = {
        'schema': schema,
        'form': form,
        'project': project
    }
    #insert post to database
    result = posts.insert_one(post_data)
    print format(result.inserted_id)
    return format(result.inserted_id)