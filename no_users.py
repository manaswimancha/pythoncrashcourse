usernames = []

if len(usernames) == 0:
    print("We need to find some users!")
else:
    for i in usernames:
        if i == "admin":
            print(f"Hello {i}, would you like to see a status report?")
        else:
            print(f"Hello {i}, thank you for logging in again.")