import itertools

def itertools_examples():
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    booleans = [1, 0, 1, 0, 0, 1]
    numbers = [23, 20, 44, 32, 7, 12]
    decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

    print(list(itertools.chain(letters, booleans, numbers, decimals)))
    print(list(itertools.takewhile(lambda x: x < 15,
                                   itertools.count(10, 0.25))))
    print(list(itertools.compress(letters, booleans)))
    r = itertools.dropwhile(lambda x: x < 5, itertools.repeat(10, 3))
    print(*itertools.filterfalse(lambda x: x % 2, range(10)))
    for i in itertools.islice(itertools.count(), 5, 10):
        print(i)

    def remove_adjacent(lst):
        return [key for key, _ in itertools.groupby(lst)]

    print(remove_adjacent([1, 2, 2, 3, 2]))

    print(*itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)]))
    print(*itertools.product('ABCD', repeat=2))
    print(*itertools.combinations('ABCD', 2))
    print(*itertools.combinations_with_replacement('ABCD', 2))

if __name__ == '__main__':
    itertools_examples()
