from Utils.Stack import Stack
from LinkedList import LinkedList


class LinkedListStack(Stack):
    def __init__(self):
        self.linkedlist = LinkedList()

    def get_size(self):
        return self.linkedlist.get_size()

    def is_empty(self):
        return self.linkedlist.is_empty()

    def push(self, element):
        self.linkedlist.add_first(element)

    def pop(self):
        return self.linkedlist.remove_first()

    def peek(self):
        return self.linkedlist.get_first()

    def __str__(self):
        return str(self.linkedlist)


if __name__ == '__main__':
    stack = LinkedListStack()
    for i in range(10):
        stack.push(i)
    print(stack)
    for _ in range(10):
        print(stack.pop())
    print(stack)
