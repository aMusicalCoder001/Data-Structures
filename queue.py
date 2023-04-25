class QueueFromArray:
    def __init__(self, length):
        self.Q = [0]*length
        self.head = 0
        self.tail = 0
        self.length = length

    def enqueue(self, val):
        self.Q[self.tail] = val
        if self.tail == self.length - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        val = self.Q[self.head]
        self.Q[self.head] = 0
        if self.head == self.length - 1:
            self.head = 0
        else:
            self.head += 1
        return val

Q = QueueFromArray(6)
Q.enqueue(4)
Q.enqueue(1)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(8)
Q.dequeue()
print(Q.Q)
