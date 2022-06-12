# Queue sample
# A Queue is the same as a Double Linked List, but the difference it follows the FIFO method
# Look at this diagram sample
#           last             first
#           |                |
#           v                v
#    none <-(11)->(3)->(4)->(19)-> none
#               <-   <-   <-
# Lets create a Queue and a Node class based on a DLL
# Another structure we can use is a LL, using pop first to dequeue and append to enqueue both are O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # For testing purposes, lets create a method to print the whole list and returns a list
    def print_queue(self):
        temp = self.last
        results = []
        while temp is not None:
            results.append(temp.value)
            temp = temp.next
        return results
    # Enqueue method to add elements to the queue on the last position
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last.prev = new_node
            self.last = new_node
        self.length = self.length + 1
        # This is added because in the future we will needs this boolean result for another code
        return True

    # Dequeue method to remove elements to the queue on the first position
    def dequeue(self):
        temp = self.first
        if self.first is None:
            return None
        elif self.last == self.first:
            self.first = None
            self.last = None
        else:
            self.first = self.first.prev
            temp.prev = None
            self.first.next = None
        self.length -= 1
        return temp


