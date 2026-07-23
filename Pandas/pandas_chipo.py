import pandas as pd
import numpy as np
url='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo=pd.read_csv(url,sep='\t')
print(chipo.head())
print(chipo.dtypes)
chipo['item_price']=chipo['item_price'].apply(lambda x:float(x[1:]))
print(chipo.dtypes)
chipo['revenue']=chipo['quantity']*chipo['item_price']
print(chipo.head())
print("The sum of revenue is\n",chipo.revenue.sum())
print(chipo.item_name.sort_values(ascending=False))
chipo[(chipo['quantity']>2) & (chipo['item_price']>30)]
print('Max Item Price\n',chipo.item_price.max())
print("Item wise sum of price column\n",chipo.groupby("item_name")['item_price'].sum().sort_values(ascending=False))
print(chipo.head())
chipo[chipo['choice_description'].str.contains('Not Provided',case=False,na=False)]=np.nan
print(chipo['choice_description'])