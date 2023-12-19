# Covid-19-Data-Analyst
https://www.kaggle.com/datasets/imdevskp/corona-virus-report

## Data Analysis Information
```
info = dataFrame.info()
print(info)
```
![info](Graphic_Analysis_Results/Info.png)

## Number of unique values
```
print(dataFrame['Country/Region'].nunique())
187
```
## Number of unique values list
```
print(dataFrame['Country/Region'].unique())
```
![unique](Graphic_Analysis_Results/number_of_unique.png)

## Number of null value
```
print(dataFrame.isnull().sum())
```
![null_value](Graphic_Analysis_Results/Number_of_null_value.png)

## Number of confirmed cases by region
```
confirmed_by_country=dataFrame.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False)
print(confirmed_by_country
```
![confirmed_by_region](Graphic_Analysis_Results/Number_of_confirmed_case_by_region.png)

## Percentage of confirmed cases by region
```
percentage=confirmed_by_country / confirmed_by_country.sum()*100
print(percentage)
```
![percentage_confirmed_cases_by_region](Graphic_Analysis_Results/Percentage_of_confirmed_cases_by_region.png)

## Top 10 elements of percentage of confirmed cases by region
```
top_10_percentage=percentage.head(10)
```
![top_10_percentage_confirmed_cases_by_region](Graphic_Analysis_Results/Top_10_percentage_confirmed_cases_by_region.png)

## Top 10 countries with the highest number of confirmed cases, deaths and recoveries
```
sorted_data = dataFrame.sort_values(by='Confirmed',ascending=False)
top_10_countries=sorted_data.head(10)
print(top_10_countries[['Country/Region','Confirmed','Deaths','Recovered']])
```
![Top_10_countries_highest_confirmed cases_deaths_recoveries](Graphic_Analysis_Results/Top_10_countries_highest_confirmed_cases_deaths_recoveries.png)

## Percentage Distribution of Confirmed Cases by Country
![Top10Countries_Confirmed](Graphic_Analysis_Results/Top10_Countries_Confirmed_Pie_Chart.png)

## Top 10 countries with the highest confirmed cases
![Top10Countries_Confirmed](Graphic_Analysis_Results/Top10_Countries_Confirmed.png)

## Top 10 countries with the highest death cases
![Top10_Countries_Deaths](Graphic_Analysis_Results/Top10_Countries_Deaths.png)

## Top 10 countries with the highest recovered cases
![Top10_Countries_Recovered](Graphic_Analysis_Results/Top10_Countries_Recovered.png)

## Correlation Between Confirmed, Death and Recovered Cases
![Correlation](Graphic_Analysis_Results/Confirmed_Death_Correlation_heatmap.png)

## Recovery status per 100 cases
![recovery_status_100Cases](Graphic_Analysis_Results/Recovery_status_per_100_cases.png)

## Deaths status per 100 cases
![death_status_100Cases](Graphic_Analysis_Results/Deaths_status_per_100_cases.png)





