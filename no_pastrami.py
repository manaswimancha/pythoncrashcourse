sandwich_orders = ["peanut","chicken","egg","fish","pastrami","pastrami","pastrami"]
print(sandwich_orders)
while("pastrami" in sandwich_orders):
    sandwich_orders.pop()
print(sandwich_orders)