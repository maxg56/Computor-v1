import sys
from parser import parse_equation
from polynomial import reduce_polynomial, get_degree
from solver import solve
from utils import display_result

def main():
    if len(sys.argv) != 2:
        print("Usage: ./computor \"equation\"")
        return
    
    equation = sys.argv[1]
    terms = parse_equation(equation)
    reduced = reduce_polynomial(terms)
    degree = get_degree(reduced)
    
    display_result(reduced, degree)
    solve(reduced, degree)

if __name__ == "__main__":
    main()
