from silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Fancy",100,2)
fancy_taxi.drive(18)
fare= fancy_taxi.get_fare()
print(f"{fancy_taxi}")
print(f"Fare for 18km trip:${fare:.2f}")
assert fare ==48.8, f"Expected fare to be 48.78 but got {fare:.2f}"