"""unittest file for base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from json import load, loads, dump, dumps
from os.path import exists
from os import remove


class TestBase(unittest.TestCase):
    """base class test class"""

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        """test initialization"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)
        b5 = Base()

        self.assertAlmostEqual(b1.id + 1, b2.id)
        self.assertAlmostEqual(b5.id, b2.id + 2)
        self.assertAlmostEqual(b2.id - 1, b1.id)

    def test_to_json_string(self):
        """test to_json_string"""
        r1 = Rectangle(10, 7, 2, 8, 5)
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

    def test_saveto_file(self):
        """test save_to_file method"""
        s = Rectangle(10, 7, 2, 8, 1)
        r = Rectangle(7, 8, 4, 4, 4)
        Rectangle.save_to_file([s, r])
        with open("Rectangle.json", "r") as file:
            lis = eval(file.read())
        self.assertListEqual(lis, [{"y": 8, "x": 2, "id": 1,
                                    "width": 10, "height": 7},
                                   {"y": 4, "x": 4, "id": 4,
                                       "width": 7, "height": 8}
                                   ])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            lis = file.read()
        self.assertEqual(lis, "[]")
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            lis = file.read()
        self.assertEqual(lis, "[]")
        s = Square(10, 2, 8, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            lis = eval(file.read())
        self.assertListEqual(
            lis, [{"y": 8, "x": 2, "id": 1, "size": 10}])
        b = Base()

    def test_from_json(self):
        """test from json method"""
        s = Square(4, 10, 12)
        r = Rectangle(10, 10, 10, 10)
        rd = r.to_dictionary()
        sd = s.to_dictionary()
        jdict = Base.to_json_string([sd, rd])
        lis = Base.from_json_string(jdict)
        self.assertEqual(lis[0]['size'], 4)
        self.assertEqual(lis[1]['width'], 10)
        self.assertEqual(len(lis), 2)
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, [{
            'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ])
        self.assertEqual(Base.to_json_string(""), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_create(self):
        """test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)
        s1 = Square(4, 8, 9, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (2) 8/9 - 4")
        self.assertEqual(str(s2), "[Square] (2) 8/9 - 4")

    def test_read_from_file(self):
        """test read from file
        """
        r1 = Rectangle(10, 9, 8, 7)
        r2 = Rectangle(2, 3)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output[0].x, 8)
        self.assertEqual(list_output[1].height, 3)

        r1 = Rectangle(12, 7, 8, 3, 44)
        r2 = Rectangle(24, 23, 19, 1, 5)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        rs = Rectangle.load_from_file()
        self.assertEqual(rs[0].width, 12)
        self.assertEqual(rs[1].id, 5)
        self.assertEqual(rs[1].x, 19)

        try:
            remove('Square.json')
        except:
            pass
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 0)
        self.assertEqual(list, type(list_output))
