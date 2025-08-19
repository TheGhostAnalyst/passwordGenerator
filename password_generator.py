import random
import string

# Welcome message
print('Welcome to The Ghost Analyst OSINT Password Generator v1')
print('Generate secure passwords for your accounts.\n')

# Full character set
full_charset = string.ascii_letters + string.digits + string.punctuation

try:
    ask = int(input("How many passwords do you want to generate? "))
    length = int(input("How long should each password be? "))

    print('\nGenerating passwords...\n')
    for i in range(1, ask + 1):
        password = ''.join(random.choices(full_charset, k=length))
        print(f"Password {i}: {password}")
except ValueError:
    print("Please enter valid numeric values for both inputs.")
