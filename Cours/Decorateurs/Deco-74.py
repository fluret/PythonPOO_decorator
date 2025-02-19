from decorators12 import CountCalls

@CountCalls
def say_whee():
    print("Whee!")

say_whee()
say_whee()
print(say_whee.num_calls)