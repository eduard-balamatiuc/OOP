import math

class MathUtils:

    def __init__(self, number):
        self.number = number

    def find_next_perfect_square(self):
        return (math.sqrt(self.number)//1 + 1)**2

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    math_utils = MathUtils(number)
    print(math_utils.find_next_perfect_square())