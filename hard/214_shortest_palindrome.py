from abc import abstractmethod, ABC

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ...


def get_shortest(data: str, n: int = 0, result: str = "") -> str:
    if n >= len(data):
        return result

    get_shortest(data, n, result)