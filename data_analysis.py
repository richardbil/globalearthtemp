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

#okay, so first of all lets build a missing data heat map

# cols = global_temp_country.columns[:100]
# colours = ['#000099', '#ffff00']
# heat = sns.heatmap(global_temp_country[cols].isnull(), cmap=sns.color_palette(colours))
# print(heat)