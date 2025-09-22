from unreliable_car import UnreliableCar

ITERATION_TIMES = 100

def main():
    unreliable_car_a = UnreliableCar("Car A", 200, 30)
    unreliable_car_b = UnreliableCar("Car B", 200, 60)
    drive_count_a = 0
    drive_count_b = 0
    for _ in range(ITERATION_TIMES):
        distance_driven_a = unreliable_car_a.drive(2)
        distance_driven_b = unreliable_car_a.drive(4)
        print(f"{unreliable_car_a.name} has driven {distance_driven_a} km")
        print(f"{unreliable_car_b.name} has driven {distance_driven_b} km")
        if distance_driven_a  != 0:
            drive_count_a += 1
        if distance_driven_b  != 0:
            drive_count_b += 1
    print(f"Total count: {ITERATION_TIMES}, Car A Drive count: {drive_count_a}")
    print(f"Total count: {ITERATION_TIMES}, Car A Drive count: {drive_count_b}")


main()