class User:
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.country = "Bangladesh"
        self.language = "Bangla"
        self.food = "rice"
    
    def describe_user(self):
        print(f"The name of the user is {self.first_name} {self.last_name}.")
        print(f"The country of the user is {self.country}.")
        print(f"The language of the user is {self.language}.")
        print(f"The food of the user is {self.food}.")
   
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user1 = User("Jack","Shar")
user2 = User("Asd","Fa")
user3 = User("Dass","Sa")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()