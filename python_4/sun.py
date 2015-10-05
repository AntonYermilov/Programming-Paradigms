class Runtime:
    pass


class Singleton(Runtime):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class StringBuilder:
    def __init__(self, encoding='utf-8'):
        self.buf = bytearray()
        self.encoding = encoding

    def add(self, s):
        self.buf += bytes(s.encode(self.encoding))
        return self

    def whitespace(self):
        return self.add(' ')

    def newline(self):
        return self.add('\n')

    def build(self):
        return self.buf.decode(self.encoding)


if __name__ == '__main__':
    # runtime
    s1 = Singleton()
    s2 = Singleton()
    if (id(s1) == id(s2)):
        print("Same")
    else:
        print("Different")
    # summary
    # https://waymoot.org/home/python_string/
    sb = StringBuilder()
    result = (sb.add('hello,')
                .whitespace()
                .add('world')
                .add('!')
                .newline()
                .build())
    print(result)
