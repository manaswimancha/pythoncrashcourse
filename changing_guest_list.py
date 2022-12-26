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