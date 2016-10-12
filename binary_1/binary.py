def to_binary_fraction(a, base=2, digits=100):
    a = str(a)
    d = 10 ** (len(a))
    a = int(a)
    result = []
    for _ in range(digits):
        if not a:
            break
        a *= base
        b, a = divmod(a, d)
        result.append(b)
    return result
