import string
import random

character = string.ascii_uppercase + string.ascii_letters + string.digits
password = ''

size = int(input('How many characters will your password have?: '))

for i in range(size):
    password += random.choice(character)

print(f'Your passaword is: {password}')
