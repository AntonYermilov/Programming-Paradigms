from operator import eq as plain_equality

def sqrt(x):
    print("Custom sqrt")
    return 42


def div_ceil(a, b):
    return (a + b - 1) // b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example of common test function


def _test(f, *args, expected=0, eq=plain_equality):
    if not eq(f(*args), expected):
        raise Exception("Math Module: {} test failed".format(f.__name__))

if __name__ == "my_math":  # module is run via "import"
    print("Init my math module")
elif __name__ == "__main__":  # run as plain script
    import sys

    print("Args list: ", sys.argv)
    _test(sqrt, 9, expected=42)
    _test(div_ceil, 5, 2, expected=3)
    _test(div_ceil, 4, 2, expected=2)
    #_test(div_ceil, 4, 2, expected=1); -- failed test
