from decorators4 import do_twice

@do_twice
def say_whee():
    print("Whee!")

print(say_whee)

print(say_whee.__name__)

help(say_whee)