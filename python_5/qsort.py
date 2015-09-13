from random import choice;
from random import randrange;

def qsort(iterable):
    lst = list(iterable);
    if len(lst) < 2:
        return lst;
    pivot = choice(lst);
    return qsort(filter(lambda x: x < pivot, lst)) + \
           list(filter(lambda x: x == pivot, lst)) + \
           qsort(filter(lambda x: pivot < x, lst));
    
print(qsort([randrange(30) for _ in range(10)]));
