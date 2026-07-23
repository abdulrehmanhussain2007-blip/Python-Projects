import pandas as pd
import numpy as np
df=pd.read_csv("Ecommerce Purchases.csv")
print(df)
print(df.columns)
#ASSIGNMENT 1
result=df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)]
print(result[['Email','CC Provider','Purchase Price']])
#ASSIGNMENT 2
result2=df[(df['CC Exp Date'].str.contains('26'))]
print(result2[['Email','CC Exp Date']])