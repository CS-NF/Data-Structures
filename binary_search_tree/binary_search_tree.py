# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# class Queue:
#     def __init__(self):
#         self.size = 0
#         # Why is our DLL a good choice to store our elements?
#         self.storage = DoublyLinkedList()

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         if self.storage.length < 1:
#             return None 
#         else:
#             return self.storage.remove_from_head()

#     def len(self):
#        return self.storage.length

# class Stack:
#     def __init__(self):
#         self.size = 0
#         # Why is our DLL a good choice to store our elements?
#         self.storage = DoublyLinkedList()

#     def push(self, value):
#         self.storage.add_to_head(value)
#         self.size += 1

#     def pop(self):
#         if self.size <= 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_from_head()

#     def len(self):
#         return self.storage.length


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    # *** Plan ***
    # if the value is greater then the given index
    # self.left is going to equal the index in the Binary Search Tree
    # else we call the function recursivly
    # if the value is less then the given index
    # append self.value to the left 
    def insert(self, i):
        if i < self.value: # if the value is greater then the given index we will exicture the code below
            if not self.left: # if it's not the left part of the binary tree
                self.left = BinarySearchTree(i) # we assign to the left part of the binary search tree
            else:
               self.left.insert(i) # otherwise we will add (i == our value) to the left of the binary search tree 
        else:
            if not self.right:
                self.right = BinarySearchTree(i) # we assign to the right part of the binary search tree
            else:
                self.right.insert(i) # otherwise we will add (i == our value) to the right of the binary search tree
        

    # Return True if the tree contains the value
    # False if it does not
    
    # *** Plan ***
    # do an if statment to see if our target is equal to our self.value
    # if it does then check to see what value it is left or right 
    # if it's left return Ture 
    # if it's not left retrun False 
    # if it's right then return True 
    # if it's not return false 
    def contains(self, target):
        if target == self.value: # do an if statment to see if our target is equal to our self.value
                return True # if it is then we will just return true and the code stops there
            if not self.left: # if the value is not in the right part of the binary tree 
                return False # we will return False
            else:
                return self.left.contains(target) # otherwise if not false then we want to return the value recursivly
        else:
            if not self.right: # if the value is not in the right part of the binary tree 
                return False  # we will return False
            else:
                return self.right.contains(target) # otherwise if not false then we want to return the value recursivly


    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
