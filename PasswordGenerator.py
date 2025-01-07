#Password Generator Developed by Kirklen Allen

import random
import string

#Character Pool (The program will use these characters to generate its passwords)
uppercase_letters = string.ascii_uppercase # A-Z
lowercase_letters = string.ascii_lowercase # a-z
digits = string.digits # 0-9
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_characters):
    character_pool= ""
    if use_uppercase:
        character_pool += uppercase_letters # in Python, the += operator is a shorthand for adding and assigning a value to a variable
    if use_lowercase:
        character_pool += lowercase_letters
    if use_digits:
        character_pool += digits
    if use_special_characters:
        character_pool += special_characters

    if not character_pool:
        return "No valid characters were entered. Try again :D."

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("Welcome to Password Generator Developed by Kirklen Allen")

    try:
        length = int(input("How long would you like your password to be? "))
        use_uppercase = input("Include uppercase letters? (y/n) ").strip().lower() == "yes"
        use_lowercase = input("Include lowercase letters? (y/n) ").strip().lower() == "yes"
        use_digits = input("Include digits? (y/n) ").strip().lower() == "yes"
        use_special_characters = input("Include special characters? (y/n) ").strip().lower() == "yes"
        num_passwords = int(input("How many passwords would you like to generate? "))


        print("\nGenerating password(s)...")
        for i in range(num_passwords):
            print(generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_characters))

    except ValueError:
        print("Error: Please enter valid numbers for length and count.")

if __name__ == "__main__":
    main()