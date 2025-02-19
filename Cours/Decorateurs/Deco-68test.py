from decorators10 import repeat

@repeat
def say_whee():
    print("Whee!")

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

say_whee()


greet("Penny")