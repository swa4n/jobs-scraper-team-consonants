# This file will fetch the data from the database to the output console

# Importing Python libraries
import requests
import json
import sys

# Importing data from database
from database import *

# main function
def main(db, keyword):
	offers = db.offers
	for job in offers.find({"tags": keyword}):
		#result=db.offers.find({"tags": keyword})
		print("The jobs offers ...", job)

