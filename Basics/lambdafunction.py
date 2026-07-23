b=10
x=lambda a:a+b
y=x(5)
print(y)
p=lambda a,b:a*b
q=p(6,8)
print(q)
m=lambda a,b,c:a+b+c
n=m(5,10,9)
print(n)
def myfun(a):
    return len(a)
g=map(myfun,('Apple','Carrot'))
print(list(g))
#two arguments
def myfun1(o,p):
    return o,p
g=map(myfun1,('Apple','Carrot'),('Pizza','Burger'))
print(list(g))
#can we use map in lambda
num=[1,2,3,4,5]
sq_num=list(map(lambda x:x**2,num))
print(sq_num)