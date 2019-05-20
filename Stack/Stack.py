class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list.__len__() == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.list[-1]

    def push(self, data):
        self.list.append(data)

stack = Stack()

stack.pop()
print(stack.peek())
stack.push(1)
stack.push(2)
stack.push("123")
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())

