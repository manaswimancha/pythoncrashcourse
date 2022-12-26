person_a_info = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 20,
    "city": "Bualo"
}

person_b_info = {
    "first_name": "Jan",
    "last_name": "Smth",
    "age": 2,
    "city": "Buflo"
}

person_c_info = {
    "first_name": "Jon",
    "last_name": "Smh",
    "age": 202,
    "city": "Buffalo"
}

people = [person_a_info,person_b_info,person_c_info]

for j in people:
    for i in j:
        print(f"{j[i]}\n")