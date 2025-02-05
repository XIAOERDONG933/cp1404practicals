number_of_items = -1
while number_of_items < 0:
    try:
        number_of_items = int(input("Number of items: "))
        if number_of_items < 0:
            print("Invalid number of items!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

total_price = 0.0

for _ in range(number_of_items):
    while True:
        try:
            price = float(input("Price of item: "))
            if price < 0:
                print("Price cannot be negative!")
                continue
            total_price += price
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")