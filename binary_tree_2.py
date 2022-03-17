from binarytree import build

class Node:
    def __init__(self, n, L, R):
        self.value = n
        self.left = L
        self.right = R

tree = Node(1, Node(2, Node(4, Node(8, None, None), Node(9, None, None)), Node(5, Node(10, None, None), None)), Node(3, Node(6, None, None), Node(7, None, None)))
"""
                1
        2               3
   4        5         6    7
8   9    10
"""

print(list(tree)