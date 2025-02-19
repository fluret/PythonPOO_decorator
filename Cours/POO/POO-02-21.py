from record import Record

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

john_record = Record()

for field, value in john.items():
    setattr(john_record, field, value)

print(john_record.name)
print(john_record.department)
print('*' * 20)
print(john_record.__dict__)