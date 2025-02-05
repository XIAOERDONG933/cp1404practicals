"""
A program that asks the user for a password, with error-checking to repeat
if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
"""
MIN_PASSWORD_LENGTH = 6

def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        password = input(f"The password must be at least {MIN_PASSWORD_LENGTH} characters. Please enter again: ")
    return password


main()