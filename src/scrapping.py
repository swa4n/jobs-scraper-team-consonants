import requests
import json
from source import *
def main(db):
	print("Enter the desired tag between quotes and replacing spaces with +")
	keyword= input()
	i=1
	for link in links:
		link.replace("{{keyword}}",keyword)
		print("Requesting link "+str(i)+" ...")
		r=requests.get(link)
		print("Request complete, converting to array of JSON objects...")
		joblist =json.loads(r.text)
		print("Conversion complete! starting database insertion...")
		for job in joblist:
			result=db.offers.insert_one(job)
		print("Results inserted in database for link number %s", i)
		i=i+1
