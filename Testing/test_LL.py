# Pytest Framework for testing LinkedList Class and methods
# There is a fixture after each test is run that initialize the test again with a LL of one element equals to 8
class TestLL:
    # Appending 2 and 1 to previously initiated LL
    # Gold value is expected to be [8, 2, 1]
    def test_append(self):
        self.my_linked_list.append(2)
        self.my_linked_list.append(1)
        gold_file = [8, 2, 1]
        assert self.my_linked_list.print_list() == gold_file
    # Pop 1 to previously initiated LL
    def test_pop(self):
        self.my_linked_list.append(1)
        a = getattr(self.my_linked_list.pop(), "value")
        assert a ==  1
        gold_file = [8]
        assert self.my_linked_list.print_list() == gold_file
    # Append 1 to a zero elements LL
    # Gold value is expected to be [1]
    def test_append_0_element(self):
        self.my_linked_list.pop()
        self.my_linked_list.append(1)
        gold_file = [1]
        assert self.my_linked_list.print_list() == gold_file
    # Pop 1 elements
    # Gold value is expected to be []
    def test_pop_1_element(self):
        a = getattr(self.my_linked_list.pop(), "value")
        assert a == 8
        gold_file = []
        assert self.my_linked_list.print_list() == gold_file
    # Pop 0 elements
    # Gold value is expected to be []
    def test_pop_0_element(self):
        self.my_linked_list.pop()
        self.my_linked_list.pop()
        gold_file = []
        assert self.my_linked_list.print_list() == gold_file
    # Prepend with 0 elements
    def test_prepend_0_element(self):
        self.my_linked_list.pop()
        self.my_linked_list.prepend(3)
        gold_file = [3]
        assert self.my_linked_list.print_list() == gold_file
    # Prepend with 1 elements
    def test_prepend_n_element(self):
        self.my_linked_list.prepend(1)
        self.my_linked_list.prepend(22)
        gold_file = [22, 1, 8]
        assert self.my_linked_list.print_list() == gold_file
    # Pop first with n elements
    def test_pop1st_n_element(self):
        self.my_linked_list.prepend(44)
        a = getattr(self.my_linked_list.pop_first(), "value")
        assert a == 44
        gold_file = [8]
        assert self.my_linked_list.print_list() == gold_file
    # Pop first with 1 elements
    # Gold value is expected to be []
    def test_pop1st_1_element(self):
        a = getattr(self.my_linked_list.pop_first(), "value")
        assert a == 8
        gold_file = []
        assert self.my_linked_list.print_list() == gold_file
    # Pop first with 0 elements
    # Gold value is expected to be []
    def test_pop1st_0_element(self):
        self.my_linked_list.pop()
        self.my_linked_list.pop_first()
        gold_file = []
        assert self.my_linked_list.print_list() == gold_file
    # Testing get with n elements
    def test_get_n_element(self):
        self.my_linked_list.append(10)
        self.my_linked_list.append(8)
        self.my_linked_list.append(10)
        self.my_linked_list.append(1)
        gold_file = [8, 10, 8, 10, 1]
        assert self.my_linked_list.print_list() == gold_file
        a = getattr(self.my_linked_list.get(3), "value")
        assert a == 10
    # Testing set with n elements
    def test_set_n_element(self):
        self.my_linked_list.append(10)
        self.my_linked_list.append(8)
        self.my_linked_list.append(1)
        self.my_linked_list.prepend(12)
        gold_file = [12,8,10,8,1]
        assert self.my_linked_list.print_list() == gold_file
        self.my_linked_list.set_value(4, 3)
        gold_file = [12, 8, 10, 8, 3]
        assert self.my_linked_list.print_list() == gold_file
    # Testing remove with n elements
    def test_remove_n_element(self):
        self.my_linked_list.append(10)
        self.my_linked_list.append(8)
        self.my_linked_list.append(1)
        self.my_linked_list.prepend(12)
        gold_file = [12,8,10,8,1]
        assert self.my_linked_list.print_list() == gold_file
        self.my_linked_list.remove(3)
        gold_file = [12,8,10,1]
        assert self.my_linked_list.print_list() == gold_file
    # Testing reverse list with n elements
    def test_reverse_n_element(self):
        self.my_linked_list.append(1)
        self.my_linked_list.append(2)
        self.my_linked_list.append(3)
        self.my_linked_list.prepend(12)
        gold_file = [12,8,1,2,3]
        assert self.my_linked_list.print_list() == gold_file
        self.my_linked_list.reverse()
        gold_file = [3, 2, 1, 8, 12]
        assert self.my_linked_list.print_list() == gold_file