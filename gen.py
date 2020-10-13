#here we are using a function that shuffles all the characters of th string we use which is the basis of our password

import random
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#main part of the code 

uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punctuationSign1=chr(random.randint(128,191))
punctuationSign2=chr(random.randint(128,191))

#password becomes a variable that shuffles all the characters in a random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2

#the output it gives us
print(password)
#created by £ocsta#9101 