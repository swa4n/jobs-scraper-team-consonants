import database
import scrapping
print("Connecting to database...")
db = database.main()
print("Connected!")
print("Executing scrapping...")
scrapping.main(db)
print("Scrapping finished!")
