def make_album(name,title):
    return {"Album":name.title(),
            "Name":title.title()
            }
c = "Yes"
while(c == "Yes"):
    n = input("What is the name?: ")
    t = input("What is the title?: ")
    print(make_album(n,t))
    c = input("Do you want to continue?: ")