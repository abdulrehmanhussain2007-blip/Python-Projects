import random
randomno=random.randrange(1,100)
randlist=[]
for i in range (25):
    x=random.randint(1,100)
    if x not in randlist and x<50:
        randlist.append(x) 
print(randlist)
print("Length of the list is =",len(randlist))
randlist.sort()
randlist.pop()
print("After 1st pop",randlist)
randlist.pop()
print("After 2nd pop",randlist)
randlist.pop()
print("After 3rd pop",randlist)
del randlist[0]
print("After deleting [0] ",randlist)
print("The final result will be ",randlist)