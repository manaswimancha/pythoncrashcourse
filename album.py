def make_album(name,title,songs=None):
    return {"Album":name.title(),
            "Name":title.title(),
            "Songs":str(songs)
            }
print(make_album("Elvis","A"))
print(make_album("Asdf","B"))
print(make_album("Alsjld","C"))
print(make_album("zbxmc","D",12))