sandwich_orders = ["peanut","chicken","egg","fish"]
finished_sandwiches = []
while(sandwich_orders):
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
