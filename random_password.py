# Generates a random password of desired length with special characters,
# letters and numbers.  Ensures there's at least one special character,
# one lowercase, one uppercase and one number in the password.

# Author: Samir Khakimov

import random
import argparse
import os
import string

# List of numbers 0 - 9
numbers = map(str, range(0, 10))
# List of all lowercase characters
lower = list(string.lowercase)
# List of all uppercase characters
upper = list(string.uppercase)
# List of special characters
specials = ['!', '@', '#', '$', '%', '&', '*']


def generate(pswd_length):
    pswd_set = set()
    random.seed(os.urandom(random.randint(1, 1000)))

    # Check there's at least one number, lower, upper and special
    while not (pswd_set & set(numbers) and pswd_set & set(lower) and
               pswd_set & set(upper) and pswd_set & set(specials)):
        pswd_list = []
        for i in xrange(pswd_length):
            pswd_char = random.choice(numbers+lower+specials+upper)
            pswd_list.append(pswd_char)
        pswd_set = set(pswd_list)

    random.shuffle(pswd_list)

    return ''.join(pswd_list)


def main():
    parser = argparse.ArgumentParser(description='Password Generator',
                                     usage='python rand_password.py -l length')
    parser.add_argument('-l', '--length',
                        help='provide desired password length', type=int,
                        required=True)

    args = parser.parse_args()
    print generate(args.length)

if __name__ == "__main__":
    main()
