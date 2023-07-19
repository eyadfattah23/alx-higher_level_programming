#!/usr/bin/python3
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

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Rectangle(3, 2, 3, 2)
            r.display()
            output = "\n\n   ###\n   ###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Rectangle(3, 2, 0, 3)
            r.display()
            output = "\n\n\n###\n###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Rectangle(3, 2, 2, 0)
            r.display()
            output = "  ###\n  ###\n"
            self.assertEqual(output, ff.getvalue())

    def test_str(self):
        """test str representation"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        r2.id = 14
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (14) 1/0 - 5/5")
        r2.id = 0
        r2.x = 0
        r2.y = 0
        self.assertEqual(str(r2), "[Rectangle] (0) 0/0 - 5/5")

    def test_update_no_args(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_update_args(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1.update(89, 2, 3, 4, 5, 8)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_kwargs(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

        r1 = Rectangle(10, 10, 10, 10, 8)
        r1.update(edo=5)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.width, 10)

    def test_to_dict(self):
        """test to_dictionary() method"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertIsInstance(r1_dictionary, dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r2.to_dictionary(55)


if __name__ == "__main__":
    unittest.main()
