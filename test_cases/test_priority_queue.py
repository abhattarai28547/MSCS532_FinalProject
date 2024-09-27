import unittest
from data_structures.priority_queue import FibonacciHeap

class TestPriorityQueue(unittest.TestCase):
    def test_insertion_and_extraction(self):
        pq = FibonacciHeap()
        pq.insert("shipment1", 10)
        pq.insert("shipment2", 5)
        self.assertEqual(pq.extract_min().value, "shipment2")

if __name__ == "__main__":
    unittest.main()
