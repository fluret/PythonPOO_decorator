from shapes import Circle, Square

circle = Circle(100)
print(circle.radius)
print('*'*20)
circle.radius = 500
print(circle.radius)
print('*'*20)
#circle.radius = 0
print('*'*20)
square = Square(200)
print(square.side)
print('*'*20)
square.side = 300
print(square.side)
print('*'*20)
square = Square(-100)
