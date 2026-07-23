print("\t\t\t------Welcome to customer search system------\t\t\t")
import os
#if os.path.exists("account.txt"):
    #account=open("account.txt",mode='a')
    #print("File already exists")
#else:
    #account=open("account.txt",mode='w')
    #print("File does not exist")
#acc_id=input("Enter account id")
#acc_title=input("Enter account title")
#acc_balance=input("Enter account balance")
#option='y'
#while(option!='n'):
    #acc_id=input("Enter account id\n")
    #acc_title=input("Enter account title\n")
    #acc_balance=input("Enter account balance\n")
    #record_string=acc_id+' '+acc_title+' '+acc_balance
    #account.write(record_string)
    #option=input("Do you want to contine (y/n)")
#account.close()
#Now for don't having duplicate id
option='y'
while(option!='n'):
    flag=0
    acc_id=input("Enter account id\n")
    account=open("account.txt",mode='r')
    for record in account:
        account_id,name,balance=record.split()
        if acc_id==account_id:
            flag=1
            break
    account.close()
    if flag==1:
        print(f'Account id is same as last id: {account_id}')
    else:
        acc_title=input("Enter account title\n")
        acc_balance=input("Enter account balance\n")
        account=open("account.txt",mode='a')
        record_string=acc_id+' '+acc_title+' '+acc_balance
        account.write(record_string)
        print("Account added successfully")
        option=input("Do you want to contine (y/n)")
account.close()