name = input('Enter your name: ')
age = input('Enter your age: ')
if age.isdigit():
    age1 = int(age) + 1
    str(age1)
    print(f"Hello {name}, on your next birthday you'll be {age1} years")
else:
    print('Write your AGE, please!')
