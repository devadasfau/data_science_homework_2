import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the result of function_B is one of the expected operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            result = function_B()
            self.assertIn(result, operators)

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            # Add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)

            # Check if the generated problem matches the expected problem
            self.assertEqual(problem, expected_problem)

            # Check if the calculated answer matches the expected answer
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
