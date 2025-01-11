import unittest

from dfm18.collections.queues._list_based_queue import ListBasedQueue
from dfm18.collections.queues._errors import EmptyQueueException


class TestListBasedQueue(unittest.TestCase):
    def setUp(self):
        self.queue = ListBasedQueue()

    def test_enqueue_increases_size(self):
        self.assertEqual(self.queue.size, 0)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size, 2)

    def test_dequeue_decreases_size(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size, 2)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.size, 1)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.size, 0)

    def test_dequeue_on_empty_queue_raises_exception(self):
        with self.assertRaises(EmptyQueueException):
            self.queue.dequeue()

    def test_size_property(self):
        self.assertEqual(self.queue.size, 0)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.size, 1)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size, 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size, 1)

    def test_len_dunder_method(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(len(self.queue), 2)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 1)

    def test_enqueue_and_dequeue_with_multiple_types(self):
        queue = ListBasedQueue[str]()
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertEqual(queue.size, 0)
