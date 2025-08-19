import random
import string
import pyinputplus as Pyip

print('Welcome to The Ghost Analyst OSINT Password Generator v1')
print('Generate secure passwords for your accounts.\n')

# Full character set including punctuation
full_charset = string.ascii_letters + string.digits + string.punctuation

ask = Pyip.inputInt("How many passwords do you want to generate? ")
length = Pyip.inputInt("How long should each password be? ")

print('\nGenerating passwords...\n')
for i in range(1, ask + 1):
    password = ''.join(random.choices(full_charset, k=length))
    print(f"Password {i}: {password}")

