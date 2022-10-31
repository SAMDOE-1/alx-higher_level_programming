#!/usr/bin/python3

"""Defines Test Class for rectangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_default_init(self):
        """Test init method"""
        # test default id, x and y
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_width_validation(self):
        """Test width validations"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("y", 5, 8, 8)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 5, 8, 8)


if __name__ == '__main__':
    unittest.main()
