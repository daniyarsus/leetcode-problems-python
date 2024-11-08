class Stack:
    _arr = []

    def add(self, x: int | float) -> None:
        self._arr.append(x)

    def remove_last(self) -> None:
        self._arr.pop()

    def get_all(self) -> list[int | float]:
        return self._arr


s = Stack()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.remove_last()
print(s.get_all())
s.remove_last()
print(s.get_all())
