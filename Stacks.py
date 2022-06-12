# Stack sample
# A stack is the same as a Linked List but with only the top pointer, it follows the LIFO method
# Look at this diagram sample, length 3
#
# Top -> 3
#        |
#        v
#        2
#        |
#        v
#        1

# Lets create a Stack and a Node class

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    # Constructor, everytime this class is called it will create a Node
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    # Print method into a list
    def print_stack(self):
        temp = self.top
        results = []
        while temp is not None:
            results.append(temp.value)
            temp = temp.next
        return results
    # Push method
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    # Pop method
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp

