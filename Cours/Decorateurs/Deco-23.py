from decorators2 import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")