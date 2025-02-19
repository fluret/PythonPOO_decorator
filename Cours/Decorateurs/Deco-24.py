from decorators2 import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"