import pytest

from DLinkedList import DoublyLinkedList
from LinkedList import LinkedList
from Stacks import Stack
from Queue import Queue

@pytest.fixture(autouse =True)
def setup(request):
    my_linked_list = LinkedList(8)
    request.cls.my_linked_list = my_linked_list
    my_d_linked_list = DoublyLinkedList(1)
    request.cls.my_d_linked_list = my_d_linked_list
    my_stack = Stack(1)
    request.cls.my_stack = my_stack
    my_queue = Queue(2)
    request.cls.my_queue = my_queue



