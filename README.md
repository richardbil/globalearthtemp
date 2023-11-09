# Global Earth Temperature Data Analysis

So this is basically just some playing around, there is no claim to meet demands to completeness or scientific rigor or whatever else.
There are also no standarts here to satisfy any demands for readibility or anything else that brings comfort to hypothetical reades, so.. 

## The Data: 

Got it from Kaggle, basically just Temperature Data Worldwide as conclusive as possible, dating back to 1750s, with monthly averages. You can get it from this link:

https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data

I didnt change the names of the data sheets or variables, because that way everyone can theorically download the analysis and the data sheets and let it run again. Only thing youd have to change are the directories given to the analysis. The gitignore file tells git to not include the .csv files in its version control, the main reason for that is, that github has some special ways to upload bigger files and i didnt care about configuring that. So if someone would fork the repository, youd still have to download the data seperately.

## What we want to do:

1. First, we'd like to do some simple analysis
	1. First some visual analysis of the data.
		1. How much missing data by country?
		2. How is the data distributed about the countrys? 
		3. How is the growth in average means distributed?
	2. Some Interpretation of what we have seen
2. Time Series Analysis
	1. Checking for Heteroskedasticity
	2. other stuff
	3. Plotting it really nicely
3. Wrapping it up by writing a blogpost about it, including some of the code, the visuals and some other fancy stuff 


PS.: I donct remember anything about time series analysis, so ill have to read up on that, only the fancy word heterosekdasticity is still in my mind. 



