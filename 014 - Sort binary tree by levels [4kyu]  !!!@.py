# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then
root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n



i2 = Node(
    Node(
        None,
        Node(None, None, 4),
        2),
    Node(
        Node(None, None, 5),
        Node(None, None, 6),
        3),
    1)


def tree_by_levels(node):
    if node:
        tree_values = []
        def print_tree(self):
            if self.left:
                print_tree(self.left)
            tree_values.append(self.value)
            if self.right:
                print_tree(self.right)
            return tree_values

        print_tree(node).insert(0, node.value)
        return tree_values
    else:
        return []


x = tree_by_levels(i2)
print(x)
print((tree_by_levels(None)))
