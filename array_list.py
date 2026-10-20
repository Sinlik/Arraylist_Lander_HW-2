from abstract_list import AbstractList

# in the __init__ part of array_list.py, 

class ArrayList(AbstractList):
    def __init__(self):
        self._data = [None] * 100
        self._size = 0

    def add(self, element):
        if (self._size > 100):
            return OverflowError 
        i = self._size
        self._data[i] = element
        self._size += 1
        return element 

    def remove(self, index):
        temp = self._data[index]
        if (index + 1 == self._size):
            self._data[index] = None
        else:
            for i in range(self._size - (index - 1)):
                self._data[index + i] = self._data[index + (i + 1)]
            self._data[self._size - 1] = None
        self._size -= 1
        return temp

    def get(self, index):
        if index > self._size - 1:
            return IndexError
        return self._data[index]

    def set(self, index, element):
        self._data[index] = element

    def getIndex(self, element):
        for i in range(self._size):
            if self._data[i] == element:
                return i
        return -1

    def size(self):
        return self._size