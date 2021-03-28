import argparse
import sys
import fgen

small_letters = 'abcdefghijklmnopqrstuvwxyz'
large_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_signs = '!@#$%&?'


parser = argparse.ArgumentParser()

parser.add_argument('-f', action='store', required=True,
                    dest='force_of_pass', type=int,
                    help="Force of password(1:low, 2:mid, 3:high)")
parser.add_argument('-q', action='store', required=True,
                    dest='passwords_quantity', type=int,
                    help="Quantity of generated password")
parser.add_argument('-l', action='store', required=True,
                    dest='password_length', type=int,
                    help="Length of generated passwords(from 5 to 60 chars)")

parser.parse_args(args=None if sys.argv[1:] else ['--help'])

argument = parser.parse_args()

if argument.force_of_pass == 1:
    pass_dictionary = fgen.string_to_list(digits + small_letters)
elif argument.force_of_pass == 2:
    pass_dictionary = fgen.string_to_list(digits + small_letters + large_letters)
elif argument.force_of_pass == 3:
    pass_dictionary = fgen.string_to_list(digits + small_letters + large_letters + special_signs)
else:
    parser.print_help()
    sys.exit(0)

if argument.password_length < 5 and argument.password_length > 60:
    parser.print_help()
    sys.exit(0)

for i in range(argument.passwords_quantity):
    fgen.password_generator(argument.password_length, pass_dictionary)
