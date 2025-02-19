from decorators import use_unit

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration

bolt = average_speed(100, 9.58)
print(bolt)

print(bolt.to("km per hour"))

print(bolt.to("mph").m)