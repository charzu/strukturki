class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, arg):
        tmp_element = LinkedList(arg)
        self.next = tmp_element
        return tmp_element

    def print_elements(self):
        current = self
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()

    def __len__(self):
        current = self
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, arg):
        current = self
        while current.next is not None:
            current = current.next
        current.set_next(arg)

    def _operators(self, tool, arg):
        current = self
        while current.next is not None:
            current = current.next
            current.value = getattr(current.value, tool)(arg)

    def __add__(self, arg):
        if type(arg) is not LinkedList:
            self._operators('__add__', arg)
        else:
            current = self
            while current.next is not None:
                current = current.next
            current.next = arg

    def __sub__(self, arg):
        self._operators('__sub__', arg)

    def __mul__(self, arg):
        self._operators('__mul__', arg)

    def __truediv__(self, arg):
        self._operators('__truediv__', arg)

    def __pow__(self, arg):
        self._operators('__pow__', arg)

    def __getitem__(self, item):
        current = self
        for idx in range(item):
            current = current.next
        return current.value

    def __setitem__(self, loc, arg):
        current = self
        for idx in range(loc):
            current = current.next
        current.value = arg

    def insert(self, loc, arg):
        if loc == 0:
            tmp_next = self.next
            self.set_next(self.value)
            self.next.next = tmp_next
            self.value = arg
        else:
            current = self
            for idx in range(loc - 1):
                current = current.next
            tmp_next = current.next
            current.set_next(arg)
            current.next.next = tmp_next

    def pop(self, *args):
        current = self
        if len(args) == 0:
            current = self
            while current.next.next is not None:
                current = current.next
            deleted_item = current.next.value
            current.next = None
            return deleted_item

        else:
            for idx in range(args[0] - 1):
                current = current.next
            deleted_item = current.next.value
            current.next = current.next.next
            return deleted_item

    def remove(self, arg):
        current = self
        while current.next.value != arg:
            current = current.next
            if current.next is None:
                raise ValueError('Wrong argument, none elements value equals argument')
        current.next = current.next.next


element1 = LinkedList(6)
# element1.print_elements()
element1.append(11)
element1.append(111)
element1.append(1111)
element1.append(11222)
element1.append(112222)
# element1.print_elements()
list2 = LinkedList(3)
list2.append(23)
list2.append(231)
list2.append(2312)
list2.append(23122)
list2.append(2311)
# element1[2]
element1.insert(2, 111)
# element1.print_elements()
# element1.next = element2
element1.__setitem__(2, 1233)
# element1.insert
# print(dir(element1))
element1.print_elements()
list2.print_elements()
# print(f"deleted item: {element1.pop()}")
# print(f"deleted item: {element1.pop()}")
# print(f"deleted item: {element1.pop()}")
# print(f"deleted item: {element1.pop(2)}")
element1.remove(11)
element1.__add__(list2)
element1.print_elements()
element1.__add__(3)
element1.print_elements()
# element1.__sub__(6)
# element1.print_elements()
# element1.__mul__(6)
# element1.print_elements()
# element1.__pow__(2)
# element1.print_elements()
# element1.__truediv__(6)
# element1.print_elements()
print(element1.__len__())
