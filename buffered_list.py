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
        self.true_length += len(other.value)

    def insert(self, gdzie, co):
        #TODO
        pass

    def reverse(self):
        #TODO
        pass

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
print(lista1.value)

lista2 = Lista()
lista2.append(2)
lista2.append(9)
lista2.append(7)
lista2.append(5)
print(lista2.value)

lista1.extend(lista2)
print(lista1.value)
