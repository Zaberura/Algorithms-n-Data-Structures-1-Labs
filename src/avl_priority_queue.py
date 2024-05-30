class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        def _insert(node, value, priority):
            if not node:
                return Node(value, priority)
            elif priority <= node.priority:
                node.left = _insert(node.left, value, priority)
            else:
                node.right = _insert(node.right, value, priority)

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            balance = self._get_balance(node)

            # Left Left Case
            if balance > 1 and priority <= node.left.priority:
                return self._right_rotate(node)

            # Right Right Case
            if balance < -1 and priority > node.right.priority:
                return self._left_rotate(node)

            # Left Right Case
            if balance > 1 and priority > node.left.priority:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

            # Right Left Case
            if balance < -1 and priority <= node.right.priority:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node

        self.root = _insert(self.root, value, priority)

    def remove_max(self):
        if not self.root:
            return None

        def _remove_max(node):
            if not node.right:
                return node, node.left
            else:
                max_node, node.right = _remove_max(node.right)
                return max_node, self._balance(node)

        max_node, self.root = _remove_max(self.root)
        return max_node.value if max_node else None

    def peek(self):
        if self.root:
            return self._find_max(self.root).value
        return None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, z):
        y = z.left
        x = y.right

        y.right = z
        z.left = x

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _left_rotate(self, z):
        y = z.right
        x = y.left

        y.left = z
        z.right = x

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _balance(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node

# Example usage:
if __name__ == "__main__":
    pq = AVLPriorityQueue()

    pq.insert("task1", 3)
    pq.insert("task2", 1)
    pq.insert("task3", 2)

    print("Peek:", pq.peek())  # Should print "task1"

    print("Removed:", pq.remove_max())  # Should print "task1"

    print("Peek:", pq.peek())  # Should print "task3"
