import random

NUMBERS_PER_LINE = 6
MIN_RANGE = 1
MAX_RANGE = 45

pick_round = int(input("How many quick picks? "))
for _ in range(pick_round):
    ith_round = 0
    random_numbers = []
    while ith_round <= NUMBERS_PER_LINE:
        random_number = random.randint(MIN_RANGE, MAX_RANGE)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
            ith_round += 1
    print(" ".join([f"{number:2}" for number in sorted(random_numbers)]))