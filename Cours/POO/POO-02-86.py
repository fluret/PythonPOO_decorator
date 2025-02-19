class Stack(list):
    def push(self, item):
        self.append(item)
    def pop(self):
        return super().pop()
    def __repr__(self) -> str:
        return f"{type(self).__name__}({super().__repr__()})"


stack = Stack()
print(dir(stack))