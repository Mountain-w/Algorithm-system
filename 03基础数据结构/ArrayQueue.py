from Utils.Queue import Queue
from Array import Array


class ArrayQueue(Queue):
    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.array.is_empty()

    def get_capacity(self):
        return self.array.get_capacity()

    def enqueue(self, element):
        self.array.add_last(element)

    def dequeue(self):
        return self.array.remove_frist()

    def get_front(self):
        return self.array[0]

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    queue = ArrayQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)
    for _ in range(10):
        queue.dequeue()
        print(queue)