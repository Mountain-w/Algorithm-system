from Utils.Queue import Queue


class LoopQueue(Queue):
    def __init__(self, capacity=10):
        self.data = [0] * (capacity + 1)
        self.front = 0
        self.tail = 0
        self.size = 0

    def get_capacity(self):
        return len(self.data) - 1

    def is_empty(self):
        return self.front == self.tail

    def get_size(self):
        return self.size

    def enqueue(self, element):
        if (self.tail + 1) % len(self.data) == self.front:
            self.__resize(self.get_capacity() * 2)
        self.data[self.tail] = element
        self.tail = (self.tail + 1) % len(self.data)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        ret = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        if self.size == len(self.data) // 4 and len(self.data) // 2 != 0:
            self.__resize(self.get_capacity() // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        return self.data[self.front]

    def __resize(self, new_capacity):
        new_data = [0] * (new_capacity + 1)
        for i in range(self.size):
            new_data[i] = self.data[(i + self.front) % len(self.data)]
        self.data = new_data
        self.front = 0
        self.tail = self.size

    def __str__(self):
        return str(self.data)


class LoopQueue1(Queue):
    def __init__(self, capacity=10):
        self.data = [0] * (capacity + 1)
        self.front = 0
        self.tail = 0

    def get_capacity(self):
        return len(self.data) - 1

    def is_empty(self):
        return self.front == self.tail

    def get_size(self):
        return (self.tail if self.tail >= self.front else self.tail + len(self.data)) - self.front

    def enqueue(self, element):
        if (self.tail + 1) % len(self.data) == self.front:
            self.__resize(self.get_capacity() * 2)
        self.data[self.tail] = element
        self.tail = (self.tail + 1) % len(self.data)

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        ret = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        if self.get_size() == len(self.data) // 4 and len(self.data) // 2 != 0:
            self.__resize(self.get_capacity() // 2)
        return ret

    def get_front(self):
        if self.is_empty():
            raise RuntimeError("Queue is Empty")
        return self.data[self.front]

    def __resize(self, new_capacity):
        new_data = [0] * (new_capacity + 1)
        for i in range(self.get_size()):
            new_data[i] = self.data[(i + self.front) % len(self.data)]
        self.tail = self.get_size()
        self.data = new_data
        self.front = 0

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    queue = LoopQueue1()
    for i in range(19):
        queue.enqueue(i)
        if i % 4 == 0:
            queue.dequeue()
        print(queue)
    for _ in range(10):
        queue.dequeue()
        print(queue)
