from decorators11 import count_calls

@count_calls
def say_whee():
    print("Whee!")


say_whee()

say_whee()

print(say_whee.num_calls)