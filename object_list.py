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

    def append(self, arg):
        current = self
        while current.next is not None:
            current = current.next
        current.set_next(arg)

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
            for idx in range(loc-1):
                current = current.next
            tmp_next = current.next
            current.set_next(arg)
            current.next.next = tmp_next

    def pop(self, *args):
        current = self
        deleted_item = None
        if len(args) == 0:
            current = self
            while current.next.next is not None:
                current = current.next
                if current.next.next is None:
                    deleted_item = current.next.value
            current.next = None
            return deleted_item

        # elif args[0] == 0:
        #     tmp_next = self.next
        #     self = tmp_next
        else:
            for idx in range(args[0]-1):
                current = current.next
            current.next = current.next.next

    def remove(self, arg):
        current = self
        while current.next.value != arg:
            current = current.next
            if current.next.next is None:
                raise ValueError('Wrong argument, none elements value equals argument')
        current.next = current.next.next


element1 = LinkedList(6)
element2 = element1.set_next(3)
element3 = element2.set_next(1)
element4 = element3.set_next(9)

# element1.print_elements()
element1.append(11)
# element1.print_elements()

# element1[2]
element1.insert(2, 111)
# element1.print_elements()
# element1.next = element2
element1. __setitem__(2, 1233)
# element1.insert
# print(dir(element1))
element1.print_elements()
print(f"deleted item: {element1.pop()}")
print(f"deleted item: {element1.pop()}")
print(f"deleted item: {element1.pop()}")
# element1.remove(3)
element1.print_elements()
# print(element1.next.value)
# print(element1.next.next.next.value)
