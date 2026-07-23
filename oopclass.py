class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f'Employee id={self.id} and Employee name={self.name}'
emply1=Employee(123,"Abid")
print(f'Id of employee 1 is {emply1.id} and his name is {emply1.name}')
emply2=Employee(342,"Sufyan")
print(f'Id of employee 2 is {emply2.id} and his name is {emply2.name}')
#changing name of emply2
emply2.name='Maaz'
print(f'Id of employee 2 is {emply2.id} and his changed name is {emply2.name}')
emply3=Employee(789,'Zahid')
print(f'Id of employee 3 is {emply3.id} and his name is {emply3.name}')
#Printing through str function
print("Printing through str for emply1")
print(emply1)
print("Printing through str for emply2")
print(emply2)
print("Printing through str for emply3")
print(emply3)