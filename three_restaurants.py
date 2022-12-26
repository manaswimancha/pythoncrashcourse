class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type of this restaurant is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant1 = Restaurant("ABC","American")
restaurant2 = Restaurant("AB","Ameri")
restaurant3 = Restaurant("A","Am")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()