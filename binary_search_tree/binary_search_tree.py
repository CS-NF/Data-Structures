# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.head.insert_before(value)
            self.head = self.head.prev
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        if not self.head and not self.tail:
            # Empty list, this is head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Planning
        # If LL is empty
        if not self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return
        # If node is head
        # If node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        
        # If node is in middle
        else:
            node.delete()
        self.length -= 1


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.storage.length < 1:
            return None 
        else:
            return self.storage.remove_from_head()

    def len(self):
       return self.storage.length

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.storage.length


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
            self.right.for_each(cb) # iterates through the right part of the tree getting every node 
        else:
            return None





    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    # *** Plan ***
    # meaning of in order print function: It should take the root/head of the binary tree and get all the values in the tree in order
    # find the root/head of the stack to see make sure it's not none 
    # if it's there then call the function recursivly on the node to the left and keep going left until you hit the leaf
    # then let's print that value of that last node and travers up the binary tree getting all the values of the node.left
    # do the say to the right side of the binary search tree
    def in_order_print(self, node):
        if node: # if there is a node 
            self.in_order_print(node.left)
            print(node.value) # print the value of that node
            self.in_order_print(node.right)
        else:
            return 

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # *** Plan ***
    # same plan as stack only replace stack with queue since it's a breadth first 
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # *** Plan ***
    # initializing stack class
    # add our node to head 
    # as long as the stack is greater then zero the code below will execute 
    # created a variable called current_node and it's equal to the  poped stack 
    # print out our right node
    # if we are on the left side of the tree
    # we want to then pop the left node
    # if we are on the right side of the tree
    # we want to pop the right node
    def dft_print(self, node):
        stack = Stack() # initializing stack class
        stack.push(node) # add our node to head 
        while stack.len() > 0: # as long as the stack is greater then zero the code below will execute 
            current_node = stack.pop() # created a variable called current_node and it's equal to the  poped stack 
            print(current_node.value) # print out the nodes value
            if current_node.left: # if we are on the left side of the tree
                stack.push(current_node.left) # we want to then pop the left node
            if current_node.right: # if we are on the right side of the tree
                stack.push(current_node.right) # we want to pop the right node









    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
