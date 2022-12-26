class User:
    
    def __init__(self,first_name,last_name,country,language,food):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.language = language
        self.food = food
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}.")
        print(f"The country of the user is {self.country}.")
        print(f"The language of the user is {self.language}.")
        print(f"The food of the user is {self.food}.")
   
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Asd","Ssa","Aus","As","Ad")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(user.login_attempts)

user.reset_login_attempts()

print(user.login_attempts)