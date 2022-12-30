import json

try:
    with open("favorite_number.json") as f:
        print(json.load(f))
except FileNotFoundError:
    number = int(input("Enter your favorite number: "))
    
    with open("favorite_number.json","w") as f:
        json.dump(number,f)