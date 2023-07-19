"""unittest file for base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from json import load, loads, dump, dumps


class TestBase(unittest.TestCase):
    """base class test class"""

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        """test initialization"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base()
        self.assertAlmostEqual(b3.id, 3)
        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)
        b5 = Base()
        self.assertAlmostEqual(b5.id, 4)

    def test_json_string(self):
        """test to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(5, 2, 3, 1)

        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertDictEqual(
            dictionary, {'x': 2, 'width': 10, 'id': 5, 'height': 7, 'y': 8})
        self.assertIsInstance(json_dictionary, str)
        self.assertIsInstance(dictionary, dict)
        self.assertListEqual(
            loads(json_dictionary),
            loads('[{"x": 2, "width": 10, "id": 5, "height": 7, "y": 8}]')
        )

        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertDictEqual(
            dictionary, {'x': 2, 'size': 5, 'id': 1, 'y': 3})
        self.assertIsInstance(json_dictionary, str)
        self.assertIsInstance(dictionary, dict)
        self.assertListEqual(
            loads(json_dictionary),
            loads('[{"x": 2, "size": 5, "id": 1, "y": 3}]')
        )

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string([{'1': 2, 'e': 6}])
        self.assertEqual(json_dictionary, '[{"1": 2, "e": 6}]')
