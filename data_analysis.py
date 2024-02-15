import numpy as np 
import pandas as pd 
import matplotlib as plt 
import plotly as py 
import seaborn as sns
import time 
import cartopy.crs as ccrs

global_temp_country = pd.read_csv('/home/richard/Documents/Projects/globalearthtemp/GlobalLandTemperaturesByCountry.csv')
print(global_temp_country)

Summary = global_temp_country.describe()
print(Summary)
print(global_temp_country.shape)
print(global_temp_country.dtypes)

#just checking, if panda think the data is normal data
print(type(global_temp_country["Country"]))
print(type(global_temp_country["AverageTemperature"]))

print(global_temp_country["Country"].shape)
print(global_temp_country["AverageTemperature"].shape)

#lets get familiar with the data

print(global_temp_country.describe())

countries = np.unique(global_temp_country['Country'])
mean_temp = []
for country in countries:
	mean_temp.append(global_temp_country[global_temp_country['Country'] == country]['AverageTemperature'].mean()
		)
print(mean_temp)
