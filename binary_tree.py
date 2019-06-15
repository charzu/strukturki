class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def make_node(self, value):
        tmp = BinaryTree(value)
        return tmp

    def setnext(self, other):
        if other.value < self.value:
            self.left = other
        else:
            self.right = other

    def append(self, value):
        tmp = BinaryTree(value)
        _next = self
        while _next is not None:
            current = _next
            if tmp.value < current.value:
                _next = current.left
            else:
                _next = current.right
        current.setnext(tmp)


root = BinaryTree(5)

root.append(3)
print(root.left, root.right, root.value)
print(root.left.value)
root.append(7)
root.append(6)
print()
