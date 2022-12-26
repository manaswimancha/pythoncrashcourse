filename = "txt_files/guest_book.txt"

with open(filename,"w") as file:
  while(True):
    name = input("Enter your name: ")
    file.write(name+"\n")
    print(f"Hello, {name}!")