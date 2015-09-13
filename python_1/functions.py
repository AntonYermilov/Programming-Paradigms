def fun_with_tuples():
    a, b = 1, 2
    a, b = b, a = a, b
    # a = 2, b = 1. Look for explanation in repo
    print("\tDouble swap: ", a, b)

    t = "", []
    t[1].append(42)
    print("\tTuples are immutable, but elements are mutable: ", t)
    # t[0] += "a" -- Error: You tell we why
    # Hint: t[1] += [42] -- Error

    a, b, *c = 1, 2, 3, 4, 5
    print("\t\"Unpack\" (non-empty tail): ", a, b, c)
    a, b, *c = 1, 2
    print("\t\"Unpack\" (empty tail case): ", a, b, c)
    # a, b, *c, *d = 1, 2, 3 -- Error

    a, b, c = [1, 2, 3]
    print("\tList \"unpacking\": ", a, b, c)
    # a, b = [1,2,3] -- Error
    _, b, _ = 1, 2, 'lol'


def multvalue_return():
    def test(a, b):  # Yapp, we have nested functions
        if b:        # 0 is False in conds
            return a / b, a % b  # tuple packing
        else:
            return "Divisor is 0", "You are stupid"  # tuple packing

    print("Multival return DEMO")
    print("\tPlain return:", test(5, 4))
    a, b = test(5, 4)
    print("\tUnpacking: ", a, b)
    print("\tFunction return value isn't strictly typed:\n\t", test(0, 0))


def default_params_test():
    # def bar(a=1, b): pass; -- Error: non-default args 
    # must be before default ones
    def foo(a, b=True, c=1):
        if b:
            return a + c

    print("Default Params DEMO")
    print("\tPlain Def params: ", foo(3))
    # NB: b can be value of any type
    print("\tSet explicit params: ", foo(3, 5, 31))
    print("\tParams jumble: ", foo(c="works", b=True, a="It "))
    # foo(c="K", b=True, "O") -- Error: keyword arg must be before non-keyword
    print("\tPartial naming: ", foo(3, c=0))
    print("\tNo-return print:", foo(None, False))  # None!
    # foo(b=True); -- Error
    # foo(1, a=15); -- Error

    def append_broken(el, lst=[]):
        ''' This implementation is broken '''
        lst.append(3)
        return lst

    print("\t\"Broken\" append 1st call:", append_broken(3))
    print("\t\"Broken\" append 2nd call:", append_broken(3), " ?!")

    def append_fixed(el, lst=None):
        if not lst:
            lst = []
        lst.append(3)
        return lst

    print("\tFixed append 1st call:", append_fixed(3))
    print("\tFixed append 2nd call:", append_fixed(3))


def varargs_test():
    def foo(a, *args, c, prefix="\t"):
        print(prefix, "a =", a, end="; ")
        print("variadic args = ", end="")
        for arg in args[:-1]:
            print(arg, end=", ")
        last_val = args[-1] if len(args) != 0 else "<empty>"
        print(last_val, end="; ")
        print("c = ", c, ".", sep="")

    print("Varargs DEMO:")
    print("\tNo varargs call:")
    foo(1, c=3)  # can pass c only by keyword
    # foo(1, 3); -- Error: c is missed
    print("\tPlain varargs call:")
    foo("a", 1, 2, 3, c="b")
    t = 1, 2, 3
    print("\tPass tuple as varargs:")
    foo("a", t, c="b")
    print("\tPass unpacked tuple as varargs:")
    foo("a", *t, c="b")
    # foo(*t, c="b", a="a"); -- Error: a is specified twice
    print("\tFirst param bounding:")
    foo(*t, c="b")
    print("\tPass unpacked _string_ as varargs:")
    foo("a", *"str", c="b")
    print("\tPass unpacked _list_ as varargs:")
    foo("a", *[1, 2, 3], c="b")


def kwargs_test():
    def foo(animal, status, prefix="\t"):
        print(prefix, animal, "is", status)

    print("Kwargs DEMO:")
    print("\tPass named params as dictionary")
    args = {"animal": "parrot", "status": "dead"}
    foo(**args)

    def bar(prefix="\t", **kwargs):
        print(prefix, "Given args: ", end="\n\t  ", sep="")
        for key, value in kwargs.items():
            print("{}={}; ".format(key, value), end="")

        print()

    bar(msg="knock", paswd=42, baz=[5])  # NB: arg names are arbitrary


def full_function_syntax(*args, **kwargs) -> int:
    """Function demo with args and kwargs"""
    print(args)
    print(*args)
    print(kwargs)
    d = {'end': '...\n'}
    print(**d)
    return 0

def python_with_statement(filename):
    with open(filename) as f:
        print()

if __name__ == "__main__":
    fun_with_tuples()
    multvalue_return()
    default_params_test()
    varargs_test()
    kwargs_test()
    full_function_syntax(1, 2, 3, name="Valya")

    def def_inside_if():
        pass
