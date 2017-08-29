#This file scraps data from all the links provided in the source file and returns
# in a database.

#Importing Python libraries
import requests
import json
import re
import urllib as ul

#Importing data from source file
from source import *

#This function imports data from links in the source file and insert it in the Database file

def main(db):
        #Gets a valid keyword
	while True:
		keyword=raw_input("Enter the desired keyword\n")
		if keyword.isdigit():
			print("Error! entry is a number")
		break
	keyword=re.sub('"', '', keyword)
	keyword=ul.quote_plus(keyword.encode('utf-8'))
	print(keyword)

	

        #scraps the keyword-related data from the websites in the source and inserts it in the Database file
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

	
