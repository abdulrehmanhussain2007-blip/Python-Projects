import pandas as pd
import numpy as np
#Creating list
grade_series=pd.Series([1,2,3,4,5],index=pd.Index(["Chemistry","Computer","OOP","C++","PF"]))
print(grade_series)
print(grade_series['OOP'])
#Creating list without index
grade_series=pd.Series([1,2,3,4,5])
print(grade_series)
#Create python list
a=[1,7,5]
myseries=pd.Series(a,index=pd.Index(["x","y","z"]))
print(myseries)
#Create dictionary from series
calories={"Day1":22,"Day2":45,"Day3":67}
calories1=pd.Series(calories)
print(calories1)
#Series from single value
series1=pd.Series(98,range(5))
print(series1)
grade_series=pd.Series([1,2,3,4,5])
#count function
print("count",grade_series.count())
#Mean
print("Mean",grade_series.mean())
#Median
print("Median",grade_series.median())
#Minimum value
print("Minimum",grade_series.min())
#Standard deviation
print(f'Standard deviation:{grade_series.std():.2f}')
#Quantiles
print("25%",grade_series.quantile(.25))
print("50%",grade_series.quantile(.50))
#Describe
print(grade_series.describe())
#CReating a dictionary:Making dataframe using dictionary
grade_dict={"Maths":[67,95,66],"English":[55,44,88]}
grade_df=pd.DataFrame(grade_dict,index=['Ahmed','Ali',"Farhan"])
print(grade_df)
#iloc : Integer location:Access data using row and columns number
#df.iloc[row_index,column_index]
#prnt single value
print(grade_df.iloc[0,1])
#print entire row
print(grade_df.iloc[1])
#loc is a locaton by label instead of row no it use row name
print(grade_df.loc["Ali"])
#Slicing:
#Slicing rows with .iloc
print(grade_df.iloc[:2])
#Boolean mask
mask=(grade_df>=70)&(grade_df<=80)
print(mask)
#Apply mask to data frame
df=grade_df[mask] #mask change false to nan
print(df)