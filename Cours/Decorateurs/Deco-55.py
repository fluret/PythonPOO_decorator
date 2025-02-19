from decorators8 import debug, do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")