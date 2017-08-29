import requests
import json
import re
import urllib as ul
from source import *
def main(db):
	while True:
		keyword=raw_input("Enter the desired keyword\n")
		if keyword.isdigit():
			print("Error! entry is a number")
		break
	keyword=re.sub('"', '', keyword)
	keyword=ul.quote_plus(keyword.encode('utf-8'))
	print(keyword)
	i=1
	for link in links:
		link=link.replace("{{keyword}}",keyword)
		print(link)
		print("Requesting link %d ..." %i)
		r=requests.get(link)
		print("Request complete, converting to array of JSON objects...")
		joblist =json.loads(r.text)
		print("Conversion complete! Number of job offers found : %d" %len(joblist))
		for job in joblist:
			result=db.offers.insert_one(job)
		print("Results inserted in database for link # %d" %i)
		i=i+1
