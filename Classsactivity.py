import random
randomno=random.randrange(1,100)
randlist=[]
for i in range (20):
    x=random.randint(1,100)
    if x not in randlist and x%5==0:
        randlist.append(x) 
print(randlist)
print("Length of the list is =",len(randlist))
randlist.sort()
randlist.pop()
print(randlist)
randlist.pop()
print(randlist)
print("The final result will be ",randlist)