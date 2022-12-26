while(True):
    topping = input("Enter a topping (enter \"quit\" to exit): ")
    if(topping=="quit"):
        break
    print(f"We will add {topping} to your pizza.")

flag = True
while(flag):
    topping = input("Enter a topping (enter \"quit\" to exit): ")
    if(topping=="quit"):
        flag = False
    else:
        print(f"We will add {topping} to your pizza.")

topping = "jhkjhkjh"
while(topping != "quit"):
    topping = input("Enter a topping (enter \"quit\" to exit): ")
    if(topping=="quit"):
        break
    print(f"We will add {topping} to your pizza.")