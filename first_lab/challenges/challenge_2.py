class MathuUtils:
    def __init__(self, number):
        self.number = number

    def extract_multiples_of_3(numbrt):
        return [i for i in range(1, number) if i % 3 == 0]
    
    def extract_multiples_of_5(self):
        return [i for i in range(1, self.number) if i % 5 == 0]
    
    def compute_sum_of_multiples_of_3_and_5(self):
        return sum(self.extract_multiples_of_3()) + sum(self.extract_multiples_of_5())
    
    def inform_the_sum(self):
        sum_of_multiples = self.compute_sum_of_multiples_of_3_and_5()
        print(sum_of_multiples)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    mathu_utils = MathuUtils(number)
    MathuUtils.compute_sum_of_multiples_of_3_and_5(mathu_utils)
    mathu_utils.inform_the_sum()