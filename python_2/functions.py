
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
    print("\tTuple(list) enumeration via packing:", end="\n\t");
    for i, el in enumerate(t):
        print("{} -> {}".format(i, el), end="; ");
    print()

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

def multvalue_return():
    def test(a, b): # Yapp, we have nested functions
        if b: # 0 is False in conds
            return a / b, a % b; # tuple packing
        else:
            return "Divisor is 0", "You is stupid" # tuple packing

    print("Multival return DEMO");
    print("\tPlain return:", test(5, 4));
    a, b = test(5, 4);
    print("\tUnpacking: ", a, b);
    print("\tFunction return value isn't strictly typed:\n\t", test(0, 0));
def default_params_test():
    def foo(a, b=True, c=1):
        if b:
            return a + c;

    print("Default Params DEMO")
    print("\tPlain Def params: ", foo(3));
    # NB: b can be value of any type
    print("\tSet explicit params: ", foo(3, 5, 31));
    print("\tParams jumble: ", foo(c="works", b=True, a="It "))
    #foo(c="K", b=True, "O") -- Error: keyword arg must be before non-keyword
    print("\tPartial naming: ", foo(3, c=0));
    print("\tNo-return print:", foo(None, False)); # None!
    #foo(b=True); -- Error
    #foo(1, a=15); -- Error

    def def_list_broken(el, lst=[], prefix="\t"):
        ''' This implementation is broken ''' # doc-string
        lst.append(3);
        return lst;

    # help(def_list_broken) -- Will print doc-string
    print("\t\"Broken\" def_list 1st call:", def_list_broken(3));
    print("\t\"Broken\" def_list 2nd call:", def_list_broken(3), " ?!");

    def def_list_fixed(el, lst=None, prefix="\t"):
        if not lst:
            lst = [];
        lst.append(3);
        return lst;

    print("\tFixed def_list 1st call:", def_list_fixed(3));
    print("\tFixed def_list 2nd call:", def_list_fixed(3));

def varargs_test():
    def foo(a, *args, c, prefix="\t"):
        print(prefix, "a =", a, end="; ");
        print("variadic args = ", end="");
        for arg in args[:-1]:
            print(arg, end=", ");
        last_val = args[-1] if len(args) != 0 else "<empty>";
        print(last_val, end="; ");
        print("c = ", c , ".", sep="");

    print("Varargs DEMO:");
    print("\tNo varargs call:");
    foo(1, c=3); # can pass c only by keyword
    #foo(1, 3); -- Error: c is missed
    print("\tPlain varargs call:");
    foo("a", 1, 2, 3, c="b");
    t = 1, 2, 3
    print("\tPass tuple as varargs:");
    foo("a", t, c="b");
    print("\tPass unpacked tuple as varargs:");
    foo("a", *t, c="b");
    # foo(*t, c="b", a="a"); -- Error: a is specified
    print("\tFirst param bounding:");
    foo(*t, c="b");
    print("\tPass unpacked _string_ as varargs:");
    foo("a", *"str", c="b");
    print("\tPass unpacked _list_ as varargs:");
    foo("a", *[1, 2, 3], c="b");



# TODO: functions
# TODO: modules

if __name__ == "__main__":
    fun_with_tuples();
    multvalue_return();
    default_params_test();
    varargs_test();
