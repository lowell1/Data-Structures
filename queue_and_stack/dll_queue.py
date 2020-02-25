import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.list = DoublyLinkedList()

    def enqueue(self, value):
        self.list.add_to_head(value)

    def dequeue(self):
        return self.list.remove_from_tail()

    def len(self):
        return len(self.list)
