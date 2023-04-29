class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        node = Node(x)
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
        node.prev = None

    def search(self, value):
        x = self.head
        while x != None and x.val != value:
            print(x.val)
            x = x.next
        return x

    def delete(self, value):
        x = self.search(value)
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

dll = DoublyLinkedList()
dll.insert(8)
dll.insert(7)
dll.insert(6)
dll.delete(8)
dll.search(8)
