import unittest

from dfm18.collections.queues._stack_based_queue import StackBasedQueue
from dfm18.collections.queues._errors import EmptyQueueException


class TestStackBasedQueue(unittest.TestCase):
    def setUp(self):
        self.queue = StackBasedQueue[int]()

    def test_enqueue_increases_size(self):
        self.assertEqual(self.queue.size, 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2)

    def test_unqueue_returns_elements_in_correct_order(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.unqueue(), 1)
        self.assertEqual(self.queue.unqueue(), 2)
        self.assertEqual(self.queue.unqueue(), 3)
        self.assertEqual(self.queue.size, 0)

    def test_unqueue_on_empty_queue_raises_exception(self):
        with self.assertRaises(EmptyQueueException):
            self.queue.unqueue()

    def test_size_is_consistent_after_operations(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2)
        self.queue.unqueue()
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size, 2)
        self.queue.unqueue()
        self.queue.unqueue()
        self.assertEqual(self.queue.size, 0)

    def test_transfer_inbound_to_outbound(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.unqueue()
        # Outbound stack should now have 1 item left
        self.assertEqual(self.queue.size, 1)
        self.assertEqual(self.queue.unqueue(), 2)
        self.assertEqual(self.queue.size, 0)

    def test_large_number_of_elements(self):
        for i in range(1000):
            self.queue.enqueue(i)

        for i in range(1000):
            self.assertEqual(self.queue.unqueue(), i)

    def test_empty_queue_size_is_zero(self):
        self.assertEqual(self.queue.size, 0)

    def test_enqueue_and_unqueue_alternating(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.unqueue(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.unqueue(), 2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.unqueue(), 3)
        self.assertEqual(self.queue.unqueue(), 4)
