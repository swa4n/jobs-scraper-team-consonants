#The main goal for this program is to look for jobs in a local set of websites
#based on the user's needs or wants. Basically the output is a list of details
#related 
####this description needs to be enhanced based on the evolution of the program

#importing database file and scrapping file and fetching file
import database
import scrapping
import fetching
import re
import urllib as ul

print("Connecting to database...")
#calls the main function in scrapping file and returns the database cursor in db
db = database.main()
print("Connected!")

def input_sanitizer(keyword):
	keyword=keyword.lower()
	keyword=re.sub('"', '', keyword)
	keyword=ul.quote_plus(keyword.encode('utf-8'))
	return keyword
#Gets a valid keyword
while True:
	raw_keyword=raw_input("Enter the desired keyword\n")
	if raw_keyword.isdigit():
		print("Error! entry is a number")
	break
keyword=input_sanitizer(raw_keyword)

print("Executing scrapping...")
#calls the scrapping file 
scrapping.main(db, keyword)
print("Scrapping finished!")

#calls the fetching file 
print("Executing fetching...")
fetching.main(db, raw_keyword)
