'''
Created on Jan 4, 2017

@author: Jahan
'''
import random
n = 20
to_be_guessed = int(n * random.random()) + 1
'''
random.random()
    Return the next random floating point number in the range [0.0, 1.0].
'''
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")