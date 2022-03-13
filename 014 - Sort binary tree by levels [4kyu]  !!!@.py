# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

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

inp1 = """
                1
            8        4
              3        5
                         7
"""

inp2 = """
                1
            2        3
              4        5
                         7
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
    return node.split() if node else []

print(i2)
print(i2.value)  # level 1

print(i2.left.value)  # level 2 left
print(i2.right.value)  # level 2 right

print(i2.left.left.value)  # level 3 left left
print(i2.left.right.value)  # level 3 left left

