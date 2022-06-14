# Pytest Framework for testing HashTable Class and methods
# There is a fixture after each test is run that initialize the test again with a empty hash table

class TestHash:
    # Testing the creation of empty Hash Table
    def test_emptyHash(self):
        a = self.my_hash.print()
        # print(a)
        assert a == [None, None, None, None, None, None, None]
    # Testing the set of the first value in a Hash Table
    def test_setHash(self):
        self.my_hash.set_items('Zero', 0)
        # print(a)
        a = self.my_hash.print()
        assert a == [None, None, None, None, None, None, [['Zero', 0]]]
    # Testing the set of the n values in a Hash Table
    def test_setHash_n(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Three', 3)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        # print(a)
        a = self.my_hash.print()
        assert a == [[['Three', 3], ['Six', 6]], None, None, None, [['Five', 5]], [['Two', 2], ['Four', 4]], [['Zero', 0], ['One', 1]]]
    # Testing get for n values in a Hash Table
    def test_getHash_n(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Three', 3)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        a = self.my_hash.get('Five')
        assert a == [5]
    # Testing get for empty Hash Table
    def test_getHash_empty(self):
        a = self.my_hash.get('Five')
        assert a is None
    # Testing get for n values in a Hash Table, using key without associate value
    def test_getHash_key_no_value(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Three', 3)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        a = self.my_hash.get('Ten')
        assert a is None
    # Testing get of the Hast Table when using the same key for two values, it should return a list of the values
    # using the same key
    def test_getHash_1key_2values(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Three', 3)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        self.my_hash.set_items('Seven', 7)
        self.my_hash.set_items('Eight', 8)
        self.my_hash.set_items('Ten', 1010)
        self.my_hash.set_items('Ten', 10)
        a = self.my_hash.get('Ten')
        assert a == [1010, 10]
        self.my_hash.print()
    # Testing keys to return all possible keys in HashTable with a unique key with multiple values
    def test_keys_method_1key_2value(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Three', 3)
        self.my_hash.set_items('Three', 11)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        self.my_hash.set_items('Seven', 7)
        self.my_hash.set_items('Eight', 8)
        # a = self.my_hash.get('Ten')
        a = self.my_hash.keys()
        assert a == ['Three', 'Six', 'Eight', 'Five', 'Seven', 'Two', 'Four', 'Zero', 'One']
        # self.my_hash.print()
    # Testing keys to return all possible keys in HashTable with a unique key with 1 value
    def test_keys_method_1key_1value(self):
        self.my_hash.set_items('Zero', 0)
        self.my_hash.set_items('One', 1)
        self.my_hash.set_items('Two', 2)
        self.my_hash.set_items('Four', 4)
        self.my_hash.set_items('Five', 5)
        self.my_hash.set_items('Six', 6)
        self.my_hash.set_items('Seven', 7)
        self.my_hash.set_items('Eight', 8)
        a = self.my_hash.keys()
        assert a == ['Six', 'Eight', 'Five', 'Seven', 'Two', 'Four', 'Zero', 'One']
    # Testing keys to return Empty when no key available
    def test_keys_method_empty(self):
        a = self.my_hash.keys()
        assert a == []
