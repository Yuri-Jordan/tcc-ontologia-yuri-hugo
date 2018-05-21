import pymongo 

client = pymongo.MongoClient("192.168.99.100", 27017)

db = client['db']

coll = db['test']

 # Perform a bulk insert and return the IDs

 return coll.insert(dataset)

post = {"author": "Mike",
...         "text": "My first blog post!",
...         "tags": ["mongodb", "python", "pymongo"]}

post_id = coll.insert_one(post).inserted_id
post_id
coll.find()
