import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# This program uses the randint() function of the random module.
# This will generate a random integer between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, and the largest number is 20

# What did you see on line 2?
# This program uses the randrange() function of the random module.
# This will generate a random integer within the range of [3,5,7,9].
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest number is 9
# Could line 2 have produced a 4?
# No, because the step is 2.

# What did you see on line 3?
# This program uses the uniform() function of the random module. This produces a random float between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, and the largest number is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))