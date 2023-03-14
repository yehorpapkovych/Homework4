name = input('Enter your name: ')
age = input('Enter your age: ')
if age.isdigit():
    int(age)
    age += 1
    str(age)
    print(f"Hello {name}, on your next birthday you'll be {age} years")
else:
    print('Write your AGE, please!')
