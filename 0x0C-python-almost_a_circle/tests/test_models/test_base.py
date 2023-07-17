"""unittest file for base"""


import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """base class test class"""

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
