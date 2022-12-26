pet_a_info = {
    "animal": "cat",
    "owner_name": "Smth",
}

pet_b_info = {
    "animal": "dog",
    "owner_name": "Smsth",
}

pet_c_info = {
    "animal": "frog",
    "owner_name": "Smdfth",
}

pets = [pet_a_info,pet_b_info,pet_c_info]

for j in pets:
    for i in j:
        print(f"{j[i]}\n")