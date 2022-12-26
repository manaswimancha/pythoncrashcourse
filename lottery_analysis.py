from random import choice

letnum = ["A","B","C","D","E","1","2","3","4","5","6","7","8","9","10"]
t = ""
mt = ["AAAA"]
count = 1

for i in range(4):
    t += choice(letnum)

print(f"Any ticket matching \"{t}\" wins a prize.")

while(True):
    if(mt == t):
        break
    count += 1

print(f"You won! Count:{count}")