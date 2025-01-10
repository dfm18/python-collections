import unittest

from dfm18.collections import Stack, EmptyStackException


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack[int]()

    def test_push_increases_size(self):
        self.assertEqual(self.stack.size, 0)
        self.stack.push(10)
        self.assertEqual(self.stack.size, 1)
        self.stack.push(20)
        self.assertEqual(self.stack.size, 2)

    def test_pop_decreases_size(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.size, 1)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.size, 0)

    def test_pop_on_empty_stack_raises_exception(self):
        with self.assertRaises(EmptyStackException):
            self.stack.pop()

    def test_peek_returns_top_element(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 10)

    def test_peek_on_empty_stack_raises_exception(self):
        with self.assertRaises(EmptyStackException):
            self.stack.peek()

    def test_contains(self):
        self.stack.push(10)
        self.assertTrue(self.stack.contains(10))
        self.assertTrue(10 in self.stack)
        self.assertFalse(self.stack.contains(20))
        self.assertFalse(20 in self.stack)
        self.stack.pop()
        self.assertFalse(self.stack.contains(10))
        self.assertFalse(10 in self.stack)

    def test_clear(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.clear()
        self.assertEqual(self.stack.size, 0)
        with self.assertRaises(EmptyStackException):
            self.stack.peek()
