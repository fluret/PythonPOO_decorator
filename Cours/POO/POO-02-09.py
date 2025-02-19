class ObjectCounter:
    num_instances = 0
    def __init__(self):
        ObjectCounter.num_instances += 1


print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter.num_instances)
print('*'*20)
counter = ObjectCounter()
print(counter.num_instances)

