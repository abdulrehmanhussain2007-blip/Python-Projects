list1=list(range(1,21))
print(list1)
list2=[x for x in list1 if x%2!=0]
print("For odd",list2)
list2=[x+1 for x in list1 if x%2!=0]
print("For even",list2)
fruits=["apple","mango"]
fruits1=[x.upper() for x in fruits]
print(fruits)
print(fruits1)
list3=list(range(1,101))
list4=[x for x in list3 if x%3==0 and x%5==0]
print(list4)
