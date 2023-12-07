from array_down import ArrayDownStack
from abstract_stack import EmptyStackException

import unittest

class TestArrayDownStack(unittest.TestCase):

    def test_push(self):
        stack = ArrayDownStack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.get_size(), 1)

    def test_push_resizing(self):
        stack = ArrayDownStack()
        for i in range(ArrayDownStack.INITIAL_SIZE):
            stack.push(i)
        # Stack should resize as we add the next element
        stack.push(ArrayDownStack.INITIAL_SIZE)
        self.assertEqual(stack.peek(), ArrayDownStack.INITIAL_SIZE)
        self.assertEqual(stack.get_size(), ArrayDownStack.INITIAL_SIZE + 1)

    def test_pop(self):
        stack = ArrayDownStack()
        stack.push(1)
        stack.push(2)
        value = stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(stack.get_size(), 1)

    def test_peek(self):
        stack = ArrayDownStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def test_is_empty(self):
        stack = ArrayDownStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_get_size(self):
        stack = ArrayDownStack()
        self.assertEqual(stack.get_size(), 0)
        for i in range(3):
            stack.push(i)
        self.assertEqual(stack.get_size(), 3)

    def test_empty_pop(self):
        stack = ArrayDownStack()
        with self.assertRaises(EmptyStackException):
            stack.pop()

    def test_empty_peek(self):
        stack = ArrayDownStack()
        with self.assertRaises(EmptyStackException):
            stack.peek()

if __name__ == '__main__':
    unittest.main()