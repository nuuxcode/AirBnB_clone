#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ class for base test """
    print()

    def setUp(self):
        # Open and truncate the file to make it empty
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        print(printed_output)

    def test_basemodel_init(self):
        new = BaseModel()

        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """existince"""
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """type test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

        """ check if save in storage """
        keyname = "BaseModel."+new.id
        """ check if object exist by keyname """
        self.assertIn(keyname, models.storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[keyname] is new)

        """ Test update """
        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        """check if save() update update_at time change"""
        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

        """ check if init it call: models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if it save in json file"""
        keyname = "BaseModel."+new.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by keyname """
        self.assertIn(keyname, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_basemodel_init2(self):
        _dict = {
            "BaseModel.45df704f-32b8-4aaf-8b60-ec589777338f": {
                "id": "45df704f-32b8-4aaf-8b60-ec589777338f",
                "created_at": "2023-08-11T20:15:11.070879",
                "updated_at": "2023-08-11T20:15:11.070914",
                "name": "My First Model",
                "my_number": 89,
                "__class__": "BaseModel"
            }
        }
        keyname = "BaseModel.45df704f-32b8-4aaf-8b60-ec589777338f"
        new2 = BaseModel(**_dict)
        print(new2.to_dict())
        """ check if it have methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """existince"""
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertFalse(hasattr(new, "__class__"))

        """check value"""
        """self.assertEqual(new.id, "45df704f-32b8-4aaf-8b60-ec589777338f")
        format = "%Y-%m-%dT%H:%M:%S.%f"
        createat = datetime.strptime(_dict[keyname].c, format)
        self.assertEqual(new.created_at, createat)"""
        print(_dict[keyname].created_at)
        """type test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

        """ check if save in storage """
        keyname = "BaseModel."+new.id
        """ check if object exist by keyname """
        self.assertIn(keyname, models.storage.all())
        """ check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[keyname] is new)

        """ Test update """
        new.name = "My First Model"
        new.my_number = 89

        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        """check if save() update update_at time change"""
        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)

        """ check if init it call: models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if it save in json file"""
        keyname = "BaseModel."+new.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by keyname """
        self.assertIn(keyname, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[keyname], new.to_dict())

        ############################


if __name__ == '__main__':
    unittest.main()
