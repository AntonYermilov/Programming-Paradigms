class LowerAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        lower_attr = dict((name.lower(), value) for name, value in dct.items())
        return super().__new__(cls, name, bases, lower_attr)

class TestClass(metaclass=LowerAttrMetaclass):
    camelCaseField = 2
    def PascalCaseMethod():
        pass
    def testPascalMethod():
        TestClass.PascalCaseMethod()

# class RegexClass(metaclass=YourMetaclass):
#     regex = "(abc)*c"

# a = RegexClass()
# a.regex.match("")

class A(object):
    ...

def init(self):
    self.a = 2

A  = type('A', (object,), {"__init__": init})
B  = type('B', (object,), {})
C  = type('C', (object,), {})
D  = type('D', (object,), {})
E  = type('E', (object,), {})
K1 = type('K1', (A, B, C), {})
K2 = type('K2', (D, B, E), {})
K3 = type('K3', (D, A), {})
Z  = type('Z', (K1, K2, K3), {})

if __name__ == '__main__':
    t = TestClass()
    print(hasattr(TestClass, 'camelCaseField'))
    print(hasattr(t, 'PascalCaseMethod'))
    print(hasattr(t, 'camelcasefield'))
    print(hasattr(t, 'pascalcasemethod'))
    TestClass.testpascalmethod()
