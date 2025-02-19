import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    if num < 2:
        value = num
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    print(f"Calculated fibonacci({num}) = {value}")
    return value