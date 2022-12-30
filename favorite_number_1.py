import json

number = int(input("Enter your favorite number: "))

with open("txt_files/favorite_number.json","w") as f:
    json.dump(number,f)