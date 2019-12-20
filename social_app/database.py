
import pymongo

# Database connection Class do not change it
class Database:
    uri = "mongodb://127.0.0.1:27017"
    DATABASE=None
    @staticmethod
    def initialize():

        client= pymongo.MongoClient(Database.uri)
        Database.DATABASE=client["fullstack"]
# insert something to database
    #collection is table
    # is the data inserted
    @staticmethod
    def insert(collection,data):
        return Database.DATABASE[collection].insert(data)
# find all from data base
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)
# find one thing from data base
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)





