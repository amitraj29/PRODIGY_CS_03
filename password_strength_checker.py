import string
import random
import math

def calculate_entropy(password):
    charset_size = 0
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)

    entropy = len(password) * math.log2(charset_size)
    return entropy

def time_to_crack(entropy):
    guesses_per_second = 1e9  # 1 billion guesses per second
    seconds = 2 ** entropy / guesses_per_second
    years = seconds / (60 * 60 * 24 * 365)
    return years

def assess_password(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    # Adjusted criteria for strength assessment
    strength = "Weak"
    if length >= 16 and criteria_met >= 3:
        strength = "Strong"
    elif length >= 12 and criteria_met >= 3:
        strength = "Moderate"
    elif length >= 8 and criteria_met >= 2:
        strength = "Weak"

    entropy = calculate_entropy(password)
    years_to_crack = time_to_crack(entropy)

    return strength, years_to_crack

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password = input("Enter a password to assess: ")

    strength, years_to_crack = assess_password(password)
    print(f"Password strength: {strength}")
    print(f"Estimated time to crack: {years_to_crack:.2f} years")

    if strength == "Weak" or years_to_crack < 1:
        print("The password is weak. Generating a stronger password for you:")
        recommended_password = generate_strong_password()
        print(f"Recommended stronger password: {recommended_password}")

if __name__ == "__main__":
    main()