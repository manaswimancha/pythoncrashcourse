with open("txt_files/learning_python.txt") as file:
  for line in file.readlines():
    print(line.strip().replace("Python", "C"))