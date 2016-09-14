#!/usr/bin/env python3

import re
import collections
import itertools


def re_examples():
    # email
    simple_email_regex = re.compile("\w+@(\w+\.)+\w+")
    words = re.compile("\w+")
    found = words.match("Hello, Re!")
    regex = re.compile("(\w+)\W+\1$")
    if found:
        print(found.start(), found.end())
    print(words.match("Hello, Re!", endpos=0))
    print(words.match("Hello, Re!", pos=7).span())

    p = re.compile('(a(b)*c)d')
    print("group example")
    print(p.match('abbbcd').group(0))
    print(p.match('acd').group(0, 1, 0))
    print(p.match('abcd').groups())

    p = re.compile(r'(\b\w+)\s+\1')  # boundary, word, whitespace, \1
    print(p.search('Word repeated twice twice').group())
    print(re.sub("not.*good", 'bad', "Homework is not so good, not good!"))
    p = re.compile("not.*?good")
    print(p.sub('bad', "Homework is not so good, not good!",
                count=2))

    p = re.compile('\W+')
    print(p.split('Students, welcome to re world!'))
    print(p.findall('Students, welcome to re world!'))

    russian = re.compile('[а-яА-Я]+')
    print(russian.findall('Привет из России'))

    charref = re.compile("""
 &[#]                # Comment starts with #
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | 0x[0-9a-fA-F]+  # Hexadecimal form
""", re.VERBOSE)
    print(charref.findall("123 012347 0xdeadbeef hello"))
    print(re.search('Vladimir(?! Putin)', 'Vladimir ').group())
    # Real world example IPv4
    # ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
    # (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$


def collections_examples():
    # namedtuple
    rgb = collections.namedtuple('Colour', ['red', 'green', 'blue'])
    blue = rgb(0, 0, 255)
    red = rgb(red=255, green=0, blue=0)
    red_component, _, _ = blue
    print(blue, red.red, red_component)

    # Counter
    c = collections.Counter('abracadabra')
    print(list(c.elements()))
    print(c.most_common(3))

    c2 = collections.Counter('abbas')
    c.subtract(c2)
    print(c.most_common())

    # deque
    # works in linear time
    def print_moving_average(sequence, n=3):
        d = collections.deque(sequence[:n])
        d.appendleft(0)
        s = sum(d)
        for elem in sequence[n:]:
            s += elem - d.popleft()
            d.append(elem)
            print(s / n)
    print_moving_average(range(10))

    # defaultdict
    d = collections.defaultdict(lambda: '<missing>')
    d.update(name='Homework 2', action='is')
    print("{name} {action} {object}!".format(**d))
    print("{0} {1} {0}!".format(1, 2))

    # OrderedDict
    d = collections.OrderedDict(hello=1, world=3)
    d['!'] = 3
    print(d.popitem(last=True))
    d.move_to_end('hello')
    print(d.popitem(last=False))

def yield_examples():
    def yield_example():
        i = 0
        while True:
            yield i
            i += 1

    a = yield_example()
    print('yield example')
    for i, e in enumerate(a):
        if i >= 10:
            break
        print(e)

    print("generator example:")
    generator_example = (i*i for i in range(1, 10))
    for i in generator_example:
        print('\t', i, end=' ')
    print()

if __name__ == '__main__':
    re_examples()
    collections_examples()
    yield_examples()
