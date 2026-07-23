import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as  plt
print(sns.get_dataset_names())
#Car crashes
df=sns.load_dataset('car_crashes')
print(df.head())
plt.scatter(df.speeding,df.alcohol)
plt.show()
sns.set_style("whitegrid")
plt.scatter(df.speeding,df.alcohol)
sns.despine()
plt.show()
#Tips
tips=sns.load_dataset('tips')
print(tips.head())
sns.relplot(data=tips,x='total_bill',y='tip')
plt.show()
print(tips.day.unique())
sns.relplot(data=tips,x='total_bill',y='tip',hue='day')
plt.show()
sns.relplot(data=tips,x='total_bill',y='tip',hue='time')
plt.show()
sns.relplot(data=tips,x='total_bill',y='tip',hue='sex')
plt.show()
sns.set_style('darkgrid')
sns.relplot(data=tips,x='total_bill',y='tip',hue='time',col='day',col_wrap=2)
plt.show()
sns.relplot(data=tips,x='total_bill',y='tip',hue='smoker',col='day',col_wrap=2)
plt.show()
#Seperate relation plot for male and female add hue for smoker
sns.relplot(data=tips,x='total_bill',y='tip',hue='smoker',col='sex',col_wrap=2)
plt.show()
#Seaborn histogram
sns.displot(tips['tip'])
plt.show()
print(len(tips[(tips['tip']>2)&(tips['tip']>=3)]))
sns.countplot(x='time',data=tips)
plt.show()
#Titanic
titanic=sns.load_dataset('titanic')
print(titanic.head())
sns.barplot(x='embarked',y='age',data=titanic)
plt.show()
print(titanic.embark_town.unique())
sns.countplot(x='survived',data=titanic)
plt.show()
sns.countplot(x='survived',hue='sex',data=titanic)
plt.show()
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()
sns.countplot(x='class',hue='who',data=titanic,palette='magma')   #palette is for coloring
plt.title("Survivors")
plt.show()
sns.jointplot(x='total_bill',y='tip',data=tips)   #Scatter+Distribution plot
plt.show()
#line fittig
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
plt.show()
sns.regplot(x='total_bill',y='tip',data=tips)
plt.show()
#Linear plot
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()
sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='day',col_wrap=2,height=3)
plt.show()
#Box plot
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()
#pairplot
sns.pairplot(tips,hue='time',kind='scatter',palette='husl')
plt.show()
#Check correlation
corr=tips.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
sns.jointplot(x='fare',y='age',data=titanic)
plt.show()
sns.boxplot(x='class',y='age',data=titanic)
plt.show()
sns.displot(titanic['fare'],bins=30,color='green')
plt.show()
#Swarm plot
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
plt.show()
#count plot
sns.countplot(x='sex',data=titanic)
plt.show()
corr=titanic.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
#irirs & flights assignment 
