#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):

    def test_rectangle_inheritance(self):
        """Test Frist Rectangle"""

        b1 = Rectangle(10, 4)
        b3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(b1.id, 2)
        self.assertAlmostEqual(b3.id, 12)

    def test_rectangle_area(self):
        """Test Rectangle area"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 4, 0, 0, 10)
        self.assertAlmostEqual(r1.area(), 20)
        self.assertAlmostEqual(r2.area(), 12)

    def test_display_rectangle_area(self):
        """Test Display Rectangle area"""


if __name__ == "__main__":
    unittest.main()
