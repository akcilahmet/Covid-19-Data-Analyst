# Covid-19-Data-Analyst
https://www.kaggle.com/datasets/imdevskp/corona-virus-report




## Percentage Distribution of Confirmed Cases by Country
![Top10Countries_Confirmed](Graphic_Analysis_Results/Top10_Countries_Confirmed_Pie_Chart.png)

## Top 10 countries with the highest confirmed cases
![Top10Countries_Confirmed](Graphic_Analysis_Results/Top10_Countries_Confirmed.png)

## Top 10 countries with the highest death cases
![Top10_Countries_Deaths](Graphic_Analysis_Results/Top10_Countries_Deaths.png)

## Top 10 countries with the highest recovered cases
![Top10_Countries_Recovered](Graphic_Analysis_Results/Top10_Countries_Recovered.png)

## Death correlation status with confirmed cases
![Death_correlation](Graphic_Analysis_Results/Confirmed_Death_Correlation.png)

## Recovered correlation status with confirmed cases
![Recovered_correlation](Graphic_Analysis_Results/Confirmed_Recovered_Correlation.png)

## Recovery status per 100 cases
![recovery_status_100Cases](Graphic_Analysis_Results/Recovery_status_per_100_cases.png)

## Deaths status per 100 cases
![death_status_100Cases](Graphic_Analysis_Results/Deaths_status_per_100_cases.png)




## Data Analysis Information
```
info = dataFrame.info()
print(info)
```

## Number of unique values
```
print(dataFrame['Country/Region'].nunique())
```
## Number of unique values list
```
print(dataFrame['Country/Region'].unique())
```

## Number of null value
```
print(dataFrame.isnull().sum())
```
## Number of confirmed cases by region
```
confirmed_by_country=dataFrame.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
print(confirmed_by_country
```

## Percentage of confirmed cases by region
```
percentage=confirmed_by_country / confirmed_by_country.sum()*100
print(percentage)
```

## Top 10 elements of percentage of confirmed cases by region
```
top_10_percentage=percentage.head(10)
```

## Top 10 countries with the highest number of confirmed cases, deaths and recoveries
```
sorted_data = dataFrame.sort_values(by='Confirmed',ascending=False) #azalan siralama yapilir
top_10_countries=sorted_data.head(10)
print(top_10_countries[['Country/Region','Confirmed','Deaths','Recovered']])
```