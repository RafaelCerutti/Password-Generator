import string
import random

def passwordGenerator():
    character = string.ascii_uppercase + string.ascii_letters + string.digits
    password = ''

    size = int(input('How many characters will your password have?: '))
    for i in range(size):
        password += random.choice(character)

    return password

while True:
    password = passwordGenerator()
    print(password)
    choice = int(input('Enter 1 for a new password or enter 0 to finish: '))

    if choice == 0:
        print('Program finished')
        break

