class Diamond:
    def __init__(self, size):
        self.size = size

    def print_diamond(self):
        if self.size % 2 == 0:
            self.size += 1

        n = self.size // 2 + 1

        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))

        for i in range(n - 1, 0, -1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))


# Example usage:
diamond = Diamond(5)
diamond.print_diamond()
