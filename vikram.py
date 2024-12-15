
import random
import string

def generate_password(length=12):
    # Define the character pool
    char_pool = string.ascii_letters + string.digits + string.punctuation

    # Ensure password contains at least one of each type
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),          # At least one digit
        random.choice(string.punctuation)      # At least one special character
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(char_pool, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Generate and print a random password
print("Your random password is:", generate_password(16))
