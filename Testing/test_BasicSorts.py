# Pytest Framework for testing basic Sorts algorithm

class TestBasicSorts:
    def test_bubble_sort(self):
        a = self.my_sort.bubble_sort([1,3,5,2])
        print(a)
        assert a == [1,2,3,5]
    def test_selection_sort(self):
        a = self.my_sort.selection_sort([5,2,5,2])
        print(a)
        assert a == [2,2,5,5]
    def test_insertion_sort(self):
        a = self.my_sort.insertion_sort([5,2,5,2])
        print(a)
        assert a == [2,2,5,5]
    def test_merge_2list(self):
        a = self.my_sort.merge([1,2,5,6], [2,3,7,8])
        print(a)
        assert a == [1,2,2,3,5,6,7,8]
    def test_merge_sort(self):
        a = self.my_sort.merge_sort([1,2,5,6,2,3,7,8])
        print(a)
        assert a == [1,2,2,3,5,6,7,8]
    # Test to find the swap_index from a list using swap methods
    def test_swap_index(self):
        mylist = [4,6,1,7,3,2,5]
        a = self.my_sort.pivot(mylist, 0, 6)
        print(a)
        assert a == 3
        print(mylist)
        assert mylist == [2, 1, 3, 4, 6, 7, 5]
    # Test quicksort function
    def test_quicksort(self):
        mylist = [4, 6, 1, 7, 3, 2, 5]
        a = self.my_sort.quick_sort(mylist)
        assert a == [1, 2, 3, 4, 5, 6, 7]


