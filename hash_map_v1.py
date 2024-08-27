from typing import Any

from pympler import asizeof


class CustomHashMap:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: str | int | float) -> int:
        return hash(key) % self.size

    def insert(self, key: str | int | float, value: Any) -> None:
        if not isinstance(key, (int, float, str)):
            raise TypeError("Key must be int, float, or string!")
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def update(self, key: str | int | float, value: Any) -> None:
        if not isinstance(key, (int, float, str)):
            raise TypeError("Key must be int, float, or string!")
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        raise KeyError(f"Key {key} not found.")

    def get(self, key: str | int | float) -> Any:
        if not isinstance(key, (int, float, str)):
            raise TypeError("Key must be int, float, or string!")
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key: str | int | float) -> None:
        if not isinstance(key, (int, float, str)):
            raise TypeError("Key must be int, float, or string!")
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key {key} not found.")


custom_hash_map = CustomHashMap()
custom_hash_map.insert(key="user_name1", value="bob")
custom_hash_map.insert(key="user_name2", value="bob")
custom_hash_map.insert(key="user_name3", value="bob")
custom_hash_map.insert(key="user_name4", value="bob")
custom_hash_map.insert(key="user_name5", value="bob")
custom_hash_map.insert(key="user_name6", value="bob")
custom_hash_map.insert(key="user_name7", value="bob")
custom_hash_map.insert(key="user_name8", value="bob")

print(f"Full size of custom_hash_map: {asizeof.asizeof(custom_hash_map)} bytes")

base_hash_map = {
    "user_name1": "bob",
    "user_name2": "bob",
    "user_name3": "bob",
    "user_name4": "bob",
    "user_name5": "bob",
    "user_name6": "bob",
    "user_name7": "bob",
    "user_name8": "bob",
}

print(f"Full size of base_hash_map: {asizeof.asizeof(base_hash_map)} bytes")
