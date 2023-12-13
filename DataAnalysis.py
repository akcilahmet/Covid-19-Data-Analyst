from DataBase import MongoDBManager
import pandas as pd
import matplotlib.pyplot as plt

mongoDb_instance=MongoDBManager()
data=mongoDb_instance.get_data()

dataFrame=pd.DataFrame(data)

# info=dataFrame.info()
# shape=dataFrame.shape

# print(dataFrame['Country/Region'].nunique()) # benzersiz degerlerin sayisi
# print(dataFrame['Country/Region'].unique()) #benzersiz degerleri list olarak döner

# print(dataFrame.isnull().sum()) # sütuna ait none değer sayisini döner

# print(dataFrame.duplicated().sum()) # yinelenen kayit sayisini verir

#
# dataFrame.rename(columns={'Country/Region':'Test'},inplace=True) #Belirtilen columns isim degistirmesini saglar
# print(dataFrame.columns)

#bölgelere göre vaka sayilari
confirmed_by_country=dataFrame.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
print(confirmed_by_country)


#yüzde hesaplama
percentage=confirmed_by_country / confirmed_by_country.sum()*100
print(percentage)

#top10
top_10_percentage=percentage.head(10)
#daire grafige cizme
plt.figure(figsize=(10,10))

plt.pie(top_10_percentage,labels=top_10_percentage.index,autopct='%1.1f%%',startangle=140,shadow=True)
plt.title(f'Percentage Distribution of Confirmed Cases by Country')
plt.show()
