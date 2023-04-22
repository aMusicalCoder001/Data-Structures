class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()

S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.pop()
print(S.stack)
