LOOP_TIMES = 5

numbers = []
for _ in range(LOOP_TIMES):
    num = int(input("Number: "))
    numbers.append(num)

print(f"The first number is {numbers[0]}.")
print(f"The last number is {numbers[-1]}.")
print(f"The smallest number is {min(numbers)}.")
print(f"The largest number is {max(numbers)}.")
print(f"The average number is {sum(numbers)/len(numbers)}.")
