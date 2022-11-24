class Node:
    def __init__(self, value, nex=None):
        self.value = value
        self.next = nex

    def __str__(self):
        return f"<Node {self.value}>"


class LinkedList:

    def __init__(self):
        self.__dummy_head = Node(None)
        self.tail = self.__dummy_head
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def add_first(self, element):
        self.add(0, element)

    def add_last(self, element):
        self.tail.next = Node(element)
        self.tail = self.tail.next
        self.__size += 1

    def add(self, index, element):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        prev = self.__dummy_head
        for _ in range(index):
            prev = prev.next
        prev.next = Node(element, prev.next)
        self.__size += 1

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        cur = self.__dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.value

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(self.__size - 1)

    def set(self, index, value):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        cur = self.__dummy_head.next
        for _ in range(index):
            cur = cur.next
        cur.value = value

    def cotains(self, element):
        cur = self.__dummy_head.next
        while cur:
            if cur.value == element.value:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        if self.is_empty():
            raise RuntimeError("Empty")
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        cur = self.__dummy_head
        for _ in range(index):
            cur = cur.next
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = None
        self.__size -= 1
        return nxt

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.__size - 1)

    def __str__(self):
        string = []
        cur = self.__dummy_head.next
        while cur:
            string.append(str(cur))
            cur = cur.next
        return "->".join(string)


if __name__ == '__main__':
    linkedlist = LinkedList()
    for i in range(10):
        linkedlist.add_last(i)
        print(linkedlist)
    linkedlist.add(2, 666)
    print(linkedlist)
    linkedlist.remove(2)
    print(linkedlist)
