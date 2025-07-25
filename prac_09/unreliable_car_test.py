from unreliable_car import UnreliableCar

successful_drives=0
unreliable_car = UnreliableCar('Toro', 100,30)

for i in range(100):
    result = unreliable_car.drive(1)
    if result >0:
        successful_drives += 1
print(f"Successful drives: {successful_drives}/100")