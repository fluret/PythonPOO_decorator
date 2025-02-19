from decorators8 import debug, do_twice

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")


greet("Yadi")