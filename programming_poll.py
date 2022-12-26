filename = "txt_files/programming_poll.txt"

with open(filename,"w") as file:
  while(True):
    e = input("Explain why you like programming: ")
    file.write(e+"\n")