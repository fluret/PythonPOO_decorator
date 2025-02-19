from decorators14 import singleton

@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

print(id(first_one))

print(id(another_one))

print(first_one is another_one)