import sys
from parser import parse_equation
from polynomial import reduce_polynomial, get_degree
from solver import solve
from utils import display_result, set_debug_mode

def main():
    debug_mode = False
    equation = None
    
    if len(sys.argv) == 2:
        equation = sys.argv[1]
    elif len(sys.argv) == 3 and sys.argv[1] == "--steps":
        debug_mode = True
        equation = sys.argv[2]
    else:
        print("Usage: ./computor [--steps] \"equation\"")
        return
    
    set_debug_mode(debug_mode)
    
    if debug_mode:
        print(f"Initial equation: {equation}")
    try:
        terms = parse_equation(equation)
    except Exception as e:
        print(f"Error parsing equation: {e}")
        return

    if debug_mode:
        print(f"Parsed terms: {terms}")
    
    reduced = reduce_polynomial(terms)
    degree = get_degree(reduced)
    
    if debug_mode:
        print(f"After reduction: {reduced}")
        print(f"Calculated degree: {degree}")
    
    display_result(reduced, degree)
    solve(reduced, degree)

if __name__ == "__main__":
    main()
