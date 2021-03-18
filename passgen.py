import random

small_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_signs = '!@#$%&?'
password_length = 30
passwords_quantity = 5


def string_to_list(word):
    return [char for char in word]

def password_generator(pass_len, pass_dict):
    password = ''
    counter = 0
    for sign in random.sample(pass_dict, pass_len):
        password += sign
        counter += 1
        if counter == password_length:
            print(password)

pass_dictionary = string_to_list(digits + special_signs + small_letters + large_letters)

for i in range(passwords_quantity):
    password_generator(password_length, pass_dictionary)