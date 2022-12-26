class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type of this restaurant is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Our flavors are:")
        for i in self.flavors:
            print(i)

ice_cream_stand = IceCreamStand("Assds","Ice Cream",["Choco","Asdas","Afshd","Gjj"])

ice_cream_stand.display_flavors()