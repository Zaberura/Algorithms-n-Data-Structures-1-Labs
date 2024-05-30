class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_tree_balanced(node: BinaryTree):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) <= 1 and is_tree_balanced(node.left) and is_tree_balanced(node.right):
        return True
    return False


def test_balance(self):

    root = BinaryTree(40)
    root.left = BinaryTree(20)
    root.right = BinaryTree(50)
    root.left.left = BinaryTree(5)
    root.left.right = BinaryTree(30)
    root.right.left = BinaryTree(45)
    root.right.right = BinaryTree(60)
    root.left.right.left = BinaryTree(25)
    root.left.right.right = BinaryTree(32)
    root.right.right.right = BinaryTree(55)

    self.assertTrue(is_tree_balanced(root))

test_balance()