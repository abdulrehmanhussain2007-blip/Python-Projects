import numpy as np
arr_int=np.random.randint(1,100,20)
print(arr_int)
arr_2d=arr_int.reshape(4,5)
print(arr_2d)
print("Slicing\n",arr_2d[::-1])
#changing values
arry_2d_copy=arr_2d.copy #.copy is used to make a copy of existing variable
print(arry_2d_copy)
arr_2d[2:]=99
print("AFter changing\n",arr_2d)
#Accessing index
print(arr_2d[1,3])
#Changing value using index
arr_2d[1,3]=50
print(arr_2d)
#Slicing with combination of rows and columns
print(arr_2d[:2,1:])
print(arr_2d[2:4,2:4])
#boolean condition in numpy arrays
#print(arr_2d[arr_2d>80])
#r=arr_2d[arr_2d>80]
#print(r.reshape(2,5))
#Array arthematic
print("Arithematic array")
arr=np.arange(1,11)
print(arr)
arr1=np.arange(21,31)
print(arr1)
print(arr+arr1)
print(arr-arr1)
print(arr*arr1)
print(arr/arr1)
print(np.sqrt(arr))
print(arr*2)
#ndenumerate used to find index of a value in array
for idx,value in np.ndenumerate(arr):
    if value==9:
        print(f'Index of {value} is {idx}')
for i in range(arr.size):
    if arr[i]==9:
        print(f'Index of arr {i} is {i}')
#Check there exist zero
x=np.array([0,1,2,3])
print("Original Array",x)
print("There isn't a zero" ,np.all(x))
#All elemnts are zero
y=np.array([0,0,0,0])
print("Original Array",y)
print("There isn't a zero" ,np.any(y))
#Infinite number
z=np.array([1,0,np.inf,0])
print("Original Array",z)
print("There infinite" ,np.isinf(z))
#nan=not a number
d=np.array([1,0,np.nan,0])
print("Original Array",d)
print("There infinite" ,np.isnan(d))
#Complex number Real & Imaginary part
p=np.array([1+2j,4+3j,4.6])
print("There imaginary" ,np.iscomplex(p))