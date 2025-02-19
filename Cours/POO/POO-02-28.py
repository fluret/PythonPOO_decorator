class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(4, 8)
print(point.__dict__)