from silver_service_taxi import SilverServiceTaxi

def main():
    sst = SilverServiceTaxi("Toyota", 100, 2)
    sst.drive(18)
    assert sst.get_fare() == 48.80, "The fare should be 48.80"
    print(f"You got it! Current fare is {sst.get_fare():.2f}")

    benz = SilverServiceTaxi("Benz", 300, 5)
    benz.drive(17)
    assert benz.get_fare() == 109.10, "The fare should be 109.10"
    print(f"You got it! Current fare is {benz.get_fare():.2f}")

main()