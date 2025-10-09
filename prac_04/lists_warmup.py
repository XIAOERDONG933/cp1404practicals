numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# numbers[0]            answer: 3
# numbers[-1]           answer: 2
# numbers[3]            answer: 1
# numbers[:-1]          answer: [3, 1, 4, 1, 5, 9]
# numbers[3:4]          answer: [1]
# 5 in numbers          answer: True
# 7 in numbers          answer: False
# "3" in numbers        answer: False
# numbers + [6, 5, 3]   answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)