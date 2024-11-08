from functools import singledispatch


@singledispatch
def math_operand(n):
    ...


@math_operand.register(int)
def _(n):
    print(type(n))


if __name__ == '__main__':
    math_operand(3)
