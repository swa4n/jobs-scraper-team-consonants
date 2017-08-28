import requests

import json
import sources from "./source.py"


keyword= input()



r=requests.get(link)
joblist =json.loads(r.text)
for job in joblist:
	#print(job['title'])
	result=offers.insert_one(job)
	#print(result.inserted_id)





