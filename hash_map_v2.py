from typing import Any

key = "bob"
print(key)
print(hash(key))


class HashMap:
    def __init__(
            self,
            size: int = 10
    ) -> None:
        self.size = size
        self.hash_map = [None] * self.size

    def get_hash(
            self,
            key: int | float | str
    ) -> hash:
        if not isinstance(key, (int, float, str)):
            raise TypeError("Key must be int or float or string!")
        return hash(key) % self.size

    def add(
            self,
            key: int | float | str,
            value: Any
    ) -> None:
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.hash_map[key_hash] is None:
            self.hash_map[key_hash] = list([key_value])
        else:
            for pair in self.hash_map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    break
            self.hash_map[key_hash].append(key_value)


hash_map = HashMap()
hash_map.add(key=1, value=2)
print(hash_map.size)
