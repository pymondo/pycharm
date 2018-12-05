import pymongo as pm

client = pm.MongoClient("172.17.0.2:27071")
database = client["test"]
friends_collection = database["friends"]
result = friends_collection.insert_one({'name':"praveen", 'age':25})

print(result.inserted_id)