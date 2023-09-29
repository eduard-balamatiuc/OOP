class MathUtils:
    def __init__(self, number):
        self.number = number

    def check_narcisistic_number(self):
        number = self.number
        sum_of_digits = 0
        while number > 0:
            digit = number % 10
            sum_of_digits += digit**3
            number //= 10
        return sum_of_digits == self.number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    math_utils = MathUtils(number)
    print(math_utils.check_narcisistic_number())
