class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    global index
    if values[index] == -1:
        index += 1
        return None

    node = Node(values[index])
    index += 1
    node.left = build_tree()
    node.right = build_tree()
    return node


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


values = list(map(int, input().split()))
index = 0

root = build_tree()

print("In-Order Traversal:")
inorder(root)
print()

print("Pre-Order Traversal:")
preorder(root)
print()

print("Post-Order Traversal:")
postorder(root)