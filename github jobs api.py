import requests
import pymongo as pm
import json
client=pm.MongoClient('localhost', 27017) #connecting to mongodb
db=client['thinkit'] #connecting to database
offers=db.offers #getting collection
db.offers.delete_many({})
keyword= input()
link="http://jobs.github.com/positions.json?description="+keyword
r=requests.get(link)
joblist =json.loads(r.text)
for job in joblist:
	#print(job['title'])
	result=offers.insert_one(job)
	#print(result.inserted_id)
cursor = db.offers.find()
for doc in cursor:
	print(doc)
