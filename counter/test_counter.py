"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest
class CounterTest(unittest.TestCase):
    def test_if_same_object(self):
        self.count = Counter()
        self.assertEqual(self.count, Counter())

    def test_count(self):
        self.count = Counter()
        for i in range(3):
            self.count.increment()
        self.assertEqual(3, self.count.count)

    def test_if_counter_continue(self):
        self.count1 = Counter()
        self.count1.increment()
        self.assertEqual(1, self.count1.count)
        self.count2 = Counter()
        self.assertEqual(1, self.count2.count)