from silver_service_taxi import SilverServiceTaxi

def main():
    sst = SilverServiceTaxi("Toyota", 100, 2)
    sst.drive(18)
    assert sst.get_fare() == 48.78, "The fare should be 48.78"
    print(f"You got it! Current fare is {sst.get_fare()}")

    benz = SilverServiceTaxi("Benz", 300, 5)
    benz.drive(20)
    assert benz.get_fare() == 127.5, "The fare should be 127.5"
    print(f"You got it! Current fare is {benz.get_fare()}")

main()