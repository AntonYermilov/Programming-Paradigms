
def fun_with_tuples():
    print("Fun with tuples");
    # Basics
    t1 = 5, 2; # create via packing
    print("\tPacking: ", t1);
    a, b = t1; # unpacking
    print("\tUnpacking: ", a, b);

    a, b = b, a # swap w/o temp. packing + unpacking
    print("\tSwap:", a, b);

    a, b = 1, 2;
    a, b = b, a = a, b;
    print("\tDouble swap: ", a, b); # a = 2, b = 1. Look for explanation in repo

    t = 3,;
    print("\tSinge element tuple: ", t);
    print("\tTuple size: ", len( (a, b, "ping", (3, 7)) ));

    t = 1, "two", (1, 1);
    print("\tElem access: ", t[0], t[-1], t[2][0]);
    for i, el in enumerate(t):
        print("\t {} -> {}".format(i, el));
    # t[3+] -- Index Error
    # t[0] = 3 -- Tuples are immutable, can't change element
    t = "", [];
    t[1].append(42);
    print("\tTuples are immutable, but elements are mutable: ", t);
    # t[0] += "a" -- Error: You tell we why
    # Hint: t[1] += [42] -- Error

    a, b, *c = 1, 2, 3, 4, 5;
    print("\t\"Unpack\" (non-empty tail): ", a, b, c);
    a, b, *c = 1, 2;
    print("\t\"Unpack\" (empty tail case): ", a, b, c);
    # a, b, *c, *d = 1, 2, 3 -- Error

    a, b, c = [1, 2, 3];
    print("\tList \"unpacking\": ", a, b, c);
    # a, b = [1,2,3] -- Error


def multi_value_return(a, b):
    if b != 0:
        return a / b, b % a; # tuple packing
    else:
        return "Divisor is 0", "You is stupid" # tuple packing

# TODO: functions
# TODO: modules

if __name__ == "__main__":
    fun_with_tuples();
    a, b = multi_value_return(5, 2);
#    print(multi_value_return(5, 0));
