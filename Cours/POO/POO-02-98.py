from vehicles2 import Car, Motorcycle

toyota = Car("Toyota", "Corolla", 2022, 5)
honda = Car("Honda", "Civic", 2022, 4)
harley = Motorcycle("Harley-Davidson", "Iron 883", 2022, 2)
indian = Motorcycle("Indian", "Scout", 2022, 2)

for vehicle in [toyota, honda, harley, indian]:
    vehicle.drive()