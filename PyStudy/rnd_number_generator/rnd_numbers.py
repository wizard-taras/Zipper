"""
    Script name: rnd_numbers.py

    Purpose: i. To generate pseudo-random number within user-defined range

    Programmer      Date        Code changes
    Koziupa T.      12/6/22     Original code
"""
import random

user_input_l = int(input('Please enter the lower bound (intenger): '))
user_input_u = int(input('Please enter the upper bound (intenger): '))

# Generating pseudo-random number within 'user_input' range
rnd = random.randint(user_input_l, user_input_u)

print(f'Pseudo-random number within range [{user_input_l}; {user_input_u}] is: {rnd}')