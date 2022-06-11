import pytest

from DLinkedList import DoublyLinkedList
from LinkedList import LinkedList

@pytest.fixture(autouse =True)
def setup(request):
    my_linked_list = LinkedList(8)
    request.cls.my_linked_list = my_linked_list
    my_dd_linked_list = DoublyLinkedList(1)
    request.cls.my_dd_linked_list = my_dd_linked_list

