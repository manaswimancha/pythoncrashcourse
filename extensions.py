cities = {
    "new york": {
    "country": "us",
    "population": "1000",
    "fact": "jashdlknlkjkljlkjlkjlkksd"
    },
    "buffalo": {
    "country": "us",
    "population": "12312",
    "fact": "jashdksdsndkjsdn"
    },
    "jersey": {
    "country": "us",
    "population": "123123",
    "fact": "jashdksd"
    }
}

l=0
for j in cities:
    print(f"{j.title()}\n")
    for i in cities[j]:
        if i=="country":
            print(f"{i.title()}: {cities[j][i].upper()}\n")
        else:
            print(f"{i.title()}: {cities[j][i]}\n")
    if l < (len(cities)-1):
        print("-"*30)
        print(""*30)
    l+=1