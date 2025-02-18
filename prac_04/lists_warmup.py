numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 6, 5, 3]
"""
# 1. Change the first element of numbers to (the string, not the number "ten"10)
numbers[0] = "ten"
# 2. Change the last element of numbers to 1
numbers[-1] = "one"
# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# 4. Print whether is an element of numbers 9
print(9 in numbers)