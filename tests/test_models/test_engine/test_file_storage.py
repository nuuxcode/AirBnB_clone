#!/usr/bin/python3
""" unit test for bases """

import unittest
from models.base_model import BaseModel
import models
import json
import os


class FileStorageTestCase(unittest.TestCase):
    """ class for base test """

    def test_FileStorage_init(self):
        """ DOC DOC DOC """
        filepath = models.storage._FileStorage__file_path
        _objs = models.storage._FileStorage__objects
        """check class attr"""
        self.assertEqual(filepath, "file.json")
        self.assertIsInstance(filepath, str)
        self.assertIsInstance(_objs, dict)
        new = BaseModel()
        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """test all"""
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(models.storage.all(), {})
        """existence id"""
        self.assertTrue(hasattr(new, "id"))
        self.assertIsInstance(new.id, str)

        """new"""
        keyname = "BaseModel."+new.id
        self.assertIsInstance(models.storage.all()[keyname], BaseModel)
        self.assertEqual(models.storage.all()[keyname], new)
        """ check if object exist by keyname """
        self.assertIn(keyname, models.storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[keyname] is new)

        """save"""
        models.storage.save()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by keyname """
        self.assertIn(keyname, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[keyname], new.to_dict())

        """reload"""
        models.storage.all().clear()
        models.storage.reload()
        with open(filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[keyname],
                         models.storage.all()[keyname].to_dict())

        """file"""
        if os.path.exists(filepath):
            os.remove(filepath)
        self.assertFalse(os.path.exists(filepath))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
