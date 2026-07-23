#ASSIGNMENT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
df=pd.read_csv('student_performance.csv')
print(df.head())
print(df.info())
print(df.describe())
sns.pairplot(df)
plt.show()
my_df=df.select_dtypes(exclude=[object])
my_df.corr()
corr=my_df.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.show()
sns.jointplot(x='Hours_Studied',y='Final_Score',kind='reg',data=df)
sns.jointplot(x='Attendance',y='Final_Score',kind='reg',data=df)
sns.jointplot(x='Sleep_Hours',y='Final_Score',kind='reg',data=df)
sns.jointplot(x='Previous_Score',y='Final_Score',kind='reg',data=df)
sns.jointplot(x='Practice_Tests',y='Final_Score',kind='reg',data=df)
plt.show()
x=df[['Hours_Studied','Attendance','Sleep_Hours','Previous_Score','Practice_Tests']]
y=df['Final_Score']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.01, random_state=20) #0.04 0
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
sns.scatterplot(x=y_test,y=predictions)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.show()
sns.distplot(y_test-predictions,kde=True)
plt.show()
from sklearn import metrics
print(metrics.mean_absolute_error(y_test,predictions))
from sklearn.metrics import explained_variance_score
print(explained_variance_score(y_test,predictions))