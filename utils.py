DEBUG_MODE = False

def set_debug_mode(enabled):
    global DEBUG_MODE
    DEBUG_MODE = enabled

def trace_step(message):
    if DEBUG_MODE:
        print(f"[STEP] {message}")

def display_result(terms, degree):
    print(f"Reduced form: {format_polynomial(terms)} = 0")
    print(f"Polynomial degree: {degree}")

def format_polynomial(terms):
    if not terms:
        return "0"
    
    sorted_powers = sorted(terms.keys())
    formatted_terms = []
    
    for i, power in enumerate(sorted_powers):
        coeff = terms[power]
        
        if i == 0:
            if coeff >= 0:
                formatted_terms.append(f"{coeff} * X^{power}")
            else:
                formatted_terms.append(f"{coeff} * X^{power}")
        else:
            if coeff >= 0:
                formatted_terms.append(f"+ {coeff} * X^{power}")
            else:
                formatted_terms.append(f"- {abs(coeff)} * X^{power}")
    
    return " ".join(formatted_terms)