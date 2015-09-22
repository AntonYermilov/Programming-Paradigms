from operator import itemgetter
from collections import defaultdict, Co

# 1


def remove_adjacent(lst):
    return [elem for i, elem in enumerate(lst) if i == 0 or lst[i - 1] != elem]


def linear_merge(a, b):
    result = []

    while a and b:
        result.append(b.pop() if a[-1] < b[-1] else a.pop())

    result.reverse()
    return a + b + result

# 2


def verbing(s):
    if len(s) >= 3:
        s += 'ly' if s.endswith('ing') else 'ing'
    return s


def not_bad(s):
    n, b = s.find('not'), s.find('bad')
    if -1 < n < b:
        return s[:n] + 'good' + s[b + 3:]
    return s


def split_middle(lst):
    middle = (len(lst) + 1) // 2
    return lst[:middle], lst[middle:]


def front_back(a, b):
    a1, a2 = split_middle(a)
    b1, b2 = split_middle(b)
    return a1 + b1 + a2 + b2

# 3


def word_frequences(filename):
    result = defaultdict(int)
    with open(filename) as f:
        for line in f:
            for word in line.lower().split():
                result[word] += 1
    return result


def second(item):
    return item[1]

def print_sorted(filename, amount=None):
    by_freq = bool(amount)
    for word, count in sorted(word_frequences(filename).items(),
                              key=second,
                              reverse=by_freq)[:amount]:
        print(word, count)


def print_words(filename):
    print_sorted(filename)


def print_top(filename):
    print_sorted(filename, 20)


if __name__ == '__main__':
    assert remove_adjacent([]) == []
    assert remove_adjacent([1]) == [1]
    assert remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_adjacent([1, 2, 2, 3, 2]) == [1, 2, 3, 2]
    assert linear_merge([], []) == []
    assert linear_merge([2], []) == [2]
    assert linear_merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert verbing('re') == 're'
    assert verbing('read') == 'reading'
    assert verbing('reading') == 'readingly'
    print("Ok")
