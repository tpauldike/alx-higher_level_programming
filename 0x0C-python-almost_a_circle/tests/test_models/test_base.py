#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):

    def test_parent_initialization(self):
        """Test parent initialization"""

        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 10)


if __name__ == "__main__":
    unittest.main()
