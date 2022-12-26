try:
    with open("txt_files/cats.txt") as f:
        print(f.read())
    with open("txt_files/dogs.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("A file is missing.")