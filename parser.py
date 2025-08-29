
import re

def parse_equation(equation):
    validate_equation(equation)
    
    if '=' not in equation:
        raise ValueError("Equation must contain '='")
    
    parts = equation.split('=')
    if len(parts) != 2:
        raise ValueError("Equation must have exactly one '=' sign")
    
    left_side, right_side = parts
    
    left_terms = parse_side(left_side)
    right_terms = parse_side(right_side)
    
    result = {}
    for power, coeff in left_terms.items():
        result[power] = result.get(power, 0) + coeff
    
    for power, coeff in right_terms.items():
        result[power] = result.get(power, 0) - coeff
    
    return result

def validate_equation(equation):
    if not equation.strip():
        raise ValueError("Empty equation")
    
    if equation.count('=') != 1:
        raise ValueError("Equation must have exactly one '=' sign")
    
    invalid_chars = set(equation) - set('0123456789+-*.=X^ \t')
    if invalid_chars:
        raise ValueError(f"Invalid characters: {', '.join(invalid_chars)}")
    
    if 'X^' in equation:
        powers = re.findall(r'X\^(-?\d+)', equation)
        for power in powers:
            if int(power) < 0:
                raise ValueError(f"Negative power not allowed: X^{power}")

def parse_side(side):
    terms = {}
    side = side.replace(' ', '')
    
    pattern = r'([+-]?\d*\.?\d*)\*?X\^(\d+)'
    matches = re.findall(pattern, side)
    
    for coeff_str, power_str in matches:
        power = int(power_str)
        
        if coeff_str == '' or coeff_str == '+':
            coeff = 1.0
        elif coeff_str == '-':
            coeff = -1.0
        else:
            coeff = float(coeff_str)
        
        terms[power] = terms.get(power, 0) + coeff
    
    return terms