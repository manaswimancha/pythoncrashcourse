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

for j in cities:
    print(f"{j}\n")
    for i in cities[j]:
        print(f"{i}: {cities[j][i]}\n")