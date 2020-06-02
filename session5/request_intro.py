import requests
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('pollice_call')

non_emer = collection.find({
  'priority': 'Non-Emergency'
  })

print(collection.find({'priority': 'Non-Emergency'
  }).count()/collection.find({}).count_documents())