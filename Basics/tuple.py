tuple1=(1,2,3,4,5)
print(tuple1)
print(tuple1[3])
#changing in tuple
list1=[1,2,3,4,5]
tuple2=(11,12,13,14,15)
list2=list(tuple2)
print(list2)
list2[2]=22
print(list2)
#add single item in tuple
tup1=(5,)
tup2=tuple2+tup1
print(tup2)
#generate tuple from function
def xyz():
    x=3
    y=2
    z=5
    w=x,y,z
    return w
r=xyz()
print(r)
#multiple assgment
tup4,tup5=(123,'abs'),(456,'hgf')
print(tup4)
print(tup5)
print(tuple1*3)