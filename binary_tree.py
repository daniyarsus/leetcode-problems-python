class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)



tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

tree.left.left = Node(4)
tree.left.right = Node(5)

preorder(tree)