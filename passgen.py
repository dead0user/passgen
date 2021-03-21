import random
import argparse

small_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_signs = '!@#$%&?'
# password_length = 15
# passwords_quantity = 5


parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store',
                    dest='force_of_pass', type=int,
                    help="Force of password(1:low, 2:mid, 3:high)")
parser.add_argument('-q', action='store',
                    dest='passwords_quantity', type=int,
                    help="Quantity of generated password")
parser.add_argument('-l', action='store',
                    dest='password_length', type=int,
                    help="Length of generated passwords")

argument = parser.parse_args()

def string_to_list(word):
    return [char for char in word]

def password_generator(pass_len, pass_dict):
    password = ''
    counter = 0
    for sign in random.sample(pass_dict, pass_len):
        password += sign
        counter += 1
        if counter == pass_len:
            print(password)


if argument.force_of_pass == 1:
    pass_dictionary = string_to_list(digits + small_letters)
elif argument.force_of_pass == 2:
    pass_dictionary = string_to_list(digits + small_letters + large_letters)
elif argument.force_of_pass == 3:
    pass_dictionary = string_to_list(digits + small_letters + large_letters + special_signs)
else:
    print("Bad argument: must be 1, 2 or 3 !!!")
    pass


# pass_dictionary = string_to_list(digits + special_signs + small_letters + large_letters)

for i in range(argument.passwords_quantity):
    password_generator(argument.password_length, pass_dictionary)