"""
Create and copy in only your function from above. Now write a main program that uses this function:more_scores.pyscore.py
-Ask the user for a number of scores
-Generate that many random numbers (scores) between 0 and 100 inclusive
-For each of those scores, write the "result" to a file called as below:results.txt
"""
import random

def main():
    count = int(input("Please enter the number of scores: "))

    file = open("results.txt", "w")
    while count > 0:
        # Generate a random score between 0 and 100 (inclusive)
        random_score = random.randint(0,100)
        status = determine_score(random_score)
        file.writelines(f"{random_score} is {status}\n")
        count -= 1
    file.close()


def determine_score(score):
    """Determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()