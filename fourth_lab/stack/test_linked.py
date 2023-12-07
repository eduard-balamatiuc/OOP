from linked_stack import LinkedStack
from abstract_stack import EmptyStackException

import unittest

class TestLinkedStack(unittest.TestCase):

    def test_push(self):
        stack = LinkedStack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.get_size(), 1)

    def test_pop(self):
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        value = stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(stack.get_size(), 1)

    def test_peek(self):
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.get_size(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def test_is_empty(self):
        stack = LinkedStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_get_size(self):
        stack = LinkedStack()
        self.assertEqual(stack.get_size(), 0)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.get_size(), 5)

    def test_empty_pop(self):
        stack = LinkedStack()
        self.assertRaises(EmptyStackException, stack.pop)

    def test_empty_peek(self):
        stack = LinkedStack()
        self.assertRaises(EmptyStackException, stack.peek)

if __name__ == '__main__':
    unittest.main()
