from Utils.Queue import Queue


class Deque(Queue):
    def __init__(self, capacity=10):
        self._data = [0] * capacity
        self.front = self.tail = self.size = 0

    def enqueue(self, element):
        if self.is_full():
            self.__resize(len(self._data) * 2)
        self._data[self.tail] = element
        self.tail = (self.tail + 1) % len(self._data)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        ret = self._data[self.front]
        self._data[self.front] = None
        self.front = (self.front + 1) % len(self._data)
        self.size -= 1
        if self.size == len(self._data) // 4:
            self.__resize(len(self._data) // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        return self._data[self.front]

    def get_size(self):
        return self.size

    def get_capacity(self):
        return len(self._data)

    def add_first(self, element):
        if self.is_full():
            self.__resize(len(self._data) * 2)
        # 计算出索引
        self.front = (self.front + len(self._data) - 1) % len(self._data)
        self._data[self.front] = element
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        self.tail = (self.tail + len(self._data) - 1) % len(self._data)
        ret = self._data[self.tail]
        self._data[self.tail] = None
        self.size -= 1
        if self.size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self.__resize(len(self._data) // 2)
        return ret

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self._data)

    def __resize(self, new_capacity):
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[(self.front + i) % len(self._data)]
        self._data = new_data
        self.front = 0
        self.tail = self.size

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    queue = Deque()
    for i in range(5):
        print("add_first", i)
        queue.add_first(i)
    print(queue)
    for _ in range(5):
        print("pop", queue.pop())
        print(queue)
