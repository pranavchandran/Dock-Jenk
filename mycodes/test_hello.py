# Testcase
import unittest
from hello import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_hello_name(self):
        self.assertEqual(hello("John"), "Hello, John!")
    
    def test_hello_name_uppercase(self):
        self.assertEqual(hello("John"), "Hello, John!")


if __name__ == "__main__":
    unittest.main()
