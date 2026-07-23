import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tex=pd.read_csv('Textile_Company_Purchases.csv')
print(tex.head())
print(tex.dtypes)
print("Fabric type on price per meter",tex.groupby('Fabric Type')['Price per Meter'].sum().sort_values(ascending=False))
result=tex[tex['CC Exp Date'].str.contains('26')]
print(result[['Credit Card','Email','CC Security Code']])
print("order at AM or PM",tex.groupby('Lot/Order ID')['AM or PM'].sum())
print('Email and shipping address',tex.groupby('Shipping Address')['Email'].sum())
print(tex.loc[tex['Price per Meter']>15,['Fabric Type']])
print("The mean Price pr meter ",tex['Price per Meter'].mean())
print(tex.describe())
highest=tex.loc[tex['Price per Meter'].idxmax()]
print(highest[['Fabric Type','Price per Meter']])
print(tex['AM or PM'].value_counts())
revenue=tex.groupby('Fabric Type')['Price per Meter'].sum()
plt.bar(revenue.index,revenue.values,color='blue',width=0.3)
plt.xlabel("Fabric Type")
plt.ylabel("Price per Meter")
plt.title("Revenue and Parchase price relation")
plt.xticks(rotation=30)
plt.show()
plt.scatter(tex['Fabric Type'],tex['Purchase Price'])
plt.xlabel("Fabric Type")
plt.ylabel("Purchase Price")
plt.title("Fabric Type & Purchase Price")
plt.xticks(rotation=30)
plt.show()
sns.regplot(x='Quantity (Meters)',y='Price per Meter',data=tex)
plt.show()
sns.lmplot(x='Quantity (Meters)',y='Purchase Price',data=tex,col='AM or PM',hue='AM or PM',col_wrap=2,height=2)
plt.show()
sns.barplot(data=tex,x='Quantity (Meters)',y='Purchase Price',hue='AM or PM')
plt.show()