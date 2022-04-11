# create guessing game

import random

secret_number = random.randint(0,100)
input_guess = int(input("What do you think the secrect number is? "))
guess_count = 1

while secret_number != input_guess:
    guess_count += 1
    if secret_number < input_guess:
        input_guess = int(input("Lower..."))
    else:
        input_guess = int(input("Higher..."))

print(f"Got it in {guess_count} tries!")