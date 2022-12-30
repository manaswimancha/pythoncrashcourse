import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
            return username
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username,f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        invalid_response = True
        while(invalid_response):
            response = input(f"Are you {username}? (y/n) ")
            if response=="y":
                print(f"Welcome back, {username}")
                invalid_response = False
            elif response=="n":
                get_new_username()
                invalid_response = False
            else:
                pass
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()