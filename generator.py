import random
import string

print("Welcome to the Password Generator!")

while True:
    try:
        length = int(input("Enter the password length: "))
        break
    except ValueError:
        print("❌ Please enter a valid number for the password length.")

include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = ""

if include_letters:
    characters += string.ascii_letters
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

if not characters:
    print("Error: You must select at least one character type!")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))
print(f"\nGenerated Password: {password}")
