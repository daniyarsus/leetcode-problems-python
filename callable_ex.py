def foo(info: str = None):
    if callable(info):
        print(info)
    else:
        print("Not callable")
