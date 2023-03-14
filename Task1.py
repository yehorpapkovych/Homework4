import random
guess = int(input("Try to guess the number: "))
result = random.randint(1, 10)
print('The number is:', result)
if guess == result:
    print("You're right!")
else:
    print("You're wrong!")