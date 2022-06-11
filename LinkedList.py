# Sample of LinkedList
# LinkedList has no index (normal list has)
# LinkedList are not continuously together in memory (normal list are), the values are spread in all mem
# LinkedList has a variable called 'head' that points to the first value of the list, and a variable named
# 'tail' that points to the last element.
# Each element of a LinkedList points to the 'next' element until the last element points to none
#   head             tail
#     |                |
#     v                v
#    (11)->(3)->(4)->(19)-> none
# Analysis of Big O in LinkedList for each method
# --Append--: the operation is that the last elements points to a new value instead of none and
# 'tail' needs to point to the new last element, this is a O(1) because no matter how many numbers are in the list
# its still 1 operation.
# --Pop--: the operation is that the last element is removed and the previous element now points
# to none, but now tails needs to point to that previous element, how will he find the pointer of that previous
# element? He needs to iterate from the head through all the elements until he finds the pointer, this is O(n)
# --Prepend--: the operation is to add a new element with the same pointer as head, then update head to point
# to the new element. This is O(1) only 1 operation
# --Pop first--: the operation is that head first points to head.next so we can have the pointer of current
# first element, after that we can make current first element points to none. This is O(1) only 1 operation.
# --Insert--: the operation is that the new number needs to be inserted in the middle of the LinkedList, we
# need to iterate from head until we find the element that will point to the new value node, after that we have
# the new element points to the same pointer that previous element have (now both the element to add and
# the previous one point the same value), after that we can make the previous element to point to the
# new element. This is O(n) because of the iteration.
# --Remove--: the operation is to delete a number in the middle of the LinkedList, first we need to iterate from
# head until we find the element we want to delete, we first needs to set the previous element to the same
# pointer of the element we want to delete (now both the element to delete and the previous one point
# the same value), now we can set the element to delete to point none. This is O(n) because of the iteration.
# --Lookup--: the operation search for the element we want we can do it either by value or by index,
# this requires to iterate from head until we find the element we need. The diff with lookup in list is that
# when we search by index in a list is O(1) is just want operation but in LinkedList you always needs to iterate
# from head. This is O(n) because of the iteration.

# A node is basically a dictionary with two elements (value and next)
# In python a LinkedList is a set of nested dictionary where each value is NOT in a continuous space in mem
# head = {
#     'value': 11,
#     'next': {
#         'value': 3,
#         'next': {
#             'value': 4,
#             'next': {
#                 'value': 19,
#                 'next': None
#                     }
#                 }
#             }
#         }
# print(head)

# Assume that I want to get the value 4
# print(head['next']['next']['value'])

# Lets create a LinkedList and a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # Condition is added in case we found that there is none elements in head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Here I am telling to the last element to points to the new element
            self.tail.next = new_node
            # Here I am telling to tail to points to new element
            self.tail = new_node
        self.length = self.length + 1
        # This is added because in the future we will needs this boolean result for another code
        return True

    def pop(self):
        # We should always code all the possible scenarios
        # There are diff ways to do this condition
        if self.head is None:
            return None
        elif self.head == self.tail:
            pop_value = self.head
            self.head = None
            self.tail = None
            # We should return the whole node, not only the value... but for testing purposes we do it...
            # return pop_value.value
            return pop_value
        else:
            temp = self.head
            pretemp = self.head
            while temp.next is not None:
                pretemp = temp
                temp = temp.next
            self.tail = pretemp
            self.tail.next = None
            self.length -= 1
            # return temp.value
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        # This is added because in the future we will needs this boolean result for another code
        return True

    def pop_first(self):
        # We should always code all the possible scenarios
        # There are diff ways to do this condition
        if self.head is None:
            return None
        elif self.head == self.tail:
            pop_value = self.head
            self.head = None
            self.tail = None
            # We should return the whole node, not only the value... but for testing purposes we do it...
            # return pop_value.value
            return pop_value
        else:
            temp1 = self.head
            temp2 = self.head.next
            self.head.next = None
            self.head = temp2
            self.length = -1
            # return temp1.value
            return temp1

    # For testing purposes, lets create a method to print the whole list
    def print_list(self):
        temp = self.head
        results = []
        while temp is not None:
            # print(temp.value)
            results.append(temp.value)
            temp = temp.next
        return results

    # This method receives an index an returns the value
    def get(self, index):
        if self.head is None:
            return None
        else:
            temp = self.head
            if index < 0:
                print('Index out of bounds')
                return None
            elif index > self.length:
                print('Index out of bounds')
                return None
            # If we are not going to use the variable in the for loop we can use _, only use a name if you
            # plan to use it
            for _ in range(index):
                temp = temp.next
            return temp

    # This method receives an index and a value to insert it in the LinkedList without deleting the
    # previous index
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            print('Index out of bounds')
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length-1:
            return self.append(value)
        else:
            # Lets reuse get() again to obtain the node parameters based on index
            # But we need to get the previous value of the index to insert the new node
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    # This method replace an old value on the desired index
    def set_value(self, index, value):
        temp_set = self.get(index)
        if temp_set:
            temp_set.value = value
            return True
        return False

    # This method remove the node in the specified index and update the LinkedList, it returns the
    # remove Node
    def remove(self, index):
        if index < 0 or index >= self.length:
            # If we are successful we return a Node
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            pretemp = self.get(index-1)
            temp = pretemp.next
            pretemp.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    # Interview question! How to reverse a LinkedList, tail will be head and viceversa, and each node
    # will invert the pointer
    #   head             tail
    #     |                |
    #     v                v
    #    (11)->(3)->(4)->(19)-> none
    # Now is:
    #          tail             head
    #           |                |
    #           v                v
    #    None<-(11)<-(3)<-(4)<-(19)
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range (self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
