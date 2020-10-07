#!/usr/bin/env python3

# Funcionssss...
# This is a normal function declaration


def hello(name):
    """
    This is a function
    """
    print('hello ' + name)


def area(a, b):
    return a * b


hello("ravel")
hello('ravel')
greet = 'hello ravel'
hello(greet)

print(hello.__doc__)

# You can hint about your parameter
# and return type
# def hello(name: str) -> None:
#     doSomething()


def calculate(a, b):
    return a**b


print(calculate(10, 2))


# no_use rather than noUse
def no_use():
    pass


a = no_use()
print(a)


# Optional and required params
def find_area(width, height=10):
    return width * height


# args and kwargs
def any_args(required, *args):
    print(required)
    print(args)


any_args("hello")
any_args("hello ", [1, 2, 3], 1, 2, 3)


def kwars_function(**kwargs):
    print(kwargs)


kwars_function(one=1, two=2)

# scope
name = 'ravel'


def welcome():
    print(name)


def welcome2():
    if True:
        name = 10
    name = 'da xiong'
    print(name)


welcome2()
print(name)
