import random

word = input('Enter 5 letters: ')
if len(word) == 5:
    i = 0
    while i < 5:
        print(''.join(random.sample(word, len(word))))
        i += 1
else:
    print('Please, enter 5 letters!')