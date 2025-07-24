class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

def printPreorder(node):
    if node is None:
        return

    print(node.data, end=' ')

    printPreorder(node.left)

    printPreorder(node.right)

def printInorder(node):
    if node is None:
        return

    printInorder(node.left)

    print(node.data, end=' ')

    printInorder(node.right)

def print_postorder(node):
    if node is None:
        return

    print_postorder(node.left)

    print_postorder(node.right)

    print(node.data, end=' ')

# printPreorder(root)
# print("\n")
# printInorder(root)
# print("\n")
# print_postorder(root)