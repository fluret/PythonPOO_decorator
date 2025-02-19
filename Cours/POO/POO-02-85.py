from stack import Stack

stack = Stack([1, 2, 3])
print(stack)
stack.push(4)
print(stack)
stack.pop()
stack.pop()
print(stack)

print(dir(stack))