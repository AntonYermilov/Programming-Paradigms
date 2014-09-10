#!/usr/bin/python3

# PEP 8 -- code style (http://legacy.python.org/dev/peps/pep-0008/)
# PEP 20 -- Zen of Python ( >>> import this)

import random; # 'import' allows to use module in python script
# module provides some useful stuff, read docs for stuff description,
# e.g. http://doc.python.org/3.0/library/random.html

# NB: style is not consistent, logic is moronic for demo purposes

def run_conditions():
    print("== Ifs");
    flip = random.randrange(10)
    if (flip < 3):
        print("Flip = {}".format(flip));
    elif (flip == 3) or (flip == 4):
        print("Flip = {1} or {0}".format(3, 4));
    else:
        print(flip);

    if flip < 5: pass   # do nothing in this branch
    else: print(">= 5");

    print("Flip is " + "even" if flip % 2 == 0 else "odd")

def run_whiles():
    print("== Whiles");
    print("= Plain while");
    i = 0;
    while (i < 5):
        print(i, end=' '); # run help(print) for more params
        i += 1;
    print(); # line break

    print("= While + continue");
    i = 0;
    while i < 10:
        i += 1
        if (i % 2) == 0:
            continue;
        print(i);

    print("= While + break");
    while not False: # or just True
        i = random.randrange(10);
        print(i, end=" ");
        if (i % 3) == 0 and i != 0:
            break;
        print("Try again...");
    print()

# TODO:
#   input
#   big int
#   lists
#   for-loops
#   list slices
#   dictionaries
#   strings
#   functions with several params
#   file reading

if __name__ == "__main__":
    run_conditions();
    run_whiles();
