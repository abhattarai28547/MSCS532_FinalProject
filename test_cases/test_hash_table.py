import unittest
from data_structures.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_insert_and_retrieve(self):
        ht = HashTable()
        ht.add_item("product_1", 100)
        self.assertEqual(ht.get_item("product_1"), 100)

if __name__ == "__main__":
    unittest.main()
