favorite_numbers = {
    "John": [13,23],
    "Mike": [21,24],
    "Slia": [23,24],
    "Asd": [34,24],
    "Fas": [12,45]
}

for j in favorite_numbers:
    print(f"{j}\n")
    for i in favorite_numbers[j]:
        print(f"{i}\n")