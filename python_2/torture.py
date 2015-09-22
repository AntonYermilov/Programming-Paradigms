# Example to torture students
# from UC Berkeley CS61a
# (only works in Python 3)


def f(t):
    def g(t):
        def h():
            nonlocal t
            t += 1
        return h, lambda: t
    h, gt = g(0)
    return h, gt, lambda: t

if __name__ == '__main__':
    h, gt, ft = f(0)
    print(ft(), gt()) 
    print(h())
    print(ft(), gt())