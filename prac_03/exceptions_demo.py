"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either numberator or denominator is not an integer value.

2. When will a ZeroDivisionError occur?
When the entered denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Just pre-check the value of denominator, make sure it is not zero before the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The denominator cannot be 0")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")