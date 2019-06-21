import random

random.seed(1234)


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

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.value, end=' ')
        if self.right is not None:
            self.right.print()

    def check_availability(self, num):
        _next = self
        while _next is not None:
            current = _next
            if num < current.value:
                _next = current.left
            else:
                _next = current.right

            if current.value == num:
                return True
        return False

    def create_tree(self, num_of_elements):
        for num in range(num_of_elements):
            tmp_rnd = random.randint(0, 20)
            self.append(tmp_rnd)

    def max_num_of_nods(self, tmp_num=0, max_num=0):
        tmp_num += 1
        if tmp_num > max_num:
            max_num = tmp_num
        if self.left is not None:
            max_num = self.left.max_num_of_nods(tmp_num, max_num)
        if self.right is not None:
            max_num = self.right.max_num_of_nods(tmp_num, max_num)

        return max_num

    # def remove(self):

    # TODO: remove, usunięcie elementu i dopisanie do jednej galezi innej
    # TODO: drzewo do ktorego dodaje sie wyraz przez co drzewo sie rozgalezia


root = BinaryTree(5)

root.create_tree(11)
root.print()
print()
print(root.check_availability(4))
print(root.max_num_of_nods())
