"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user inputs a numerator or denominator that is not a valid integer.

2. When will a ZeroDivisionError occur?
When the denominator entered by the user is 0, it causes the calculation to be divided by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, and I have made the following changes to the code
"""

valid_input = False

while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator != 0:
            fraction = numerator / denominator
            print(fraction)
            valid_input = True
        else:
            print("Cannot divide by zero! Please enter new denominator.")

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

print("Finished.")