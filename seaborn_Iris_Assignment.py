import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as  plt
print(sns.get_dataset_names())
#IRIS
ir=sns.load_dataset('iris')
print(ir.head())
#Scatter Plot
plt.scatter(ir.sepal_length,ir.petal_length)
sns.despine()
plt.show()
#Relation Plot
sns.relplot(data=ir,x='sepal_width',y='petal_width',hue='species')
sns.set_style("darkgrid")
plt.show()
#Dis Plot
sns.displot((ir['petal_length']))
plt.show()
#Count Plot
sns.countplot(x='sepal_width',hue='petal_length',data=ir,palette='magma')
plt.show()
#Bar Plot
sns.barplot(data=ir,x='sepal_length',y='sepal_width',hue='species')
plt.show()
#Joint Plot
sns.jointplot(x='petal_length',y='sepal_width',data=ir,kind='reg')
plt.show()
#Reg Plot
sns.regplot(x='petal_width',y='petal_length',data=ir)
plt.show()
#Linear Plot
sns.lmplot(x='petal_width',y='sepal_length',data=ir,col='species',hue='species',col_wrap=2,height=2)
plt.show()
#Box Plot
sns.boxplot(x='petal_length',y='petal_width',data=ir)
plt.show()
#Pair Plot
sns.pairplot(ir,hue='petal_width',kind='scatter',palette='husl')
plt.show()
#Heatmap Plot
corr=ir.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()
#Swarm Plot
sns.swarmplot(x='petal_width',y='sepal_width',data=ir,palette='Set2')
plt.show()
#Count Plot
sns.countplot(x='petal_length',data=ir)
plt.show()