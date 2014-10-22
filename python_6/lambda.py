import random
from functools import partial
from functools import reduce

def fun_with_lambda():
    print("== Intro");
    
    # lambda in python -- expression as a function
    foo = lambda x, y: x + y;
    # Error: foo(3), foo(3, 2, 3)
    print(foo(3, 2));

    foo = lambda x, y=1: x * y;
    print(foo(22), foo(2, 4));
    
    def create_add(n):
        return lambda x: x + n
    
    print(create_add(3)(2));

    print("== Binding");
        
    foo = create_add(1);
    n = 2;
    print(foo(3)); # 5 as expected

    # foo(x) = x + 1
    def create_fadd():
        return lambda x: x + foo(x);

    bar = create_fadd();
    foo = create_add(2);
    print(bar(0)); # 2 -- late binding/dynamic scoping
    # Q: what is closure? (from lects)
    
def function_as_fcc(): # first-class citizen
    print("== FCC");
    # 1. Function can be passed as param
    print(sorted([random.randrange(30) for _ in range(10)],\
                 key=lambda x: x % 10));
    
    # 2. Function can be assigned (stored) and defined as literal
    identity = lambda x: x;
    def add_one(x):
        return x + 1;
    foo = add_one;
    bar = lambda x: x * 2;
    
    # 3. Function can be returned
    def compose(f, g):
        return lambda x: f(g(x));

    print(compose(compose(foo, bar), identity)(1));

def hof_examples(): # higher order functions
    print("== HoF examples");

    gp = [0, 1, 2, 3];
    # map -- modify iterable
    print("Map:", list(map(lambda x: x + 1, gp)));
    # filter -- drop elements
    print("Filter:", list(filter(lambda x: x % 2, gp)));
    # reduce (fold lefl)
    print("Reduce:", reduce(lambda x, y: x + y, gp));
    # partial
    multi_lxor = partial(reduce, lambda x, y: x != y);
    print("Multi LXor:", multi_lxor([False, False, True]))
          
if __name__ == "__main__":
    fun_with_lambda();
    function_as_fcc();
    hof_examples();
