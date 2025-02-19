class ObjectCounter:
    num_instances = 0
    def __init__(self):
        self.num_instances += 1

print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter())
print('*'*20)
print(ObjectCounter.num_instances)