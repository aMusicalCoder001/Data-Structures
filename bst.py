class node:
    def __init__(self, val):
        self.val = val
        self.p = None
        self.l = None
        self.r = None

class binary_tree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.r != None:
            x = x.r
        return x

    def minimum(self, x):
        while x.l != None:
            x = x.l
        return x

    def search(self, value):
        x = self.root
        while x != None:
            if value > x.val:
                x = x.r
            elif value < x.val:
                x = x.l
            else:
                return x

    def delete(self, z):
        z = self.search(z)
        if z.l == None:
            self.transplant(z, z.r)
        elif z.r == None:
            self.transplant(z, z.l)
        else:
            y = minimum(z.r)
            if y.p != z:
                transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            transplant(z, y)
            y.l = z.l
            y.l.p = y

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else:
            u.p.r = v

        if v != None:
            v.p = u.p

    def insert(self, z):
        y = None
        x = self.root

        while x != None:
            y = x
            if z.val < x.val:
                x = x.l
            else:
                x = x.r

        z.p = y
        if y == None:
            self.root = z
        elif z.val < y.val:
            y.l = z
        else:
            y.r = z
        

bst = binary_tree()
bst.insert(node(1))
bst.insert(node(2))
bst.insert(node(3))
bst.delete(1)
print(bst.minimum(bst.root).val)
