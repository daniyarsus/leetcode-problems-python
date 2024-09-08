def dataclass(cls: object):
    def greet(self):
        return f"Hello, I am an instance of {self.__class__.__name__}"

    cls.greet = greet
    return cls


@dataclass
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


person = Person("John")
print(person.greet())
