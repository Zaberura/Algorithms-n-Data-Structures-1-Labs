
class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.prev = None
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            current = self.head
            while current is not None and current.priority >= priority:
                prev = current
                current = current.next

            if current is self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif current is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                prev.next = new_node
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Черга з пріоритетами порожня")

        highest_priority_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return highest_priority_node.value

    def peek(self):
        if self.is_empty():
            raise Exception("Черга з пріоритетами порожня")

        return self.head.value

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(f"({current.value}, {current.priority})")
            current = current.next
        return " -> ".join(result)



