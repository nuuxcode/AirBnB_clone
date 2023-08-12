#!/usr/bin/python3
""" unit test for bases """

import unittest
from models.base_model import BaseModel
import models


class FileStorageTestCase(unittest.TestCase):
    """ class for base test """

    def test_FileStorage_init(self):
        new = BaseModel()
        new.name = "My_First_Model"
        new.my_number = 89
        new.save()
        models.storage.all()
        models.storage.new(new)
        models.storage.save()
        models.storage.reload()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))


if __name__ == '__main__':
    unittest.main()
