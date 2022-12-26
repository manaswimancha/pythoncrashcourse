current_users = ["jamie","domin","Asd","cli","asf","aer"]
new_users = ["jamie","domin","asd","clia","asfa","aera"]

i=0

for i in range(len(current_users)):
    current_users[i]=current_users[i].lower()

j=0

for j in range(len(new_users)):
    new_users[i]=new_users[i].lower()

for i in new_users:
    if i in current_users:
        print("The person will need to enter a new username.")
    else:
        print("The username is available.")