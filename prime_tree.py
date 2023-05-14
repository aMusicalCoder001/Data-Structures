#An algorithm that finds prime numbers using a binary tree written by Jason Wu
class node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class prime_tree:
    def __init__(self):
        self.root = node(2)

    def insert(self, v):
        y = None
        x = self.root
        
        while x != None:
            y = x
            if v.val % x.val != 0:
                x = x.left
            else:
                x = x.right
        
        v.parent = y
        if v.val % y.val != 0:
            y.left = v
        else:
            y.right = v

    def get_all_primes(self):
        x = self.root
        answer = []
        while x != None:
            answer.append(x.val)
            x = x.left
        return answer

pt = prime_tree()
for i in range(2, 101):
    pt.insert(node(i))

primes = pt.get_all_primes()
print(primes)
        
        
