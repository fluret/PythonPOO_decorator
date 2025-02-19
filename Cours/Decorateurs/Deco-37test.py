from decorators6 import debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"

result = make_greeting("Benjamin")
print(result)
print('*'*20)
result = make_greeting("Juan", age=114)
print(result)
print('*'*20)
result = make_greeting(name="Maria", age=116)
print(result)