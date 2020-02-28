import sys

sys.path.append('/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    # *** Plan ***
    # self.max = 0 ~ keeps track of the max number of nodes the DLL can hold
    # self.value = DoublyLinkedList() ~ list that holds the key-value entries in the correct order
    # self.storage = dict() ~ storage dict that provides fast access to every node stored in the cache

    def __init__(self, limit=10):
        self.limit = limit
        self.max = 0
        self.list = DoublyLinkedList()
        self.cache = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # *** Plan ***
    # need to find the key that's associated with the value so if key is in cache we are going to return
    # once that's done we are going to move that node to the end of the list
    # we are going to return the value and none if it is not in the catch

    def get(self, key):
        if key in self.cache: # if key is found in our cache
            node = self.cache[key] # gives the value associated with the key 
            self.list.move_to_end(node) # moves the key-value pair to the end of the list
            return node.value[1] # the value associated with the key
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    # *** Plan ***
    #

    def set(self, key, value):
        # if key in self.cache:
        #     new_node = self.cache[key]
        #     new_node.value = (key, value)
        #     self.list.move_to_end(new_node)
        #     return
        # if self.max >= self.limit:
        #     self.list.delete([0])
        #     self.list.remove_from_tail()
        #     self.max -= 1
        # overwrite the old value associated with the key with the newly-specified value

        # Instructor's solution
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.list.move_to_end(node)
            return
        if self.max == self.limit:
            del self.cache[self.list.head.value[0]]
            self.list.remove_from_head()
            self.max -= 1
        self.list.add_to_tail((key, value))
        self.cache[key] = self.list.tail
        self.max += 1 