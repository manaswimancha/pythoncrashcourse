pizzas = ["cheese","chicken","mushroom"]
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print("I really love pizza!")
friend_pizzas = pizzas[0:]
pizzas.append("pumpkin")
friend_pizzas.append("tomato")
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)