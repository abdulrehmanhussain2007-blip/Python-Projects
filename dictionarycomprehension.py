import math
days_per_month={'Jan':21,'Feb':22}
monhs2={days:month for month,days in days_per_month.items()}
print(monhs2)
#grad_summary dictionary
grade={'Abd':[22,4,56],'Dcs':[55,99,87]}
grade_summary={name:math.ceil(sum(marks)/len(marks)) for name,marks in grade.items()}
print(grade_summary)
#1-5 with cubes and dictonary
number={number:number**3 for number in range(1,6)}
print(number)
#names to upper case
names=["Sayiqa", "Jabeen","Sara"]
names1={name:name.upper() for name in names}
print(names1)



