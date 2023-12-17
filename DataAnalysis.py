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

#top10 daire grafik
top_10_percentage=percentage.head(10)

chartdrawer.plot_pie_chart(top_10_percentage,'Percentage Distribution of Confirmed Cases by Country','Top10_Countries_Confirmed_Pie_Chart')


#en fazla dogrulanmıs vaka , ölüm ve iyilesen vaka sayisina sahip ilk 10 ülke
sorted_data = dataFrame.sort_values(by='Confirmed',ascending=False) #azalan siralama yapilir
top_10_countries=sorted_data.head(10)
print(top_10_countries[['Country/Region','Confirmed','Deaths','Recovered']])

#en fazla dogrulanmıs vaka bar grafigi
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Confirmed',
    'Top 10 countries with the highest confirmed cases',
    'Countries',
    'Confirmed',
    'Top10_Countries_Confirmed'
)

#en fazla ölüm sayisi
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Deaths',
    'Top 10 countries with the highest death cases',
    'Countries',
    'Deaths',
    'Top10_Countries_Deaths')

#En fazla iyilesen vaka sayisi
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Recovered',
    'Top 10 countries with the highest recovered cases',
    'Countries',
    'Recovered',
    'Top10_Countries_Recovered')


#Onaylanmış vakalar, ölüm vakaları ve iyileşen vakalar arasında bir korelasyon var mı?
chartdrawer.plot_and_analyze_correlation(
    dataFrame,
    'Confirmed',
    'Deaths',
    'Onaylanmis vakalar ve ölüm korelasyonu',
    'Confirmed',
    'Deaths',
    'Confirmed_Death_Correlation')

chartdrawer.plot_and_analyze_correlation(
    dataFrame,
    'Confirmed',
    'Recovered',
    'Onaylanmis vakalar ve iyileşme korelasyonu',
    'Confirmed',
    'Recovered',
    'Confirmed_Recovered_Correlation')


#100 vakaya top 10
sorted_data_recovered_100cases = dataFrame.sort_values(by='Recovered / 100 Cases',ascending=False) #azalan siralama yapilir
top10_recovered_100_cases=sorted_data_recovered_100cases.head(10)
#100 vakaya top 10 recovered
chartdrawer.plot_bar_chart(
    top10_recovered_100_cases,
    'Country/Region',
    'Recovered / 100 Cases',
    'Number of recovered per 100 cases',
    'Countries',
    'Recovered/100 Cases',
    'Number of recovered per 100 cases'
)
sorted_data_deaths_100cases = dataFrame.sort_values(by='Deaths / 100 Cases',ascending=False) #azalan siralama yapilir
top10_deaths_100_cases=sorted_data_deaths_100cases.head(10)
#100 vakaya top 10 deaths
chartdrawer.plot_bar_chart(
    top10_deaths_100_cases,
    'Country/Region',
    'Deaths / 100 Cases',
    'Number of deaths per 100 cases',
    'Countries',
    'Recovered/100 Cases',
    'Number of deaths per 100 cases'
)
