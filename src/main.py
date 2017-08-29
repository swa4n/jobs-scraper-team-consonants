import requests
import json
from source import *
import database

db = database.main()
keyword= input()
for link in links:
	link.replace("{{keyword}}",keyword)
	r=requests.get(link)
	joblist =json.loads(r.text)
	for job in joblist:
		result=db.offers.insert_one(job)





