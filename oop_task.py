class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def get_info(self):
        print(self.name)
        self.name = 4
        print(self.name)


p1 = Person(name='John')
print(p1.name)
p1.get_info()