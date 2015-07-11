#Generates a random password of desired length with one special character and one number :)
#Author: Samir Khakimov
import random
import argparse
import os

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = ['!','@','#','$','%','&','*']

def generate(length):
  char_list = []
  ret = ''
  random.seed(os.urandom(random.randint(1,1000)))
  number = random.choice(numbers)
  special = random.choice(specials)
  char_list.append(number)
  char_list.append(special)

  for i in xrange(length-2):
    char =  random.choice(letters)
    upper = random.randint(0,1)
    if upper == True:
      char_list.append(char.upper())
    else:
      char_list.append(char)

  random.shuffle(char_list)
  for item in char_list:
    ret+=item
  
  return ret

def main():
  parser = argparse.ArgumentParser(description = 'Password Generator', usage ='python rand_password.py -l length')
  parser.add_argument('-l','--length', help='provide desired password length', type =int, required = True)

  args = parser.parse_args()
  print generate(args.length)

if __name__== "__main__":
  main()