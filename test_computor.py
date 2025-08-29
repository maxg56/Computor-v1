import unittest
from parser import parse_equation
from polynomial import reduce_polynomial, get_degree
from solver import solve
from io import StringIO
import sys

class TestParser(unittest.TestCase):
    def test_basic_parsing(self):
        result = parse_equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
        expected = {0: 4.0, 1: 4.0, 2: -9.3}
        self.assertEqual(result, expected)
    
    def test_simple_equation(self):
        result = parse_equation("1 * X^1 = 0")
        expected = {1: 1.0}
        self.assertEqual(result, expected)
    
    def test_negative_coefficients(self):
        result = parse_equation("-5 * X^2 + 3 * X^1 = 0")
        expected = {1: 3.0, 2: -5.0}
        self.assertEqual(result, expected)

class TestPolynomial(unittest.TestCase):
    def test_reduce_polynomial(self):
        terms = {0: 4.0, 1: 4.0, 2: -9.3}
        result = reduce_polynomial(terms)
        self.assertEqual(result, {0: 4.0, 1: 4.0, 2: -9.3})
    
    def test_remove_zero_coefficients(self):
        terms = {0: 0.0, 1: 4.0, 2: 0.0}
        result = reduce_polynomial(terms)
        self.assertEqual(result, {1: 4.0})
    
    def test_get_degree(self):
        terms = {0: 4.0, 1: 4.0, 2: -9.3}
        self.assertEqual(get_degree(terms), 2)
        
        terms = {0: 4.0, 1: 4.0}
        self.assertEqual(get_degree(terms), 1)
        
        terms = {0: 4.0}
        self.assertEqual(get_degree(terms), 0)

class TestSolver(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def tearDown(self):
        sys.stdout = self.held
    
    def test_degree_0_infinite_solutions(self):
        terms = {}
        solve(terms, 0)
        output = sys.stdout.getvalue()
        self.assertIn("Every real number is a solution", output)
    
    def test_degree_0_no_solution(self):
        terms = {0: 5.0}
        solve(terms, 0)
        output = sys.stdout.getvalue()
        self.assertIn("No solution", output)
    
    def test_degree_1_solution(self):
        terms = {0: 4.0, 1: 2.0}
        solve(terms, 1)
        output = sys.stdout.getvalue()
        self.assertIn("-2", output)
    
    def test_degree_2_positive_discriminant(self):
        terms = {0: 4.0, 1: 4.0, 2: -9.3}
        solve(terms, 2)
        output = sys.stdout.getvalue()
        self.assertIn("strictly positive", output)
    
    def test_degree_too_high(self):
        terms = {3: 1.0}
        solve(terms, 3)
        output = sys.stdout.getvalue()
        self.assertIn("strictly greater than 2", output)

if __name__ == '__main__':
    unittest.main()