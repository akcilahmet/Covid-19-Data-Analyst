from DataBase import MongoDBManager
import pandas as pd
import ChartDrawer as chartdrawer

mongoDb_instance=MongoDBManager()
data=mongoDb_instance.get_data()

dataFrame=pd.DataFrame(data)

#info
info=dataFrame.info()
print('x'*100)
#number of unique values
print(dataFrame['Country/Region'].nunique())
print('x'*100)
#number of unique values list
print(dataFrame['Country/Region'].unique())

#Number of null value
print(dataFrame.isnull().sum())

#Returns the number of duplicated
print(dataFrame.duplicated().sum())


#Number of confirmed cases by region
confirmed_by_country=dataFrame.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
print(confirmed_by_country)


#Percentage of confirmed cases by region
percentage=confirmed_by_country / confirmed_by_country.sum()*100
print(percentage)

#Top 10 elements of percentage of confirmed cases by region
top_10_percentage=percentage.head(10)

#Top 10 element pie chart of percentage of confirmed cases by region
chartdrawer.plot_pie_chart(top_10_percentage,'Percentage Distribution of Confirmed Cases by Country','Top10_Countries_Confirmed_Pie_Chart')


#Top 10 countries with the highest number of confirmed cases, deaths and recoveries
sorted_data = dataFrame.sort_values(by='Confirmed',ascending=False) #azalan siralama yapilir
top_10_countries=sorted_data.head(10)
print(top_10_countries[['Country/Region','Confirmed','Deaths','Recovered']])

#Top 10 confirmed cases chart
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Confirmed',
    'Top 10 countries with the highest confirmed cases',
    'Countries',
    'Confirmed',
    'Top10_Countries_Confirmed'
)

#Top 10 deaths cases chart
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Deaths',
    'Top 10 countries with the highest death cases',
    'Countries',
    'Deaths',
    'Top10_Countries_Deaths')

#Top 10 recovered cases chart
chartdrawer.plot_bar_chart(
    top_10_countries,
    'Country/Region',
    'Recovered',
    'Top 10 countries with the highest recovered cases',
    'Countries',
    'Recovered',
    'Top10_Countries_Recovered')

#Correlation
#Death correlation status with confirmed cases
chartdrawer.plot_and_analyze_correlation(
    dataFrame,
    'Confirmed',
    'Deaths',
    'Death correlation status with confirmed cases',
    'Confirmed',
    'Deaths',
    'Confirmed_Death_Correlation')

#Recovered correlation status with confirmed cases
chartdrawer.plot_and_analyze_correlation(
    dataFrame,
    'Confirmed',
    'Recovered',
    'Recovered correlation status with confirmed cases',
    'Confirmed',
    'Recovered',
    'Confirmed_Recovered_Correlation')


#100 cases status

#Recovery status per 100 cases
sorted_data_recovered_100cases = dataFrame.sort_values(by='Recovered / 100 Cases',ascending=False) #azalan siralama yapilir
top10_recovered_100_cases=sorted_data_recovered_100cases.head(10)
chartdrawer.plot_bar_chart(
    top10_recovered_100_cases,
    'Country/Region',
    'Recovered / 100 Cases',
    'Recovery status per 100 cases',
    'Countries',
    'Recovered/100 Cases',
    'Recovery_status_per_100_cases'
)
#Deaths status per 100 cases
sorted_data_deaths_100cases = dataFrame.sort_values(by='Deaths / 100 Cases',ascending=False) #azalan siralama yapilir
top10_deaths_100_cases=sorted_data_deaths_100cases.head(10)
chartdrawer.plot_bar_chart(
    top10_deaths_100_cases,
    'Country/Region',
    'Deaths / 100 Cases',
    'Deaths status per 100 cases',
    'Countries',
    'Recovered/100 Cases',
    'Deaths_status_per_100_cases'
)
