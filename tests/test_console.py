import unittest

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class ConsoleTestCase(unittest.TestCase):
    def test_error(self):
        print("")
        cmd_classname = ["create", "update", "show", "destroy"]
        cmd_id = ["update", "show", "destroy"]
        cmd_attr = ["update"]

        """ class name missing """
        for cmd in cmd_classname:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ class doesn't exist """
        class_dont_exist = ["create x", "update x", "show x", "destroy x"]
        for cmd in class_dont_exist:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class doesn't exist **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ instance id missing """
        print("----------------------------")
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().all_class
        for cmd in cmds:
            for clas in all_class:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** instance id missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ no instance found """
        print("----------------------------")
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().all_class
        wrong_id = "x"
        for cmd in cmds:
            for clas in all_class:
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** no instance found **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
                    self.assertCountEqual(expected, f.getvalue().strip())


# python3 -m unittest -v tests/test_console.py
# echo "python3 -m unittest -v tests/test_console.py " | bash
