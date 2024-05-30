import unittest
from src.list_based_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def test_insert_and_peek(self):
        pq = PriorityQueue()
        pq.insert("A", 3)
        pq.insert("B", 2)
        pq.insert("C", 1)
        pq.insert("D", 4)
        pq.insert("E", 2)

        self.assertEqual(pq.peek(), "D", "Елемент з найвищим пріоритетом повинен бути D")

    def test_insert_and_pop(self):
        pq = PriorityQueue()
        pq.insert("A", 3)
        pq.insert("B", 2)
        pq.insert("C", 1)
        pq.insert("D", 4)
        pq.insert("E", 2)

        self.assertEqual(pq.pop(), "D", "Елемент з найвищим пріоритетом повинен бути D")
        self.assertEqual(pq.pop(), "A", "Наступний елемент з найвищим пріоритетом повинен бути A")
        self.assertEqual(pq.pop(), "B", "Наступний елемент з найвищим пріоритетом повинен бути B")
        self.assertEqual(pq.pop(), "E", "Наступний елемент з найвищим пріоритетом повинен бути E")
        self.assertEqual(pq.pop(), "C", "Наступний елемент з найвищим пріоритетом повинен бути C")

    def test_pop_from_empty_queue(self):
        pq = PriorityQueue()
        with self.assertRaises(Exception) as context:
            pq.pop()
        self.assertTrue('Черга з пріоритетами порожня' in str(context.exception))

    def test_peek_from_empty_queue(self):
        pq = PriorityQueue()
        with self.assertRaises(Exception) as context:
            pq.peek()
        self.assertTrue('Черга з пріоритетами порожня' in str(context.exception))

    def test_order_with_same_priority(self):
        pq = PriorityQueue()
        pq.insert("A", 2)
        pq.insert("B", 2)
        pq.insert("C", 2)

        self.assertEqual(pq.pop(), "A", "Елементи з однаковим пріоритетом повинні повертатись у порядку додавання (A)")
        self.assertEqual(pq.pop(), "B", "Елементи з однаковим пріоритетом повинні повертатись у порядку додавання (B)")
        self.assertEqual(pq.pop(), "C", "Елементи з однаковим пріоритетом повинні повертатись у порядку додавання (C)")


if __name__ == '__main__':
    unittest.main()
