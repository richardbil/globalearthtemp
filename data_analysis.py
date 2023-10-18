import numpy as np 
import pandas as pd 
import matplotlib as plt 
import plotly as py 
import seaborn as sns
import time 

global_temp_country = pd.read_csv('/home/richard/Documents/Projects/globalearthtemp/GlobalLandTemperaturesByCountry.csv')
print(global_temp_country)