from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


class StackByQueue:
    def __init__(self):
        self.queue1 = ArrayQueue()
        self.queue2 = ArrayQueue()
        self.size = 0

    def push(self, element):
        self.queue1.enqueue(element)
        self.size += 1

    def move(self):
        while self.queue1.get_size() != 1:
            self.queue2.enqueue(self.queue1.dequeue())

    def pop(self):
        if self.size == 0:
            raise RuntimeError("Stack is empty")
        self.move()
        ret = self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.size -= 1
        return ret

    def peek(self):
        if self.size == 0:
            raise RuntimeError("Stack is empty")
        self.move()
        return self.queue1.get_front()


class QueueByStack:
    pass


if __name__ == '__main__':
    stack = StackByQueue()
    for i in range(10):
        stack.push(i)
    for _ in range(10):
        print(stack.pop())
