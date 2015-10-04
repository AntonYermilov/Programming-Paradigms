def add_layer(food):
    print(food)


def cutlet():
    add_layer("--котлета--")


def tomatos():
    add_layer("#помидоры#")


def make_hamburger(food):
    add_layer("</------\>")
    tomatos()
    cutlet()
    add_layer("<\______/>")


# Decorators to the rescue!
def bread(func):
    def wrapper(*args, **kwargs):
        add_layer("</------\>")
        func(*args, **kwargs)
        add_layer("<\______/>")
    return wrapper


def tomato(func):
    def wrapper(*args, **kwargs):
        add_layer("#помидоры#")
        func(*args, **kwargs)
    return wrapper


# порядок важен!
@bread
@tomato
def hamburger(food="--котлета--"):
    add_layer(food)

# hamburger = bread(tomato(hamburger))


def cheese(func):
    def wrapper(*args, **kwargs):
        add_layer("***сыр***")
        func(*args, **kwargs)
    return wrapper


@bread
@tomato
@cheese
def cheesburger(food="--котлета--"):
    add_layer(food)


def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap


@decoratorFunctionWithArguments('hello', 1, ("A", 5))
def hello_world():
    print('world')


class Foo:
    @staticmethod
    def bar():
        print("bar")

if __name__ == '__main__':
    print("hamburger:")
    hamburger()
    print("\nvegetarian cheesburger:\n")
    cheesburger("---соя---")
    hello_world()

    # real world: html tags <b><i> </i></b>
    #             staticmethod, ...
    Foo.bar()
