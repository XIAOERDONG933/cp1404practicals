"""This module implements a password checking program.
It prompts the user to enter a password to verify if it meets the minimum length requirement,
and then display a series of asterisks corresponding to the password length."""

PASSWORD_LENGTH = 10

def main():
    """Obtain password, verify length, and display corresponding asterisk."""
    password = get_password()
    while len(password) < PASSWORD_LENGTH:
        print(f'Password must be at least {PASSWORD_LENGTH} characters long.')
        password = input('Enter a password: ')
    show_stars(password)

def show_stars(password):
    """Display asterisks indicating the corresponding number of passwords."""
    print("*" * len(password))

def get_password():
    """Retrieve the password entered by the user."""
    password = input(f'Enter a password (at least {PASSWORD_LENGTH} characters): ')
    return password

main()