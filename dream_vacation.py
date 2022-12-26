flag = True
dicti = {}

while (flag):
    user = input("What is your name? ")
    vaca = input("What is your dream vacation? ")
    dicti[user] = vaca
    resp = input("Is anybody else taking the poll? (Enter \"yes\" or \"no\") ")
    if (resp == "no"):
        flag = False
    else:
        pass

for i in dicti:
    print(f"{i} wants to go to {dicti[i]}.")