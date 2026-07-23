account=open("account.txt",mode='w')
account.write('101 abdy 3000\n')
account.write('102 ab 3000\n')
account.write('103 abd 3000\n')
account.close()
#append
account=open("account.txt",mode='a')
account.write('104 szy 1000\n')
account.write('105 bzy 1000\n')
account.write('106 bpy 1000')
account.close()
#search from file
account=open('account.txt',mode='r')
print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
for record in account:
    acc_id,name,balance=record.split()
    print(f'{acc_id:<10}{name:<10}{balance:>10}')
account.close() #ONLY SHOWING ALL ACCOUNTS
flag=0 #FROM NOW ITS SEARCHING ACCOUNTS
id=input('Please Enter account id to search')
account=open('account.txt',mode='r')
for record in account:
    acc_id,name,balance=record.split()
    if acc_id==id:
        print(f'The Account details of accounts.id {id} are as following')
        print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
        print(f'{acc_id:<10}{name:<10}{balance:>10}')
        flag=1
if flag==0:
    print("Record not found")
account.close()
       