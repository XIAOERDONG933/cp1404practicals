"""
A program that asks the user for a password, with error-checking to repeat
if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
"""
password = input("Enter a password: ")
MIN_PASSWORD_LENGTH = 6
while len(password) < MIN_PASSWORD_LENGTH:
    password = input(f"The password must be at least {MIN_PASSWORD_LENGTH} characters. Please enter again: ")
print("*" * len(password))