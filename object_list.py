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
            print(current.value)
            current = current.next

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

    def __setitem__(self, key, value):
        #TODO - Ser item ma ustawiać podaną wartość na istniejącym elemencie o podanym indeksie
        pass

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
        # TODO - deletes last item if no args or deletes strict element with given arg
        pass

    def remove(self, value):
        # TODO - deletes first element that value is given
        pass


element1 = LinkedList(6)
element2 = element1.set_next(3)
element3 = element2.set_next(1)
element4 = element3.set_next(9)

# element1.print_elements()
element1.append(11)
# element1.print_elements()

# element1[2]
element1.insert(0, 111)
element1.print_elements()
# element1.next = element2
element1.insert
# print(dir(element1))
# print(element1.value)
# print(element1.next.value)
# print(element1.next.next.next.value)
