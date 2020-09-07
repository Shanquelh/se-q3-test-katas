import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(3, 2), 5)
        self.assertEqual(katas.add(220, 30), 250)
        self.assertEqual(katas.add(-7, 3), -4)
    
    def test_multiply(self):
        self.assertEqual(katas.multiply(6, 3), 18)
        self.assertEqual(katas.multiply(10, 8), 80)
        self.assertEqual(katas.multiply(12, 12), 144)
    
    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)
        self.assertEqual(katas.power(4, 4), 256)
        self.assertEqual(katas.power(3, 3), 27)

    def test_factorial(self):
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(13), 144)
        self.assertEqual(katas.fibonacci(8), 13)
        self.assertEqual(katas.fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
