def to_binary_fraction(a, base=2, digits=100):
    n = len(a)
    a = int(a)
    result = []
    d = 10 ** n
    for _ in range(digits):
        if not a:
            break
        a *= base
        b = a // d
        result.append(b)
        a -= b * d
    return result
