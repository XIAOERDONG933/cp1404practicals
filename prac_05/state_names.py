"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

MAX_CODE_LENGTH = max([len(code) for code in CODE_TO_NAME.keys()])
# prints all the states and names neatly lined up with string formatting
for code, name in CODE_TO_NAME.items():
    print(f"{code:{MAX_CODE_LENGTH}} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    """ LBYL version"""
    # if state_code in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")
    # state_code = input("Enter short state: ").upper()

    """ EAFP version"""
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
