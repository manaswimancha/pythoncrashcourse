import json

with open("txt_files/favorite_number.json") as f:
    print(json.load(f))