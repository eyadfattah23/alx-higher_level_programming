#!/usr/bin/python3
"""unittest file for Square"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest import mock


class TestSquare(unittest.TestCase):
    """Test Square class"""

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        """test initialization"""
        s1 = Square(10, 10)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Rectangle)
        s1.id = 12
        self.assertAlmostEqual(s1.id, 12)

        with self.assertRaises(TypeError):
            s1 = Square()

        with self.assertRaises(TypeError):
            s1 = Square(10, 10, 10, 10, 10, 10)

    def test_size(self):
        """test square size"""
        with self.assertRaises(TypeError):
            s1 = Square('2')

        with self.assertRaises(TypeError):
            s1 = Square(None)

        with self.assertRaises(ValueError):
            s5 = Square(0)

        with self.assertRaises(ValueError):
            s5 = Square(-1)

        s5 = Square(5)
        self.assertAlmostEqual(s5.size, 5)
        self.assertAlmostEqual(s5.height, 5)
        self.assertAlmostEqual(s5.width, 5)

    def test_xy(self):
        """test x and y coordinates"""
        s = Square(10, 1, 2)
        self.assertAlmostEqual(s.x, 1)
        self.assertAlmostEqual(s.y, 2)
        s.x = 5
        self.assertAlmostEqual(s.x, 5)

        s.y = 5
        self.assertAlmostEqual(s.x, 5)

        s.x = 0
        s.y = 0
        self.assertAlmostEqual(s.x, 0)
        self.assertAlmostEqual(s.x, 0)

        with self.assertRaises(TypeError):
            s.x = 'y'
        with self.assertRaises(ValueError):
            s.x = -5
        with self.assertRaises(TypeError):
            s.y = 'x'
        with self.assertRaises(ValueError):
            s.y = -5

    def test_area(self):
        """test area calculation"""
        r1 = Square(3)
        self.assertAlmostEqual(r1.area(), 9)

    def test_display(self):
        """test display method
        """

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Square(3)
            r.display()
            output = "###\n###\n###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Square(3, 2, 3)
            r.display()
            output = "\n\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Square(3, 3, 2)
            r.display()
            output = "\n\n   ###\n   ###\n   ###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Square(3, 0, 3)
            r.display()
            output = "\n\n\n###\n###\n###\n"
            self.assertEqual(output, ff.getvalue())

        with mock.patch('sys.stdout', new=StringIO()) as ff:
            r = Square(3, 2, 0)
            r.display()
            output = "  ###\n  ###\n  ###\n"
            self.assertEqual(output, ff.getvalue())

        with self.assertRaises(TypeError):
            r.display(5)

    def test_str(self):
        """test str representation"""

        r1 = Square(4, 2, 1, 12)
        r2 = Square(5, 5, 1)
        r2.id = 14
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")
        self.assertEqual(str(r2), "[Square] (14) 5/1 - 5")
        r2.id = 0
        r2.x = 0
        r2.y = 0
        self.assertEqual(str(r2), "[Square] (0) 0/0 - 5")

    def test_update_no_args(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Square(10, 10, 10)
        r1.update()
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_update_args(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Square(10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(89, 2, 3, 4, 5, 8)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_update_kwargs(self):
        """test update method that assigns an argument to each attribute"""
        r1 = Square(10, 10, 10)
        r1.update(size=1)
        self.assertEqual(r1.size, 1)

        r1.update(size=1, x=2)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)

        r1 = Square(10, 10, 10, 8)
        r1.update(edo=5)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.y, 10)

    def test_to_dict(self):
        """test to_dictionary() method"""
        r1 = Square(10, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'size': 10})
        self.assertIsInstance(r1_dictionary, dict)
        r2 = Square(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.size, 10)
        r2 = Square(1, 1)
        with self.assertRaises(TypeError):
            r2.to_dictionary(55)
