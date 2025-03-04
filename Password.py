#  EHsan

import random
print('''
================================
      Password Generator 
================================
''')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=<>?:"|\';[].,/~`0123456789'

number = int(input('Number of Passwords??'))
length = int(input('paswword length ?'))

print('thats your passwords')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
