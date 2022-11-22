from Utils.Stack import Stack
from Array import Array


class ArrayStack(Stack):
    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.array.is_empty()

    def get_capacity(self):
        return self.array.get_capacity()

    def push(self, e):
        self.array.add_last(e)

    def pop(self):
        return self.array.remove_last()

    def peek(self):
        return self.array[-1]

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    stack = ArrayStack()
    for i in range(5):
        stack.push(i)
    print(stack)
    stack.pop()
    print(stack)
