#  EHsan

import random
print('''
================================
      Password Generator 
================================
''')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=<>?:"|\';[].,/~`0123456789'

while True:
    try :
        number = int(input('''
        =======================================
            How many password do you want ? 
        =======================================
        '''))
        break
    except  ValueError : 
        print('''
        ===============================================
            ===> you have to enter int not str <=== 
        ===============================================
        ''')
   
while True:
    try : 
        length = int(input('''
        ============================================
            How long do you want your password ? 
        ============================================
        '''))
        break
    except ValueError :
        print('''
        ==============================================
           ===> you have to enter int not str <===
        ==============================================
        ''')
    
print()
print('''
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        Here are your passwords :
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    ''')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)