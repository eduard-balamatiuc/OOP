import math


class MathUtils:
    """A class that contains a method that finds the next perfect square of a given number."""

    def __init__(self, number):
        """Initialize a MathUtils object with a number."""
        self.number = number

    def find_next_perfect_square(self):
        """Find the next perfect square of a given number."""
        return (math.sqrt(self.number) // 1 + 1) ** 2


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    math_utils = MathUtils(number)
    print(math_utils.find_next_perfect_square())
