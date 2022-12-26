from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

die1 = Die()
die2 = Die(10)
die3 = Die(20)

print("Rolling Die 1:")
for i in range(10):
    print(die1.roll_die())

print("Rolling Die 2:")
for i in range(10):
    print(die2.roll_die())

print("Rolling Die 3:")
for i in range(10):
    print(die3.roll_die())