from pymongo import MongoClient

mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('pollice_call')


# total_false_call =  collection.count({'priority': 'Non-Emergency'})
# total_call = collection.count()
# print(total_call, total_false_call)
# print(total_false_call * 100 / total_call)

all_district = collection.distinct('district')

count_call_by_district = {}
for district in all_district:
  count_call_by_district[district] = collection.count_documents({'district': district})

max = 0
name = ''
for key in count_call_by_district:
  if count_call_by_district[key] > max:
    max = count_call_by_district[key]
    name = key

print(name, max)