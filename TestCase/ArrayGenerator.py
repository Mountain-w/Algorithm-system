import random
class ArrayGenerator:
    @staticmethod
    def generate_ordered_array(n):
        return [i for i in range(n)]

    @staticmethod
    def generate_random_array(n, start, end):
        return [random.randint(start, end-1) for _ in range(n)]
