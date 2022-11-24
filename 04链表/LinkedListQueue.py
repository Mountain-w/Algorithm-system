from Utils.Queue import Queue
from LinkedList import LinkedList


class LinkedListQueue(Queue):
    def __init__(self):
        self.linkedlist = LinkedList()

    def get_size(self):
        return self.linkedlist.get_size()

    def is_empty(self):
        return self.linkedlist.is_empty()

    def enqueue(self, element):
        self.linkedlist.add_last(element)

    def dequeue(self):
        return self.linkedlist.remove_first()

    def get_front(self):
        return self.linkedlist.get_first()

    def __str__(self):
        return str(self.linkedlist)


if __name__ == '__main__':
    queue = LinkedListQueue()
    for i in range(10):
        queue.enqueue(i)
    print(queue)
    for _ in range(10):
        print(queue.dequeue())
    # queue.dequeue()
