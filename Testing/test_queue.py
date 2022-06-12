# Pytest Framework for testing Queue Class and methods
# There is a fixture after each test is run that initialize the test again with a queue of one element equals to 2
class TestStack:
    # This test add a new element to the queue
    def test_enqueue(self):
        self.my_queue.enqueue(7)
        self.my_queue.enqueue(14)
        self.my_queue.enqueue(21)
        gold_value = [21, 14, 7, 2]
        assert self.my_queue.print_queue() == gold_value
        # Remove until None and add one element
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        self.my_queue.enqueue(44)
        gold_value = [44]
        assert self.my_queue.print_queue() == gold_value
        # Add element with queue with size 1
        self.my_queue.enqueue(5)
        gold_value = [5, 44]
        assert self.my_queue.print_queue() == gold_value

    # This test remove the first element of the queue
    def test_dequeue(self):
        self.my_queue.enqueue(7)
        self.my_queue.enqueue(14)
        self.my_queue.enqueue(21)
        a = getattr(self.my_queue.dequeue(), "value")
        gold_value = 2
        assert a == gold_value
        gold_value = [21, 14, 7]
        assert self.my_queue.print_queue() == gold_value
        # Keep removing until 1 element
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        gold_value = [21]
        assert self.my_queue.print_queue() == gold_value
        # Keep removing...
        self.my_queue.dequeue()
        self.my_queue.dequeue()
        gold_value = []
        assert self.my_queue.print_queue() == gold_value

