class Que:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list.__len__() == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.list[0]

    def push(self, data):
        self.list.append(data)

que = Que()

print(que.pop())
print(que.peek())
que.push(3)
que.push(5)
que.push(23)
que.push("123")
print(que.pop())
print(que.peek())
print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())

