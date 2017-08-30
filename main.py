#The main goal for this program is to look for jobs in a local set of websites
#based on the user's needs or wants. Basically the output is a list of details
#related 
####this description needs to be inhanced based on the evolution of the program

#importing database file and scrapping file
import database
import scrapping

print("Connecting to database...")
#calls the main function in scrapping file and returns the database in db
db = database.main()
print("Connected!")
print("Executing scrapping...")

#calls the scrapping file 
scrapping.main(db)
print("Scrapping finished!")





