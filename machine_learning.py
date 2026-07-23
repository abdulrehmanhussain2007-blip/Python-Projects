import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
df=pd.read_csv("data.csv")
print(df.head())
print(df.describe())
sns.pairplot(df)
plt.show()
my_df=df.select_dtypes(exclude=[object])
print(my_df.corr())
#Joint plot to check the relation seperately
sns.jointplot(x=df['Time on App'],y=df['Yearly Amount Spent'])
plt.show()
sns.jointplot(x='Time on App',y='Yearly Amount Spent',kind='reg',data=df)
plt.show()
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',kind='reg',data=df)
plt.show()
sns.jointplot(x='Length of Membership',y='Yearly Amount Spent',kind='reg',data=df)
plt.show()
corr=my_df.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.show()
print(df.columns)
x=df[['Time on App','Time on Website','Length of Membership']]
y=df['Yearly Amount Spent']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=101)
print(X_train)
print(X_test)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,y_train)
print(lm.intercept_)
print(lm.coef_)
cdf=pd.DataFrame(lm.coef_,x.columns)
print(cdf)
predictions=lm.predict(X_test)
sns.scatterplot(y_test,predictions)
sns.distplot((y_test-predictions))
from sklearn import metrics
metrics.mean_absolute_error(y_test,predictions)
from sklearn.metrics import explained_variance_score
explained_variance_score(y_test,predictions)