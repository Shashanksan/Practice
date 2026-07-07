class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(tokens):
    stack = []

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(Node(token))
        elif token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                return None
            right = stack.pop()
            left = stack.pop()
            node = Node(token)
            node.left = left
            node.right = right
            stack.append(node)
        else:
            return None

    if len(stack) != 1:
        return None

    return stack[0]


def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.value)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if left == "Division by zero" or right == "Division by zero":
        return "Division by zero"

    if root.value == '+':
        return left + right
    elif root.value == '-':
        return left - right
    elif root.value == '*':
        return left * right
    elif root.value == '/':
        if right == 0:
            return "Division by zero"
        return left // right


tokens = input().split()

root = build_tree(tokens)

if root is None:
    print("Invalid expression.")
else:
    result = evaluate(root)
    if result == "Division by zero":
        print("Output: Division by zero")
    else:
        print("Output:", result)