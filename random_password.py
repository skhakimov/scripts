#Generates a random password of desired length with one special char and one number
import random
import argparse
import os

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = ['!','@','#','$','%','&','*']

def generate(length):
  list = []
  ret = ''
  random.seed(os.urandom(random.randint(1,1000)))
  number = random.choice(numbers)
  list.append(number)
  special = random.choice(specials)
  list.append(special)

  for i in xrange(length-2):
    char =  random.choice(letters)
    upper = random.randint(0,1)
    if upper == True:
      list.append(char.upper())
    else:
      list.append(char)

  random.shuffle(list)
  for item in list:
    ret+=item
  
  return ret

def main():
  parser = argparse.ArgumentParser(description = 'Password Generator', usage ='python rand_password.py -l length')
  parser.add_argument('-l','--length', help='provide desired password length', type =int, required = True)
 
  args = parser.parse_args()
  print generate(args.length)

if __name__== "__main__":
  main()
