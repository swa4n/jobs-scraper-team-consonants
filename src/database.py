#This is the Database file. It connects to the MongoDB and to the database
#It ensures the database is intially empty and adds are not repetitive.
#The output of the main function is a database.
import pymongo as pm
def main():
	client=pm.MongoClient('localhost', 27017) #connecting to mongodb
	db=client['thinkit'] #connecting to database
	offers=db.offers #getting collection
	#db.offers.delete_many({})
	return db
