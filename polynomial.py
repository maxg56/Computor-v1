def reduce_polynomial(terms):
    cleaned = {}
    for power, coeff in terms.items():
        if coeff != 0:
            cleaned[power] = coeff
    return cleaned

def get_degree(terms):
    if not terms:
        return 0
    return max(terms.keys())