class Node:
    def __init__(self, n, L, R):
        self.value = n
        self.left = L
        self.right = R

tree = Node(1, Node(2, Node(4, Node(8, None, None), Node(9, None, None)), Node(5, Node(10, None, None), None)), Node(3, Node(6, None, None), Node(7, None, None)))

inorder_tree = []
def inorder(node):
    if node:
        inorder(node.left)
        inorder_tree.append(node.value)
        inorder(node.right)
    return inorder_tree

preorder_tree = []
def preorder(node):
    if node:
        preorder_tree.append(node.value)
        preorder(node.left)
        preorder(node.right)
    return preorder_tree

print(inorder(tree))
print(preorder(tree))
