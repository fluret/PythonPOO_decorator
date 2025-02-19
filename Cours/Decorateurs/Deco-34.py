from decorators5 import timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


waste_some_time(1)

waste_some_time(999)