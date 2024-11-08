class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("fuck")

    def __repr__(self):
        return self.name

    def __enter__(self):
        print("hohoho")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val)


print(Person("name"))

del Person