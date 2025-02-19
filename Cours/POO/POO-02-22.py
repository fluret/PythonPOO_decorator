class User:
    pass

# Add instance attributes dynamically
jane = User()
jane.name = "Jane Doe"
jane.job = "Data Engineer"
print(jane.__dict__)
{'name': 'Jane Doe', 'job': 'Data Engineer'}

# Add methods dynamically
def __init__(self, name, job):
    self.name = name
    self.job = job

User.__init__ = __init__

print(User.__dict__)

linda = User("Linda Smith", "Team Lead")
print(linda.__dict__)
{'name': 'Linda Smith', 'job': 'Team Lead'}