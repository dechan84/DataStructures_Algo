# Pytest Framework for testing Stack Class and methods
# There is a fixture after each test is run that initialize the test again with a stack of one element equals to 1
class TestStack:
    # Test to push elements in a stack with at least 1 element previously defined
    def test_push(self):
        self.my_stack.push(2)
        self.my_stack.push(3)
        gold_value = [3, 2, 1]
        assert self.my_stack.print_stack() == gold_value
    # Test to pop elements in a stack with at least 1 element previously defined
    def test_pop(self):
        # Pop with 2 elements on stack
        self.my_stack.push(55)
        # Now we should return [55,1], there are two values in stack
        assert self.my_stack.print_stack() == [55, 1]
        a = getattr(self.my_stack.pop(), "value")
        gold_value = 55
        assert a == gold_value
        # Now we should return 1, there is one value in stack
        assert self.my_stack.print_stack() == [1]
        # Pop with 1 element on stack
        a = getattr(self.my_stack.pop(), "value")
        gold_value = 1
        assert a == gold_value
        # Now we should return nothing, there is no value in stack
        assert self.my_stack.print_stack() == []

