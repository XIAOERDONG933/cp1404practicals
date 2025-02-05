print("a. Count in steps of 10:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("\nb. Countdown:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("\nc. Stars:")
n = int(input("Number of stars: "))
for _ in range(n):
    print('*', end='')
print()

print("\nd. Increasing stars:")
n = int(input("Number of stars: "))
for i in range(1, n + 1):
    print('*' * i)