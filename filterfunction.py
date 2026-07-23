def myfun3(x):
    if x<18:
        return False
    else:
        return True
age=[5,6,18,40,32]
adults=filter(myfun3,age)
print("Filter function output",list(adults))