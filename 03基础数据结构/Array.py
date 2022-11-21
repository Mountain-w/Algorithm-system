import numpy as np


class Array:
    def __init__(self, capacity=10):
        self._data = np.array([0] * capacity)
        self._size = 0

    def add_last(self, item):
        """
        在所有元素后添加新元素
        :param item: 新元素
        :return: None
        """
        self.add(item, self._size)

    def add_first(self, item):
        self.add(item, 0)

    def add(self, item, index):
        """
        在数组中index位置插入元素
        :param item: 新元素
        :param index: 要插入的位置
        :return:
        """
        if index < 0 or index > self._size:
            raise RuntimeError("The index out of range")
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        for i in range(self._size, index - 1, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def remove(self, index):
        """
        删除index位置的元素并返回
        :param index:
        :return:
        """
        if index < 0 or index >= self._size:
            raise RuntimeError("The index out of range")
        ret = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self.resize(len(self._data) // 2)
        return ret

    def remove_frist(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, element):
        index = self.find(element)
        if index != -1:
            self.remove(index)

    def find(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def __contains__(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True
        return False

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def __getitem__(self, item):
        if item < 0 or item > self._size:
            raise IndexError("Index out of range")
        return self._data[item]

    def __setitem__(self, key, value):
        if key < 0 or key > self._size:
            raise IndexError("Index out of range")
        self._data[key] = value

    def __str__(self):
        string = [f"<Array size={self._size} capacity={self.get_capacity()}>\n", "["]
        for i in range(self._size):
            string.append(f"{self._data[i]}")
            if i != self._size - 1:
                string.append(",")
        string.append("]")
        return "".join(string)

    def resize(self, new_capacity):
        new_data = np.array([0] * new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data


if __name__ == '__main__':
    arr = Array()
    for i in range(10):
        arr.add_last(i)
    print(arr)
    arr.add_last(1)
    print(arr)
    arr.remove_last()
    arr.remove_last()
    arr.remove_last()
    arr.remove_last()
    print(arr)
