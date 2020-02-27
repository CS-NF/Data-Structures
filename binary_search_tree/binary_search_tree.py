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
            if not self.left: # if the value is not in the right part of the binarytree 
                return False # we will return False
            else:
                return self.left.contains(target) # otherwise if not false then we want to return the value recursivly
        else:
            if not self.right: # if the value is not in the right part of the binarytree 
                return False  # we will return False
            else:
                return self.right.contains(target) # otherwise if not false then we want to return the value recursivly


    # Return the maximum value found in the tree
    
    # *** Plan ***
    # do an if statment see if self.right because we know that the max will be in the right part of the tree beacuse the right index will be bigger then the head index
    # return the value of the right index
    # else it will return the right side of the binary tree with the recursive call of get_max to get the biggest value
    def get_max(self):
        if not self.right: # seeing if the tree does not point to the right of the tree if so code below get exicuted
            return self.value # we will then just return the value of the binary tree most likely on the left
        else:
            return self.right.get_max() # otherwise we will return the right part of the tree with the recursive call to get the biggest number in the right side of the tree

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    # *** Plan ***
    # see if index/node in the left part of the tree 
    # if so then we will assign for_each to the left part of the tree. Since we are doing this recursily it will iterate through the left part of the tree and get ever sign index/node 
    # if index/node in the right part of the tree 
    # then we will assign for_each to teh right part of the tree. Since we are doing this recursively it will iterate through the right part of the tree and get ever sign index/node 
    def for_each(self, cb):
        if self.left: # if we are looking at the left part of the tree then execute code below
            self.left.for_each(cb) # iterates through the left part of the tree getting ever node 
        else:
            return None  
        if self.right: # if we are looking at the right part of the tree then execute code below
            self.right.for_each(cb) # iterates through the right part of the tree getting ever node 
        else:
            return None





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
