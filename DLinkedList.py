# Double Linked List sample
# A DLL is the same as a Linked List, but the difference is that the node has to pointers, next and prev
# Look at this diagram sample>
# Each element of a LinkedList points to the 'next' element until the last element points to none
#           head             tail
#           |                |
#           v                v
#    none <-(11)->(3)->(4)->(19)-> none
#               <-   <-   <-
# Lets create a DLinkedList and a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Constructor, everytime this class is called it will create a Node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # For testing purposes, lets create a method to print the whole list
    def print_list(self):
        temp = self.head
        results = []
        while temp is not None:
            results.append(temp.value)
            temp = temp.next
        return results

    # Append method, the same as LL the difference is updated the prev from new node
    def append(self, value):
        new_node = Node(value)
        # Condition is added in case we found that there is none elements in head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Here I am telling to new node prev to point last element
            new_node.prev = self.tail
            # Here I am telling to the last element to points to the new element
            self.tail.next = new_node
            # Here I am telling to tail to points to new element
            self.tail = new_node

        self.length = self.length + 1
        # This is added because in the future we will needs this boolean result for another code
        return True

    # Pop method
    def pop(self):
        # We should always code all the possible scenarios
        # There are diff ways to do this condition
        temp = self.tail
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    # Pop method
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        # This is added because in the future we will needs this boolean result for another code
        return True

    # Pop first method
    def pop_first(self):
        # We should always code all the possible scenarios
        # There are diff ways to do this condition
        temp = self.head
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length = -1
        return temp

    # This method receives an index and returns the value
    def get(self, index):
        temp = self.head
        if self.head is None:
            return None
        else:
            if index < 0:
                print('Index out of bounds')
                return None
            elif index >= self.length:
                print('Index out of bounds')
                return None
            elif index == 0:
                return temp
            # If we are not going to use the variable in the for loop we can use _, only use a name if you
            # plan to use it
            elif self.length % index == 0:
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - index - 1):
                    temp = temp.prev
        return temp

    # This method replace an old value on the desired index
    def set_value(self, index, value):
        temp_set = self.get(index)
        if temp_set:
            temp_set.value = value
            return True
        return False

    # This method receives an index and a value to insert it in the DLinkedList without deleting the
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
            temp = self.get(index - 1)
            after = temp.next
            new_node.next = after
            after.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            self.length += 1
            return True

    # This method remove the node in the specified index and update the DLinkedList, it returns the
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
            # There are two methods to do this
            # The first one is using 3 variables like this
            # pretemp = self.get(index-1)
            # temp = pretemp.next
            # postemp = temp.next
            # temp.next = None
            # temp.prev = None
            # postemp.prev = pretemp
            # pretemp.next = postemp
            # The second one is using 1 variable and nested pointers
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None

        self.length -= 1
        return temp
