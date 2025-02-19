from vehicles import Car, Motorcycle

tesla = Car("Tesla", "Model S", 2022, 5)
tesla.start()
tesla.drive()
tesla.stop()
print(tesla)
print('*'*20)
harley = Motorcycle("Harley-Davidson", "Iron 883", 2021, 2)
harley.start()
harley.ride()
harley.stop()
print(harley)