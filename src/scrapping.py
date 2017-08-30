#This file scraps data from all the links provided in the source file and returns it in the local database.

#Importing Python libraries
import requests
import json
from filtering import *
from source import *

def convert_to_json_array(r):
        result=json.loads(r.text)
        return result
def main(db,keyword):

        i=1
        #scraps the keyword-related data from the websites in the source and inserts it in the Database file
        for source in sources:
                link=source['url'].replace("{{keyword}}",keyword)
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
