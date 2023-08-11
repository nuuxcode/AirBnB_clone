#!/usr/bin/python3
""" unit test for bases """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """ class for base test """
    def setUp(self):
        """
        Resets id
        """
        Base._Base__nb_objects = 0

    def test_base_task1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

class RectangleTestCase(unittest.TestCase):
    """ test class for rectangle """
    def setUp(self):
        """
        Resets id
        """
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """ rectangle func """
        #
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        #
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        #12
        r4 = Rectangle(1, 2)
        self.assertEqual(r4.id, 3)
        #13
        r5 = Rectangle(1, 2, 3)
        self.assertEqual(r5.id, 4)
        #14
        r5 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r5.id, 5)
        #15
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        #16
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        #17
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        #18
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        #19
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        #20
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        #21
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        #22
        with self.assertRaises(ValueError):
            Rectangle(0, -2)
        #23
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        #24
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        #25
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        #26
        self.assertEqual(Rectangle(3, 2).area(), 6)
        #27
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(), '[Rectangle] (12) 2/1 - 4/6')


if __name__ == '__main__':
    unittest.main()
