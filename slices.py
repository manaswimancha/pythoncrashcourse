import math
squares = [i**2 for i in range(1,11)]
middle = math.floor(len(squares)/2)
print(f"The first 3 items in this list are {squares[0:3]}")
print(f"The last 3 items in this list are {squares[-3:]}")
print(f"The middle 3 items in this list are "+
      f"{squares[(middle-2):(middle+1)]}")