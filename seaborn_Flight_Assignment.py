import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as  plt
print(sns.get_dataset_names())
#Flights
fl=sns.load_dataset('flights')
print(fl.head())
#Scatter Plot
plt.scatter(fl.year,fl.passengers)
sns.despine()
plt.show()
#Relation Plot
sns.relplot(data=fl,x='year',y='passengers',hue='month')
sns.set_style("darkgrid")
plt.show()
#Dis Plot
sns.displot((fl['passengers']))
plt.show()
#Count Plot
sns.countplot(x='month',hue='passengers',data=fl,palette='magma')
plt.show()
#Bar Plot
sns.barplot(data=fl,x='year',y='passengers',hue='month')
plt.show()
#Joint Plot
sns.jointplot(x='year',y='passengers',data=fl,kind='reg')
plt.show()
#Reg Plot
sns.regplot(x='year',y='passengers',data=fl)
plt.show()
#Linear Plot
sns.lmplot(x='year',y='passengers',data=fl,col='month',hue='month',col_wrap=2,height=2)
plt.show()
#Box Plot
sns.boxplot(x='year',y='passengers',data=fl)
plt.show()
#Pair Plot
sns.pairplot(fl,hue='passengers',kind='scatter',palette='husl')
plt.show()
#Heatmap Plot
corr=fl.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
#Swarm Plot
sns.swarmplot(x='year',y='passengers',data=fl,palette='Set2')
plt.show()
#Count Plot
sns.countplot(x='passengers',data=fl)
plt.show()
