import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
#line plot
v=40
t=np.linspace(0,50,11)
d=v*t
plt.plot(t,d,'g') #g is green color
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Distance-Time Graph')
plt.show()
#multiplots
x=t=np.linspace(0,50,11)
y=t**2
plt.subplot(1,2,1)
plt.plot(t,y,'r')
plt.subplot(1,2,2)
plt.plot(y,t,'g')
plt.show()
#Object oriented approach
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8]) #these numbers so that name doesnt mix with number
axes.plot(t,y)
axes.set_xlabel('Xlabel')
axes.set_ylabel('Ylabel')
plt.show()
#Multiple Axes graph
fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(t,y)
axes1.set_title('Larger Plot')
axes2.plot(y,t)
axes2.set_title('Smaller Plot')
plt.show()
#Object oriented approach
fig,axes=plt.subplots(2,2)
axes[0][0].plot(t,y)
axes[0][0].set_xlabel('Time')
axes[0][0].set_ylabel('Distance')
axes[0][0].set_title('Distance-Time Graph')
axes[0][1].plot(y,t)
axes[0][1].set_xlabel('Time Square')
axes[0][1].set_ylabel('Time')
axes[0][1].set_title('Time-Time Square Graph')
axes[1][0].plot(d,t)
axes[1][0].set_xlabel('Distance')
axes[1][0].set_xlabel('Time')
axes[1][0].set_title('Distance-Time Graph')
axes[1][1].plot(t,y)
axes[1][1].set_xlabel('Time')
axes[1][1].set_xlabel('Time_Square')
axes[1][1].set_title('Time-Time Square Graph')
plt.show()
#Double plot

#Bar plot
data={'C':20,'C++':15,'JAVA':30,'PYTHON':35}
langs=list(data.keys())
no_studs=list(data.values())
plt.bar(langs,no_studs,color='maroon',width=0.3) #width is thickness of bar
plt.xlabel("Programming Languages")
plt.ylabel("No. of Students")
plt.title("Students Enroll in different Languages")
plt.show()
#Bar plot through object oriented approach
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(langs,no_studs)
ax.set_xlabel('Programming Languages')
ax.set_ylabel('No. Of Students')
ax.set_title("Students Enroll in different Languages")
plt.show()
#Bar plot with comparison
#The data is multi dimensional containing no of students passed in three branches of an enigineering college 
#passed in last 4 years
data=[[30,25,50,20],[40,23,51,17],[35,22,45,19]]
x=np.arange(4)
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(x+0.0,data[0],color='g',width=0.25)
ax.bar(x+0.25,data[1],color='b',width=0.25)
ax.bar(x+0.5,data[2],color='r',width=0.25)
ax.set_xticks(x+0.25)
ax.set_xticklabels([2019,2020,2021,2022])
ax.legend(labels=['CS','IT','E&TC'])
plt.show()
#Stacked Bar
labels = ['2023', '2024', '2025', '2026']
cs = [20, 15, 30, 10]
ee = [35, 20, 25, 15]
me = [32, 25, 15, 40]
x = np.arange(len(labels))
plt.bar(x, cs, color='green', label='Computer Science')
plt.bar(x, ee, bottom=cs, color='red',
        label='Electrical Engineering')
plt.bar(x, me,
        bottom=np.array(cs) + np.array(ee),
        color='blue',
        label='Mechanical Engineering')
plt.title("Number of Students")
plt.xlabel("Years")
plt.ylabel("Students")
plt.xticks(x, labels)
plt.legend()
plt.show()
#Distribution plot
fig,ax=plt.subplots(1,1)
a=np.array([22,87,5,43,56])
ax.hist(a,bins=8,linewidth=1,edgecolor='white')
ax.set_title('Histogram of result')
ax.set_xticks(np.arange(5,100,5))
ax.set_yticks(np.arange(1,5))
ax.set_xlabel('Marks')
ax.set_ylabel('No. of Students')
plt.show()
#scatter plot
girls_grade=[22,55,44,88,77,5,66,40,51,43]
boys_grade=[21,45,54,78,87,4,99,57,53,11]
grades_range=[10,20,30,40,50,60,70,80,90,100]
fig,ax=plt.subplots(1,1)
ax.scatter(grades_range,girls_grade,color='g',label='Girls Grades')
ax.scatter(grades_range,boys_grade,color='b',label='Boys Grades')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('Grades of Boys & Girls')
ax.legend()
plt.show()
#pie plot
fig,ax=plt.subplots()
langs=['C','C++','JAVA','PYTHON']
students=[27,13,33,55,76]
ax.pie(students,label=langs,autopct='%1.2f%%')
ax.set_title('Pie Bar of Students')
ax.legend()
plt.show