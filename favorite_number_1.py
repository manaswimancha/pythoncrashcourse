import json

number = int(input("Enter your favorite number: "))

with open("favorite_number.json","w") as f:
    json.dump(number,f)