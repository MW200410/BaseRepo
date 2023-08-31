'''
while loop relies on boolean conditions: True/False

for loop requires an iterable object: {list, string, tuple, disctionay, set}

'''

'''
# While Loop 

loopControl = True

i = 0
while loopControl: 
    print(i)
    i += 1
    
    if i > 20:
        loopControl = False


count = 0
while count <= 20: 
    print("->",count)
    count += 1
'''


# Number Guessing 

import random

random_number = random.randint(1,10)
print("Welcome to the number guessing game")
tries = 0 # Tries/GameActive variable

while tries < 3:
    val = int(input("Guess a number between 1 and 10: "))
    print("your guess was -- > ", val)

    if val == random_number:
        print("You guessed correctly")
        break
    elif val < random_number: 
        print("Your guess was too low, try again")
    elif val > random_number: 
        print("Your guess was too high, try again")

    if val != random_number and tries == 2:
        print("Unlucky: GAME OVER!")
    
    tries += 1 





