class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type of this restaurant is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,number):
        self.number_served += number

restaurant = Restaurant("ABC","American")

print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(100)
print(restaurant.number_served)

restaurant.increment_number_served(100)
print(restaurant.number_served)