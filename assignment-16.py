import pymongo
client = pymongo.MongoClient()
database = client['Students']
collection = database['students1']
for i in range(1,11):
    name=input("enter name")
    marks=int(input("enter marks"))
    collection.insert_one({'name':name, 'marks':marks})
data = collection.find({ 'marks': { '$gt': 80 } })

for document in data:
    print(document)
