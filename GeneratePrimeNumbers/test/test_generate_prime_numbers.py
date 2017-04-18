import unittest
from math import sqrt

class TestGeneratePrimeNumbers(unittest.TestCase):
    
    def setUp(self):
        self.arg_limit = 32
        self.sample_prime = [2,3,5,7,11,13,17,19,23]

    def test_generate_prime_numbers_returns_error_message_if_arg_not_number(self):
        self.assertRaises(TypeError, generatePrimeNumbers, 'two')

    def test_generate_prime_numbers_returns_error_if_arg_is_less_than_three(self):
        self.assertRaises(ValueError, generatePrimeNumbers, 2)

    def test_generate_prime_numbers_returns_list(self):
        self.assertTrue(isinstance(generatePrimeNumbers(self.arg_limit), list))
    
    def test_list_returned_contains_values_greater_than_one(self):
        self.assertTrue(all(x >= 2 for x in generatePrimeNumbers(self.arg_limit)))

    def test_generate_prime_numbers_returns_prime_numbers_less_than_arg(self):
        self.assertTrue(all(x < self.arg_limit for x in generatePrimeNumbers(self.arg_limit)))

    def test_generate_prime_numbers_returns_only_prime_numbers(self):
        isPrime = True
        for x in generatePrimeNumbers(self.arg_limit):
            sqrt_value = sqrt(x)
            sample_range = [i for i in self.sample_prime if i < sqrt_value]
            for y in sample_range:
                if x%y == 0:
                    isPrime = False
                    break
        self.assertTrue(isPrime)

if __name__ == '__main__':
    unittest.main()