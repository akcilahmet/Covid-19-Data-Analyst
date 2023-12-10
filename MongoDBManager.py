import pymongo
import pandas as pd

class MongoDBManager:
    def __init__(self,database_name="Covid19_db",collection_name="covid_data"):
        self.client=pymongo.MongoClient("mongodb://localhost:27017/")
        self.database_name=database_name
        self.collection_name=collection_name
        self.db=self.client[database_name]
        self.collection=self.db[collection_name]

    def clear_data(self):
        self.collection.delete_many({})
    def insert_data(self,data):
        self.collection.insert_many(data)
    def get_data(self,filter_query=None,projection=None):
        result = self.collection.find(filter_query,projection)
        return list(result)
    def get_length(self):
        return self.collection.count_documents({})


df =pd.read_csv(r'D:\github\Covid-19-Data-Analyst\Covid-19-DataSets\country_wise_latest.csv')
mongo_manager=MongoDBManager()
mongo_manager.clear_data()
data_dict=df.to_dict("records")
mongo_manager.insert_data(data_dict)
print(mongo_manager.get_length())
print(mongo_manager.get_data({"Country/Region":"Turkey"}))