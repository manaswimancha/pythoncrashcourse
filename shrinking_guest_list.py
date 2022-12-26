guests = ["Einstein","Tagore","Smith"]
print(f"Hello {guests[0]}, you are invited to dinner.")
print(f"Hello {guests[1]}, you are invited to dinner.")
print(f"Hello {guests[2]}, you are invited to dinner.")
print(guests[2])
del guests[2]
guests.append("Turing")
print(f"Hello {guests[0]}, you are invited to dinner.")
print(f"Hello {guests[1]}, you are invited to dinner.")
print(f"Hello {guests[2]}, you are invited to dinner.")
print("Hello guests, I found a bigger dinner table.")
guests.insert(0, "Jefferson")
guests.insert(2, "Washington")
guests.append("Biden")
print(f"Hello {guests[0]}, you are invited to dinner.")
print(f"Hello {guests[1]}, you are invited to dinner.")
print(f"Hello {guests[2]}, you are invited to dinner.")
print(f"Hello {guests[3]}, you are invited to dinner.")
print(f"Hello {guests[4]}, you are invited to dinner.")
print(f"Hello {guests[5]}, you are invited to dinner.")

print("Hello guests, I can invite only 2 people for dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print(f"Hello {guests[0]}, you are still invited to dinner.")
print(f"Hello {guests[1]}, you are still invited to dinner.")

del guests[1]
del guests[0]
print(guests)

