from sample_dict import SampleClass
instance = SampleClass("Hello!")

print(instance.instance_attr)
print('*'*20)
instance.method()
print('*'*20)
print(instance.__dict__)
print('*'*20)
print(instance.__dict__["instance_attr"])
print('*'*20)
print(instance.instance_attr)