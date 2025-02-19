from decorators8 import register, PLUGINS

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"