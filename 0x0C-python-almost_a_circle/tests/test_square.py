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
