class MathuUtils:
    """A class that contains methods to extract multiples of 3 and 5 from a given number and compute the sum of the
    extracted multiples.
    """

    def __init__(self, number):
        """Initialize a MathuUtils object with a number."""
        self.number = number

    def extract_multiples_of_3(numbrt):
        """Extract multiples of 3 from a given number."""
        return [i for i in range(1, number) if i % 3 == 0]

    def extract_multiples_of_5(self):
        """Extract multiples of 5 from a given number."""
        return [i for i in range(1, self.number) if i % 5 == 0]

    def compute_sum_of_multiples_of_3_and_5(self):
        """Compute the sum of the extracted multiples of 3 and 5."""
        return sum(self.extract_multiples_of_3()) + sum(self.extract_multiples_of_5())

    def inform_the_sum(self):
        """Print the sum of the extracted multiples of 3 and 5."""
        sum_of_multiples = self.compute_sum_of_multiples_of_3_and_5()
        print(sum_of_multiples)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    mathu_utils = MathuUtils(number)
    MathuUtils.compute_sum_of_multiples_of_3_and_5(mathu_utils)
    mathu_utils.inform_the_sum()
