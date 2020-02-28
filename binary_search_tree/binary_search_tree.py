import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# class Node:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self

        while True:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left =  BinarySearchTree(value)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right =  BinarySearchTree(value)
                    break
                else:
                    cur_node = cur_node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur_node = self

        while cur_node is not None:
            if target == cur_node.value:
                return True
            elif target < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        cur_node = self
        # max_num = self.value

        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def recurse(node):
            cb(node.value)

            if node.left:
                recurse(node.left)
            
            if node.right:
                recurse(node.right)

        recurse(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            cur_node = queue.dequeue()
            print(cur_node.value)
            
            if cur_node.left:
                queue.enqueue(cur_node.left)

            if cur_node.right:
                queue.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            cur_node = stack.pop()
            print(cur_node.value)

            if cur_node.right:
                stack.push(cur_node.right)

            if cur_node.left:
                stack.push(cur_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left: self.pre_order_dft(node.left)
        if node.right: self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left: self.post_order_dft(node.left)
        if node.right: self.post_order_dft(node.right)
        print(node.value)