import numpy as np
import pandas as pd
df=pd.read_csv('FIFA_Practice_100_Rows.csv')
print(df)
#.head to get first 5 rows
print(df.head())
#.info to get all info
df.info()
print("Total number of record",len(df))
#.columns to get all columns
print(df.columns) 
#.unique to get unique things in name or alphabets
print("Unique nationality of players",df.nationality.unique)
#To get toatal number of things in numbers
print("Toatal number of countries",df.nationality.nunique())
countries=['Spain','Brazil','Portugal','France']
print(df[df.nationality.isin(countries)])
print(df[["short_name",'nationality']])
#inplace = true means change original object
#inplace=false create a copy original remains same
df.rename(columns={'weight_kg':'weight (kg)'},inplace=True)
print(df.columns)
#query method clean data & make it readable
#.groupby to make group of a thing
#.sort_values(ascending=True) for ascending and descending
#.values.count to count values