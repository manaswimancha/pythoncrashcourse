while(True):
    age = int(input("Enter your age: "))
    if(age<3):
        print("Ticket price: $0")
    elif(age>=3 and age<=12):
        print("Ticket price: $10")
    else:
        print("Ticket price: $15")