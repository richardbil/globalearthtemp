import numpy as np 
import pandas as pd 
import matplotlib as plt 
import plotly as py 
import seaborn as sns
import time 

global_temp_country = pd.read_csv('/home/richard/Documents/Projects/globalearthtemp/GlobalLandTemperaturesByCountry.csv')
print(global_temp_country)

Summary = global_temp_country.describe()
print(Summary)
print(global_temp_country.shape)
print(global_temp_country.dtypes)

#So, first we probably want to clean the data and delete the countrys where too much data is missing
#At first, well differentiate between numeric and non numeric cols 

numeric_cols = global_temp_country.select_dtypes(include=['number']).columns
print('Numeric is '+numeric_cols)

non_numeric_cols = global_temp_country.select_dtypes(exclude=['number']).columns
print('Non numeric is '+non_numeric_cols)

# okay, newly realized that, before doing anything else, we maybe sould look into the methods, we plan to use,
#because there are different needs for clean data, so lets start with something easy instaed
#but for the first analysis, lets store a new version without missing temps

global_temp_country_withoutNaN = global_temp_country.dropna()
print(global_temp_country_withoutNaN.describe())
print(global_temp_country_withoutNaN.shape)

#calculate the percentage of missing data
missing_percentage = global_temp_country.groupby('Country').apply(lambda x: x['AverageTemperature'].isnull().mean())
print(missing_percentage)

#get countries with more than 20 % missing
countries_to_drop = missing_percentage[missing_percentage > 0.2].index
print(countries_to_drop)

global_temp_country = global_temp_country[~global_temp_country['Country'].isin(countries_to_drop)]
global_temp_country.to_csv('cleaned_data_country.csv', index=False)

#okay, so lets organise the countrys by sorting by biggest growth in yearly averages 

country_cleaned = pd.read_csv('/home/richard/Documents/Projects/globalearthtemp/cleaned_data_country.csv')

# okay lets get the average temp of each countrys
countries = np.unique(country_cleaned['Country'])
mean_temp = []
for country in countries:
	mean_temp.append(country_cleaned[country_cleaned['Country'] == country]['AverageTemperature'].mean())
print(mean_temp)


biggest_difference_temp = []
for country in countries:
	biggest_difference_temp.append(country_cleaned[country_cleaned['Country'] == country]