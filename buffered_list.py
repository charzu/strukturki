class Lista:
    def __init__(self):
        self.value = []
        self.true_length = 0

    def __getitem__(self, item):
        return self.value[item]

    def __setitem__(self, key, value):
        if key < self.true_length:
            self.value[key] = value
        else:
            raise IndexError

    @staticmethod
    def empty(length):
        empty_list = [None for _ in range(length)]
        return empty_list

    def append(self, list_element):

        if self.true_length >= len(self.value):
            tmp_list = self.empty(self.true_length * 2 + 1)
            for ind, ele in enumerate(self.value):
                tmp_list[ind] = ele
            self.value = tmp_list
        self.value[self.true_length] = list_element
        self.true_length += 1

    def pop(self, *args):
        if len(args) == 0:
            del_item = self.value[self.true_length - 1]
        else:
            del_item = self.value[args[0]]
            for idx in range(args[0], self.true_length):
                self.value[idx] = self.value[idx + 1]

        self.value[self.true_length - 1] = None
        self.true_length -= 1
        if self.true_length < len(self.value) // 2:
            tmp_list = Lista.empty(self.true_length + 2)
            for ind in range(self.true_length):
                tmp_list[ind] = self.value[ind]
            self.value = tmp_list

        return del_item

    def extend(self, other):
        if self.true_length + other.true_length >= len(self.value):
            tmp_list = self.empty(self.true_length + len(other.value) + 1)
            for ind, ele in enumerate(self.value):
                tmp_list[ind] = ele
            self.value = tmp_list
        for ind, ele in enumerate(other.value):
            self.value[self.true_length + ind] = ele
        self.true_length += other.true_length

    def insert(self, gdzie, co):
        if self.true_length + 1 >= len(self.value):
            tmp_list = self.empty(self.true_length + 2)
            for ind, ele in enumerate(self.value):
                tmp_list[ind] = ele
            self.value = tmp_list

        tmp_list2 = self.empty(self.true_length + 4)
        for idx in range(0, gdzie + 1):
            if idx == gdzie:
                tmp_list2[idx] = co
                self.true_length += 1
            else:
                tmp_list2[idx] = self.value[idx]

        for idx in range(gdzie, self.true_length):
            tmp_list2[idx + 1] = self.value[idx]
        self.value = tmp_list2

    def reverse(self):
        for idx in range(0, self.true_length // 2):
            self.value[idx], self.value[self.true_length - idx - 1] = self.value[self.true_length - idx - 1], \
                                                                      self.value[idx]


lista1 = Lista()
lista1.append(9)
lista1.append(11)
lista1.append(12)
lista1.append(13)
lista1.append(14)
lista1.append(15)
# print(lista1[1])
# print(lista1.value)
lista1[1] = 3
# print(lista1.value)

lista2 = Lista()
lista2.append(2)
lista2.append(9)
lista2.append(7)
lista2.append(5)
print(f"lista1 value: {lista1.value}")
# print(f"lista1 true_length: {lista1.true_length}")
# print(f"lista2 value: {lista2.value}")
# print(f"lista2 true_length: {lista2.true_length}")
# print()

# lista1.extend(lista2)
# print('po extend:')
# print(f"lista1 value: {lista1.value}")
# print(f"lista1 true_length: {lista1.true_length}")
# print(f"lista2 value: {lista2.value}")
# print(f"lista2 true_length: {lista2.true_length}")
# print()

lista1.insert(2, 123)
# print('po insert: ')
print(f"lista1 value: {lista1.value}")
# print(f"lista1 true_length: {lista1.true_length}")
# print(f"lista2 value: {lista2.value}")
# print(f"lista2 true_length: {lista2.true_length}")

print(f"lista1 value: {lista1.value}")
lista1.reverse()
print('po reverse: ')
print(f"lista1 value: {lista1.value}")
# print(f"lista1 true_length: {lista1.true_length}")
