>>> from circle import Circle

>>> c = Circle(5)
>>> c.radius
5

>>> c.area
78.5398163375

>>> c.radius = 2
>>> c.area
12.566370614

>>> c.area = 100
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

>>> c.cylinder_volume(height=4)
50.265482456

>>> c.radius = -1
Traceback (most recent call last):
    ...
ValueError: radius must be non-negative

>>> c = Circle.unit_circle()
>>> c.radius
1

>>> c.pi()
3.1415926535

>>> Circle.pi()
3.1415926535
