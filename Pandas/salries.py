import pandas as pd
import numpy as np
sal=pd.read_csv('Salaries.csv')
print(sal.head())
print(sal.dtypes)
#Converting basepay object to float
print(sal['BasePay'])
sal['BasePay'].to_csv(('Base.csv'))
sal[sal['BasePay'].str.contains('not provided',case=False,na=False)]=np.nan
print(sal['BasePay'])
#To change its type
sal['BasePay']=sal['BasePay'].apply(lambda x:float(x))
print(sal.dtypes)
print("Mean basepay",sal['BasePay'].mean())
#Converting overtimepaypay object to float
sal['OvertimePay'].to_csv(('Overtime.csv'))
sal[sal['OvertimePay'].str.contains('not provided',case=False,na=False)]=np.nan
print(sal['OvertimePay'])
sal['OvertimePay']=sal['OvertimePay'].apply(lambda x:float(x))
print(sal.dtypes)
print("Overtime pay",sal['OvertimePay'].mean())
#Converting otherpay object to float
sal['OtherPay'].to_csv(('Other.csv'))
sal[sal['OtherPay'].str.contains('not provided',case=False,na=False)]=np.nan
print(sal['OtherPay'])
sal['OtherPay']=sal['OtherPay'].apply(lambda x:float(x))
print(sal.dtypes)
print("OtherPay",sal['OtherPay'].mean())
#Converting benifits object to float
sal['Benefits'].to_csv(('Benif.csv'))
sal[sal['Benefits'].str.contains('not provided',case=False,na=False)]=np.nan
print(sal['Benefits'])
sal['Benefits']=sal['Benefits'].apply(lambda x:float(x))
print(sal.dtypes)
print("Benefits",sal['Benefits'].mean())
#Print employeename job title and base pay of employee JOSEPH DRISCOLL
print(sal[['EmployeeName','JobTitle','BasePay']][sal.EmployeeName=='JOSEPH DRISCOLL'])
#print the maximum total paybenefits
print("Maximum Total Benifites",sal['TotalPayBenefits'].max())
#Employee name job tytle with highest total benefits
print("Employee with maximum total pay benifits")
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()][['EmployeeName','JobTitle','TotalPayBenefits']])
#What are unique titles
print("Unique job titles\n",sal['JobTitle'].unique())
#Display mean value of basepay year wise
print("BasePay mean groupby year\n",sal.groupby('Year')['BasePay'].mean().to_frame('Mean').reset_index())
print(sal['Agency'].unique())
#Groupby on job titles
print("BasicPay Mean GroupBy Job Titles\n",sal.groupby('JobTitle')['BasePay'].mean().to_frame('Mean').reset_index())
#Search record with Employee Name having job title chief 
df_cheif=sal[sal['JobTitle'].str.lower().str.contains('chief',na=False)][['EmployeeName','JobTitle']]
print(df_cheif.head(10))
#print("Item wise sum of price column\n",chipo.groupby("item_name")['item_price].sum())
#chippo[(chippo['quantity']>2) & (chippo['item_price']>30)]
#readcsv(url,sep='\t')
#url='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'