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
    def __init__(self):
        self.stack_in = ArrayStack()
        self.stack_out = ArrayStack()
        self.size = 0

    def enqueue(self, element):
        self.stack_in.push(element)
        self.size += 1

    def move(self):
        while self.stack_in.get_size() != 0:
            self.stack_out.push(self.stack_in.pop())

    def dequeue(self):
        if self.size == 0:
            raise RuntimeError("Queue is empty")
        if self.stack_out.get_size() == 0:
            self.move()
        ret = self.stack_out.pop()
        self.size -= 1
        return ret

    def get_front(self):
        if self.size == 0:
            raise RuntimeError("Queue is empty")
        if self.stack_out.get_size() == 0:
            self.move()
        return self.stack_out.peek()


if __name__ == '__main__':
    print("test stack")
    stack = StackByQueue()
    for i in range(10):
        stack.push(i)
    for _ in range(10):
        print(stack.pop())
    print("test queue")
    queue = QueueByStack()
    for i in range(10):
        queue.enqueue(i)
    for _ in range(10):
        print(queue.get_front())
    print(queue.dequeue())
    print(queue.dequeue())