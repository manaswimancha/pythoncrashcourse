def make_car(manufacturer,model,**kwargs):
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs
print(make_car("subaru","outback",color="blue",tow_package=True,q="2"))