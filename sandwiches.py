def sandwich_toppings(*toppings):
    print("Ordering a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
sandwich_toppings("mayo","cheese","tuna")
sandwich_toppings("mayo","cheese")
sandwich_toppings("mayo")