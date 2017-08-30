#This file scraps data from all the links provided in the source file and returns it in the local database.

#Importing Python libraries
import requests
import json
import re
import urllib as ul
from filtering import *
#Importing data from source file
from source import *

#Deletes quotes and replaces whitespaces with a + sign to make the keyword valid for URL use. MORE TIME
def input_sanitizer(keyword):
        keyword=keyword.lower()
        keyword=re.sub('"', '', keyword)
        keyword=ul.quote_plus(keyword.encode('utf-8'))
        return keyword

#Scrapping is importing data from the link in the source file and inserting the result in the Database

def main(db):
        #Gets a valid keyword
        while True:
                keyword=raw_input("Enter the desired keyword\n")
                if keyword.isdigit():
                        print("Error! entry is a number")
                break
        keyword=input_sanitizer(keyword)
        i=1
        #scraps the keyword-related data from the websites in the source and inserts it in the Database file
        for source in sources:
                link=source['url'].replace("{{keyword}}",keyword)
                print(link)
                print("Requesting link %d ..." %i)
                r=requests.get(link)
                print("Request complete, converting to array of JSON objects...")
                joblist =json.loads(r.text)
                print("Conversion complete! Number of job offers found : %d" %len(joblist))
                for job in joblist:
                        structurize(job,keyword,source)
                        result=db.offers.insert_one(job)
                print("Results inserted in database for link # %d" %i)
                i=i+1
