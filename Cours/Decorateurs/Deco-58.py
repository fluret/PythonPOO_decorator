from decorators8 import repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet("World")