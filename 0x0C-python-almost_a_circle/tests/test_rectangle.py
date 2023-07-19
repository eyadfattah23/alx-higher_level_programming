"""unittest file for rectagle"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest import mock


class TestRectangle(unittest.TestCase):
    """Rectangle class test class"""

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        """test initialization"""
        r1 = Rectangle(10, 10)
        self.assertIsInstance(r1, Base)
        r1.id = 12
        self.assertAlmostEqual(r1.id, 12)

        with self.assertRaises(TypeError):
            r1 = Rectangle()

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 10, 10, 10, 10)

    def test_height(self):
        """test height"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, '2')
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, None)
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, [5])

        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r5 = Rectangle(10, -1)
        r6 = Rectangle(10, 5)
        self.assertAlmostEqual(r6.height, 5)

    def test_width(self):
        """test width"""
        with self.assertRaises(TypeError):
            r4 = Rectangle('2', 10)
        with self.assertRaises(TypeError):
            r5 = Rectangle(None, 10)

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r5 = Rectangle(-1, 10)
        r6 = Rectangle(10, 5)
        self.assertAlmostEqual(r6.width, 10)

    def test_xy(self):
        """test x and y coordinates"""
        r = Rectangle(10, 10, 1, 2)
        self.assertAlmostEqual(r.x, 1)
        self.assertAlmostEqual(r.y, 2)
        r.x = 5
        self.assertAlmostEqual(r.x, 5)

        r.y = 5
        self.assertAlmostEqual(r.x, 5)

        r.x = 0
        r.y = 0
        self.assertAlmostEqual(r.x, 0)
        self.assertAlmostEqual(r.x, 0)

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

    def test_display(self):
        """test display method
        """

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Rectangle(3, 3)
            r.display()
            output = "###\n###\n###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Rectangle(3, 2, 2, 3)
            r.display()
            output = "\n\n\n  ###\n  ###\n"
            self.assertEqual(output, ff.getvalue())

    def test_str(self):
        """test str representation"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == "__main__":
    unittest.main()
