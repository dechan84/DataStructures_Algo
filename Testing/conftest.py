import pytest

from DLinkedList import DoublyLinkedList
from LinkedList import LinkedList
from Stacks import Stack
from Queue import Queue
from Trees import BST


@pytest.fixture(autouse =True)
def setup(request):
    # Initialize LL with value == 8
    my_linked_list = LinkedList(8)
    request.cls.my_linked_list = my_linked_list
    # Initialize DLL with value == 1
    my_d_linked_list = DoublyLinkedList(1)
    request.cls.my_d_linked_list = my_d_linked_list
    # Initialize Stack with value == 1
    my_stack = Stack(1)
    request.cls.my_stack = my_stack
    # Initialize queue with value == 2
    my_queue = Queue(2)
    request.cls.my_queue = my_queue
    # Initialize BST with empty tree
    my_bst_tree = BST()
    request.cls.my_bst_tree = my_bst_tree





