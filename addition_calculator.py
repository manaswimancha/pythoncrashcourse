while(True):
    try:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        print(n1+n2)
    except ValueError:
        print("You added a character instead of a number.")