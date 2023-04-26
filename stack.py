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

class StackFromArray():
    def __init__(self, n):
        self.stack = [0]*n
        self.top = 0

    def is_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, val):
        self.stack[self.top] = val
        self.top += 1

    def pop(self):
        self.top -= 1
        self.stack[self.top] = 0
        return self.stack[self.top+1]

S = StackFromArray(6)
S.push(4)
S.push(1)
S.push(3)
S.pop()
S.push(8)
S.pop()
print(S.stack)

class QfromStack():
    def __init__(self, length):
        self.array = [0]*length
        self.stack1 = StackFromArray(length)
        self.stack2 = StackFromArray(length)
        self.stack2.top = length *-1 + 1
        self.head = 0
        self.length = length

    def enqueue(self, val):
        self.stack1.push(val)
        self.array = self.stack1.stack
        if self.stack1.top == self.length:
            self.stack1.top = 0

    def dequeue(self):
        self.stack2.stack = self.array
        self.stack2.pop()
        self.stack2.top += 2
        self.array = self.stack2.stack

Q = QfromStack(6)
Q.enqueue(4)
Q.enqueue(1)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(8)
Q.dequeue()
print(Q.array)
