from DataBase import MongoDBManager
import pandas as pd
import matplotlib.pyplot as plt
import ChartDrawer as chartdrawer

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

# plt.pie(top_10_percentage,labels=top_10_percentage.index,autopct='%1.1f%%',startangle=140,shadow=True)
# plt.title(f'Percentage Distribution of Confirmed Cases by Country')
# plt.show()


#en fazla dogrulanmıs vaka , ölüm ve iyilesen vaka sayisina sahip ilk 10 ülke
sorted_data = dataFrame.sort_values(by='Confirmed',ascending=False) #azalan siralama yapilir
top_10_countries=sorted_data.head(10)
print(top_10_countries[['Country/Region','Confirmed','Deaths','Recovered']])

#en fazla dogrulanmıs vaka bar grafigi
chartdrawer.plot_bar_chart(top_10_countries,'Country/Region','Confirmed','Top 10 countries with the highest confirmed cases','Countries','Confirmed')

#en fazla ölüm sayisi
chartdrawer.plot_bar_chart(top_10_countries,'Country/Region','Deaths','Top 10 countries with the highest death cases','Countries','Deaths')

#En fazla iyilesen vaka sayisi
chartdrawer.plot_bar_chart(top_10_countries,'Country/Region','Recovered','Top 10 countries with the highest recovered cases','Countries','Recovered')


#Onaylanmış vakalar, ölüm vakaları ve iyileşen vakalar arasında bir korelasyon var mı?
chartdrawer.plot_and_analyze_correlation(dataFrame,'Confirmed','Deaths','Onaylanmis vakalar ve ölüm korelasyonu','Confirmed','Deaths')

chartdrawer.plot_and_analyze_correlation(dataFrame,'Confirmed','Recovered','Onaylanmis vakalar ve iyileşme korelasyonu','Confirmed','Recovered')
