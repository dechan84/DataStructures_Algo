# Pytest Framework for testing BST Class and methods
# There is a fixture after each test is run that initialize the test again with an empty BST
class TestStack:
    # This test creates an empty BST and validates to be None
    def test_BST_creation(self):
        print(self.my_bst_tree.root)
    # Test to insert on root value 10
    def test_insert_root(self):
        self.my_bst_tree.insert(10)
        print(self.my_bst_tree.root.value)
        assert self.my_bst_tree.root.value == 10
    # Test to insert on root value 5 and 15
    def test_insert_5_15(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(5)
        self.my_bst_tree.insert(15)
        print(self.my_bst_tree.root.value)
        assert self.my_bst_tree.root.value == 10
        print(self.my_bst_tree.root.left.value)
        assert self.my_bst_tree.root.left.value == 5
        print(self.my_bst_tree.root.right.value)
        assert self.my_bst_tree.root.right.value == 15
    # Test to insert on root value 10, 5, 15, 1
    def test_insert_5_15_1(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(5)
        self.my_bst_tree.insert(15)
        print(self.my_bst_tree.root.value)
        assert self.my_bst_tree.root.value == 10
        print(self.my_bst_tree.root.left.value)
        assert self.my_bst_tree.root.left.value == 5
        print(self.my_bst_tree.root.right.value)
        assert self.my_bst_tree.root.right.value == 15
        self.my_bst_tree.insert(1)
        print(self.my_bst_tree.root.left.left.value)
        assert self.my_bst_tree.root.left.left.value == 1
    # Test that search the value we want if is in an empty tree
    def test_contains_empty(self):
        print(self.my_bst_tree.contains(1))
        assert self.my_bst_tree.contains(1) == False
    # Test that search the value we want if is in a tree with only root
    def test_contains_root(self):
        self.my_bst_tree.insert(10)
        print(self.my_bst_tree.contains(10))
        assert self.my_bst_tree.contains(10) == True
    # Test that search the value we want if is in a tree with more elements
    def test_contains_n_elements(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(4)
        self.my_bst_tree.insert(12)
        self.my_bst_tree.insert(1)
        self.my_bst_tree.insert(2)
        print(self.my_bst_tree.contains(1))
        assert self.my_bst_tree.contains(1) == True
    # Test that search the value we want if is NOT in a tree with more elements
    def test_contains_n_elements_NOT(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(4)
        self.my_bst_tree.insert(12)
        self.my_bst_tree.insert(1)
        self.my_bst_tree.insert(2)
        print(self.my_bst_tree.contains(44))
        assert self.my_bst_tree.contains(44) == False
    # Test the minimum value from reference root
    def test_minimum_value_root(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(4)
        self.my_bst_tree.insert(12)
        self.my_bst_tree.insert(1)
        self.my_bst_tree.insert(2)
        a = getattr(self.my_bst_tree.minimumValue(self.my_bst_tree.root), "value")
        assert a == 1
    # Test the minimum value from reference root.right
    def test_minimum_value_root_right(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(4)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(14)
        self.my_bst_tree.insert(12)
        a = getattr(self.my_bst_tree.minimumValue(self.my_bst_tree.root.right), "value")
        assert a == 12
    # Test the minimum value from reference root.left
    def test_minimum_value_root_left(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(8)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(7)
        self.my_bst_tree.insert(9)
        self.my_bst_tree.insert(1)
        a = getattr(self.my_bst_tree.minimumValue(self.my_bst_tree.root.left.left), "value")
        assert a == 1
    # Test the minimum value from reference only root
    def test_minimum_value_only_root(self):
        self.my_bst_tree.insert(10)
        a = getattr(self.my_bst_tree.minimumValue(self.my_bst_tree.root), "value")
        assert a == 10
    # Test tree traversal using BFS, we convert a BST into a list by traversing the tree
    def test_BFS_tree_traversal(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(7)
        self.my_bst_tree.insert(8)
        self.my_bst_tree.insert(14)
        self.my_bst_tree.insert(16)
        self.my_bst_tree.insert(9)
        # The returned list should NOT always be the same order than how we insert each value in the tree, its better
        # to draw the tree manually and then you can see how each child leaf gets added
        a = self.my_bst_tree.BFS()
        assert a == [10, 7, 15, 8, 14, 16, 9]
    # Test tree traversal using DFS pre order, we convert a BST into a list by traversing the tree
    def test_DFS_pre_tree_traversal(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(7)
        self.my_bst_tree.insert(8)
        self.my_bst_tree.insert(14)
        self.my_bst_tree.insert(16)
        self.my_bst_tree.insert(9)
        # The returned list should NOT always be the same order than how we insert each value in the tree, its better
        # to draw the tree manually and then you can see how each child leaf gets added
        a = self.my_bst_tree.DFS_pre()
        assert a == [10, 7, 8, 9, 15, 14, 16]
    # Test tree traversal using DFS post order, we convert a BST into a list by traversing the tree
    def test_DFS_post_tree_traversal(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(7)
        self.my_bst_tree.insert(8)
        self.my_bst_tree.insert(14)
        self.my_bst_tree.insert(16)
        self.my_bst_tree.insert(9)
        # The returned list should NOT always be the same order than how we insert each value in the tree, its better
        # to draw the tree manually and then you can see how each child leaf gets added
        a = self.my_bst_tree.DFS_post()
        assert a == [9, 8, 7, 14, 16, 15, 10]
    # Test tree traversal using DFS in order, we convert a BST into a ordered list by traversing the tree
    def test_DFS_in_tree_traversal(self):
        self.my_bst_tree.insert(10)
        self.my_bst_tree.insert(15)
        self.my_bst_tree.insert(7)
        self.my_bst_tree.insert(8)
        self.my_bst_tree.insert(14)
        self.my_bst_tree.insert(16)
        self.my_bst_tree.insert(9)
        # The returned list should NOT always be the same order than how we insert each value in the tree, its better
        # to draw the tree manually and then you can see how each child leaf gets added
        a = self.my_bst_tree.DFS_in()
        assert a == [7, 8, 9, 10, 14, 15, 16]

