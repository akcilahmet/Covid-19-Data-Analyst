import pymongo
class MongoDBManager:
    def __init__(self, database_name="Covid19_db", collection_name="covid_data"):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database_name = database_name
        self.collection_name = collection_name
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def clear_data(self):
        self.collection.delete_many({})
    def insert_data(self, data):
        self.collection.insert_many(data)
    def get_data(self, filter_query=None, projection=None):
        result = self.collection.find(filter_query, projection)
        return list(result)
    def get_one_data(self,filter_query=None,projection=None):
        result=self.collection.find_one(filter_query,projection)
        return result
    def update_data(self, filter_query=None, update_data=None):
        self.collection.update_many(filter_query, {"$set": update_data})
    def delete_data(self,filter_query):
        self.collection.delete_many(filter_query)
