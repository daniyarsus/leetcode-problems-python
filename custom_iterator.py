class CustomIterator:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

        self.current = 1
        self.temp = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_size:
            num = self.current
            self.current += 1
            self.temp.append(num)
            return num
        else:
            raise StopIteration

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.temp


custom_array = []

for i in CustomIterator(5):
    print(i)
