from mixins import Employee

john = Employee("John Doe", 30, 50000)
print(john.to_json())
print(john.to_pickle())