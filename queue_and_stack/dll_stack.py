import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.list = DoublyLinkedList()

    def push(self, value):
        self.list.add_to_head(value)

    def pop(self):
        return self.list.remove_from_head()

    def len(self):
        return len(self.list)
