from DataBase import MongoDBManager
import pandas as pd

mongoDb_instance=MongoDBManager()
data=mongoDb_instance.get_data()

dataFrame=pd.DataFrame(data)

# info=dataFrame.info()
# shape=dataFrame.shape

# print(dataFrame['Country/Region'].nunique()) # benzersiz degerlerin sayisi
# print(dataFrame['Country/Region'].unique()) #benzersiz degerleri list olarak döner

# print(dataFrame.isnull().sum()) # sütuna ait none değer sayisini döner

# print(dataFrame.duplicated().sum()) # yinelenen kayit sayisini verir
