import math
from fractions import Fraction
from utils import trace_step

def solve(terms, degree):
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return
    
    if degree == 0:
        solve_degree_0(terms)
    elif degree == 1:
        solve_degree_1(terms)
    elif degree == 2:
        solve_degree_2(terms)

def solve_degree_0(terms):
    constant = terms.get(0, 0)
    if constant == 0:
        print("Every real number is a solution.")
    else:
        print("No solution.")

def solve_degree_1(terms):
    a = terms.get(1, 0)
    b = terms.get(0, 0)
    
    if a == 0:
        solve_degree_0(terms)
        return
    
    solution = -b / a
    fraction_solution = Fraction(-b).limit_denominator() / Fraction(a).limit_denominator()
    
    if fraction_solution.denominator == 1:
        print(f"The solution is:\n{fraction_solution.numerator}")
    else:
        print(f"The solution is:\n{fraction_solution}")

def solve_degree_2(terms):
    a = terms.get(2, 0)
    b = terms.get(1, 0)
    c = terms.get(0, 0)
    
    trace_step(f"Coefficients: a={a}, b={b}, c={c}")
    
    if a == 0:
        solve_degree_1(terms)
        return
    
    discriminant = b * b - 4 * a * c
    trace_step(f"Discriminant = b² - 4ac = {b}² - 4×{a}×{c} = {discriminant}")
    
    if discriminant > 0:
        print(f"Discriminant is strictly positive, the two solutions are:")
        sqrt_d = math.sqrt(discriminant)
        trace_step(f"√Δ = √{discriminant} = {sqrt_d}")
        
        sol1 = (-b + sqrt_d) / (2 * a)
        sol2 = (-b - sqrt_d) / (2 * a)
        
        trace_step(f"x₁ = (-b + √Δ) / 2a = ({-b} + {sqrt_d}) / {2*a} = {sol1}")
        trace_step(f"x₂ = (-b - √Δ) / 2a = ({-b} - {sqrt_d}) / {2*a} = {sol2}")
        
        frac1 = format_as_fraction_or_decimal(sol1)
        frac2 = format_as_fraction_or_decimal(sol2)
        
        print(f"{frac1}")
        print(f"{frac2}")
    elif discriminant == 0:
        print("Discriminant is zero, the solution is:")
        solution = -b / (2 * a)
        trace_step(f"x = -b / 2a = {-b} / {2*a} = {solution}")
        
        frac_solution = format_as_fraction_or_decimal(solution)
        print(f"{frac_solution}")
    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        
        trace_step(f"Real part = -b / 2a = {-b} / {2*a} = {real_part}")
        trace_step(f"Imaginary part = √(-Δ) / 2a = √{-discriminant} / {2*a} = {imag_part}")
        
        real_frac = format_as_fraction_or_decimal(real_part)
        imag_frac = format_as_fraction_or_decimal(imag_part)
        
        print(f"{real_frac} + {imag_frac}i")
        print(f"{real_frac} - {imag_frac}i")

def format_as_fraction_or_decimal(value):
    try:
        frac = Fraction(value).limit_denominator(1000)
        if abs(float(frac) - value) < 1e-10:
            if frac.denominator == 1:
                return str(frac.numerator)
            else:
                return str(frac)
        else:
            return str(value)
    except:
        return str(value)