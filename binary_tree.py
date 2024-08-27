# 10, 5, 7, 16, 13, 2, 20

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def __find(self, node, parent, value):
        pass

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj)