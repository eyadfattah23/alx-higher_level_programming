"""unittest file for rectagle"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle class test class"""

    def test_init(self):
        """test initialization"""
        r1 = Rectangle(10, 10)
        self.assertIsInstance(r1, Base)

    def test_width(self):
        """test width"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, '2')
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 0)
        r6 = Rectangle(10, 5)
        self.assertAlmostEqual(r6.width, 10)

    def test_height(self):
        """test height"""
        with self.assertRaises(TypeError):
            r4 = Rectangle('2', 10)
        with self.assertRaises(ValueError):
            r5 = Rectangle(-1, 10)
        r6 = Rectangle(10, 5)
        self.assertAlmostEqual(r6.height, 5)

    def test_xy(self):
        """test x and y coordinates"""
        r = Rectangle(10, 10, 1, 2)
        self.assertAlmostEqual(r.x, 1)
        self.assertAlmostEqual(r.y, 2)
        r.x = 5
        self.assertAlmostEqual(r.x, 5)

        r.y = 5
        self.assertAlmostEqual(r.x, 5)

        with self.assertRaises(TypeError):
            r.x = 'y'
        with self.assertRaises(ValueError):
            r.x = -5
        with self.assertRaises(TypeError):
            r.y = 'x'
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        """test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)


if __name__ == "__main__":
    unittest.main()
