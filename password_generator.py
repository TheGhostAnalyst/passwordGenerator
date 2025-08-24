import random
import string
import pyinputplus as Pyip
from pathlib import Path
from datetime import datetime

print('Welcome to The Ghost Analyst OSINT Password Generator v1')
print('Generate secure passwords for your accounts.\n')

# Full character set including punctuation
full_charset = string.ascii_letters + string.digits + string.punctuation

try:
    ask = Pyip.inputInt("How many passwords do you want to generate? ")
    length = Pyip.inputInt("How long should each password be? ")

    print('\nGenerating passwords...\n')
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    
    with open('generated_passwords.txt', 'a') as f:
        f.write(f"\n{timestamp}\n#################################\n")
        
        for i in range(1, ask + 1):
            password = ''.join(random.choices(full_charset, k=length))
            given_pass = f"Password {i}: {password}"
            print(given_pass)
            f.write(given_pass + '\n')

    the_path = Path('generated_passwords.txt').resolve()
    print(f"\nAll passwords have been saved to {the_path}.")

except KeyboardInterrupt:
    print('\nProcess interrupted. Exiting...')
