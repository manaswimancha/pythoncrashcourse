favorite_places = {
    "school": ["us","uk","au"],
    "home": ["as","ak","su"],
    "mountain": ["aa","as","ds"]
}

for j in favorite_places:
    print(f"{j}\n")
    for i in favorite_places[j]:
        print(f"{i}\n")