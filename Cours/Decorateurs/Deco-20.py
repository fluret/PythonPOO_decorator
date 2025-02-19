from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")