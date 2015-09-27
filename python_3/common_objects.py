import os
import sys
import string
import random
import itertools


#################################################
# State

balance = 0


def deposit(amount):
    global balance
    balance += amount
    return balance


def withdraw(amount):
    global balance
    balance -= amount
    return balance

#################################################
# Dict like


def make_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    return account['balance']


def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']


# >>> a = make_account()
# >>> b = make_account()
# >>> deposit(a, 100)
# 10
# >>> deposit(b, 50)
# 50
# >>> withdraw(b, 10)
# 40
# >>> withdraw(a, 10)
# 90

#################################################
# Class


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


# >>> a = BankAccount()
# >>> b = BankAccount()
# >>> a.deposit(100)
# 100
# >>> b.deposit(50)
# 50
# >>> b.withdraw(10)
# 40
# >>> a.withdraw(10)
# 90

#################################################
# Inheritance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

# >>> a = MinimumBalanceAccount(0)
# >>> a.deposit(100)
# 100
# >>> b.withdraw(101)
# 'Sorry, minimum balance must be maintained.'


########################################
# Mangling, Exceptions


def generate_id(n=16):
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(random.choice(alphabet) for _ in range(n))


class WithdrawError(Exception):
    """Not enough money"""
    def __init__(self, amount):
        super().__init__()
        self.amount = amount


class BankAccount:
    MAX_BALANCE = 2 ** 64

    def __init__(self):
        self._balance = 0
        self.__id = generate_id()

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise ValueError
        if self._balance < amount:
            raise WithdrawError(amount)
        self._balance -= amount
        return self.balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def get_max_balance():
        return BankAccount.MAX_BALANCE

if __name__ == '__main__':
    a = BankAccount()
    b = a
    c = BankAccount()
    a.deposit(10)
    # BankAccount.deposit(a, 10) # the same
    print('b balance:', b._balance)  # UNACCEPTABLE!
    # print(b.__id) # error, name mangling
    a.get_id = lambda self: self.__id
    # print(a.get_id())  # TypeError
    # print(a.get_id(a)) # AttributeError

    ################################################
    # UNACCEPTABLE!
    # print("b id:", b._BankAccount__id)  # name unmangling

    # static
    BankAccount.MAX_BALANCE = 2 ** 32
    print('max balance:', BankAccount.get_max_balance())
    a.MAX_BALANCE = 2 ** 64
    print('a max: {}, c max: {}'.format(a.MAX_BALANCE,
                                        c.MAX_BALANCE))

    ################################################
    # Exceptions

    # in module import
    try:
        a.withdraw("100")
    except:
        pass
        # UNACCEPTIBLE!
    try:
        a.withdraw(100)
    except WithdrawError as e:
        pass

    try:
        a.withdraw(100)
    except (ValueError, WithdrawError) as e:
        pass
    else:
        pass
    finally:
        print('Finally')

    def tricky():
        try:
            print('Tricky called')
            return 1
        finally:
            print('Tricky finally called')
            return 42
        return 0

    print(tricky())
    # how about with statement?
    # module is object -> import

#################################################
# Operator overloading, Special methods
# https://docs.python.org/3.5/reference/datamodel.html#specialnames

# add path "../python_1/modules/custom" to python system path
sys.path.insert(0, os.path.join(os.pardir, 'python_1', 'modules', 'custom'))
from my_math import gcd


class RationalNumber:
    """
    Rational Numbers with support for arithmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator
        self.simplify()

    def simplify(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)

    def __div__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2, d1*n2)

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    __repr__ = __str__  # why?!


########################################
# Case study iterator


class ReversedList:

    def __init__(self, host):
        self.host = host

    def __iter__(self):
        self.ind = len(self.host)
        return self

    def __next__(self):
        if self.ind == 0:
            raise StopIteration
        self.ind -= 1
        return self.host[self.ind]

if __name__ == "__main__":
    print("-" * 3 + "ReversedList" + "-" * 3)
    rev_list = ReversedList(list(range(10)))
    print(*rev_list)
