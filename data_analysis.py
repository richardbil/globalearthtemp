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

#so, first we will want to clean the data a little bit, but because this is a free time whatever
#project, we want to do it as lazy as possible and maybe just stop after doing half of it because why not 

#okay, so lets see first, where data is missing, we suppose that information about countrys and dates is not missing, 
#but temeperature data ist so
# first, well differentiate between numeric and non numeric cols 

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

#
countrygrouped1 = global_temp_country.groupby(global_temp_country.dt.dt.year)

countrygrouped = global_temp_country.groupby(global_temp_country.Country, global_temp_country.dt)

print(countrygrouped.get_group('Germany'))
print(countrygrouped['AverageTemperature'].max())

