def foo(*args):
    for i in args:
        print(i)


foo("1", "2", "3", "4", "5", "6", "7", "8", "9")


def foo_2(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


foo_2(key=2, key2=3)


def foo_3(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


foo_3((1, 2, 3), {'1': '2', '2': '3'}, key1='value1', key2='value2')
