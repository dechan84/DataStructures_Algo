# Pytest Framework for testing Doubly LinkedList Class and methods
# There is a yield method after each test is run that initialize the test again with a DLL of one element equals to 1
class TestDLL:
    # Appending 2 and 1 to previously initiated DLL
    def test_append(self):
        self.my_dd_linked_list.append(2)
        self.my_dd_linked_list.append(1)
        gold_file = [1, 2, 1]
        assert self.my_dd_linked_list.print_list() == gold_file
    #  Pop to previously initiated LL
    def test_pop(self):
        self.my_dd_linked_list.append(3)
        a = getattr(self.my_dd_linked_list.pop(), "value")
        assert a == 3
        gold_file = [1]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Append 1 to a zero elements LL
    def test_append_0_element(self):
        self.my_dd_linked_list.pop()
        self.my_dd_linked_list.append(1)
        gold_file = [1]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Pop 1 elements
    def test_pop_1_element(self):
        a = getattr(self.my_dd_linked_list.pop(), "value")
        assert a == 1
        gold_file = []
        assert self.my_dd_linked_list.print_list() == gold_file
    # Pop 0 elements
    def test_pop_0_element(self):
        self.my_dd_linked_list.pop()
        self.my_dd_linked_list.pop()
        gold_file = []
        assert self.my_dd_linked_list.print_list() == gold_file
    # Prepend with 0 elements
    def test_prepend_0_element(self):
        self.my_dd_linked_list.pop()
        self.my_dd_linked_list.prepend(3)
        gold_file = [3]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Prepend with 1 elements
    def test_prepend_n_element(self):
        self.my_dd_linked_list.prepend(1)
        self.my_dd_linked_list.prepend(22)
        gold_file = [22, 1, 1]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Pop first with n elements
    def test_pop1st_n_element(self):
        self.my_dd_linked_list.prepend(44)
        self.my_dd_linked_list.prepend(55)
        self.my_dd_linked_list.prepend(2)
        a = getattr(self.my_dd_linked_list.pop_first(), "value")
        assert a == 2
        gold_file = [55, 44, 1]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Pop first with 1 elements
    def test_pop1st_1_element(self):
        a = getattr(self.my_dd_linked_list.pop_first(), "value")
        assert a == 1
        gold_file = []
        assert self.my_dd_linked_list.print_list() == gold_file
    # Pop first with 0 elements
    def test_pop1st_0_element(self):
        self.my_dd_linked_list.pop()
        self.my_dd_linked_list.pop_first()
        gold_file = []
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing get with n elements with index less than half the length of DLL
    def test_get_n_element1(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(2)
        self.my_dd_linked_list.append(4)
        gold_file = [1, 10, 8, 2, 4]
        assert self.my_dd_linked_list.print_list() == gold_file
        a = getattr(self.my_dd_linked_list.get(1), "value")
        assert a == 10
    # Testing get with n elements with index more than half the length of DLL
    def test_get_n_element2(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(2)
        self.my_dd_linked_list.append(4)
        gold_file = [1, 10, 8, 2, 4]
        assert self.my_dd_linked_list.print_list() == gold_file
        a = getattr(self.my_dd_linked_list.get(3), "value")
        assert a == 2
    # Testing set with n elements
    def test_set_n_element(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(7)
        self.my_dd_linked_list.prepend(12)
        gold_file = [12,1,10,8,7]
        assert self.my_dd_linked_list.print_list() == gold_file
        self.my_dd_linked_list.set_value(4, 3)
        gold_file = [12,1,10,8,3]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing set with n elements on index 1
    def test_set_n_element_index1(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(7)
        self.my_dd_linked_list.prepend(12)
        gold_file = [12,1,10,8,7]
        assert self.my_dd_linked_list.print_list() == gold_file
        self.my_dd_linked_list.set_value(1, 9)
        gold_file = [12,9,10,8,7]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing insert with n elements on index 1
    def test_insert_n_element_index1(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(7)
        self.my_dd_linked_list.insert(1, 44)
        gold_file = [1, 44, 10, 8, 7]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing insert with n elements on index 0
    def test_insert_n_element_index0(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(7)
        self.my_dd_linked_list.insert(0, 44)
        gold_file = [44, 1, 10, 8, 7]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing insert with n elements on index n
    def test_insert_n_element_indexn(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(7)
        self.my_dd_linked_list.insert(3, 44)
        gold_file = [ 1, 10, 8, 7, 44]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing remove with n elements
    def test_remove_n_element(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(1)
        self.my_dd_linked_list.prepend(12)
        gold_file = [12,1,10,8,1]
        assert self.my_dd_linked_list.print_list() == gold_file
        a = getattr(self.my_dd_linked_list.remove(3), "value")
        assert a == 8
        gold_file = [12,1,10,1]
        assert self.my_dd_linked_list.print_list() == gold_file
    # Testing remove with n elements index 1
    def test_remove_n_element_index1(self):
        self.my_dd_linked_list.append(10)
        self.my_dd_linked_list.append(8)
        self.my_dd_linked_list.append(1)
        self.my_dd_linked_list.prepend(12)
        gold_file = [12,1,10,8,1]
        assert self.my_dd_linked_list.print_list() == gold_file
        a = getattr(self.my_dd_linked_list.remove(1), "value")
        assert a == 1
        gold_file = [12,10,8,1]
        assert self.my_dd_linked_list.print_list() == gold_file