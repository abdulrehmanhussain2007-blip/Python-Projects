while True:
    celsius=float(input("Enter Celsius"))
    farenheit=celsius*1.8+32
    print(farenheit,"Farenheit")
    print("Do you want to do conversation again")
    choice=input("Enter your choice")
    if(choice=='y'):
        print("Enter again")
    else:
        break