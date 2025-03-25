import random
import string

def generate_password(length, include_symbols, include_numbers, include_uppercase):
    characters = string.ascii_lowercase
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = int(input("Enter the desired password length: "))
include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'

password = generate_password(length, include_symbols, include_numbers, include_uppercase)
print("Generated password:", password)
