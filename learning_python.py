path = "txt_files/learning_python.txt"

with open(path) as file:
    text = file.read()
print(text)

with open(path) as file:
    for line in file.readlines():
        print(line.rstrip())

with open(path) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())