balance=10000; pin=2543
print('----Welcome to the ATM----')
print('----Please insert your card----')
print('----Please insert your pin----')
while True:
    if pin==2543:
        print('Please choose an option')
        print('1. Cashwithdraw')
        print('2. Cashdeposite')
        print('3. Check Current Balance')
        print('4. Exit')
        choice=input('Enter Your Choice')
        if choice=='1':
            print("Enter the amount to withdraw")
            amount=int(input('Enter the amount'))
            balance=-amount
            if balance<100:
                print('Your remaining balance is insufficient to maintain your account your account is closing')
            else:
                print('Your remaining balance is ',balance)
        elif choice=='2':
            print("Enter the amount to deposit")
            amount=int(input('Enter the amount'))
            balance=+amount
            print('Your new balance is ',balance)
        elif choice=='3':
            print('Your current balance is ',balance)
        elif choice=='4':
            print('Thanks for visiting our ATM')
            break
        else:
            print('Invalid....Please choose an option')
    else:
        print('Invalid pin please enter correct pin')