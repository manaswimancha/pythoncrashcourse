people = ["jamie","ed","jen","phil"]

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for i in people:
    if i in favorite_languages:
        print("Thank you for responding.")
    else:
        print("Take the poll.")