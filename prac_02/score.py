import random

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    print(determine_grade(user_score))
    print("\nRandom score test:")
    random_score = random.uniform(-20, 120)
    print(f"Score: {random_score:.2f} → {determine_grade(random_score)}")

if __name__ == "__main__":
    main()