#!/usr/bin/python3
""" Console module for AirBnB """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the console AirBnB"""
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    attr_str = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]
    attr_int = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    attr_float = ["latitude", "longitude"]

    def do_EOF(self, arg):
        """Ctrl-D to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance :
Usage: create <class name>\n"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if self.valid(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
            storage.save()
            print(new.id)

    def do_clear(self, arg):
        """Clear data storage :
Usage: clear\n"""
        storage.all().clear()
        self.do_all(arg)
        print("** All data been clear! **")

    def valid(self, arg, _id_flag=False, _att_flag=False):
        """validation of argument that pass to commands"""
        args = arg.split()
        _len = len(arg.split())
        if _len == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return False
        if _len < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if _id_flag and args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
            return False
        if _len == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if _len == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        """Prints the string representation of an instance
Usage: show <class name> <id>\n"""
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def do_destroy(self, arg):
        """Deletes an instance
Usage: destroy <class name> <id>\n"""
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
instances based or not on the class name
Usage1: all
Usage2: all <class name>\n"""
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            if args[0] not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def casting(self, arg):
        """cast string to float or int if possible"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute
Usage: update <class name> <id> <attribute name> \"<attribute value>\"\n"""
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            if args[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif args[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = args[3]
            if args[2] in HBNBCommand.attr_str:
                setattr(storage.all()[_key], args[2], str(match))
            elif args[2] in HBNBCommand.attr_int:
                setattr(storage.all()[_key], args[2], int(match))
            elif args[2] in HBNBCommand.attr_float:
                setattr(storage.all()[_key], args[2], float(match))
            else:
                setattr(storage.all()[_key], args[2], self.casting(match))
            storage.save()

    def count(self, arg):
        """the number of instances of a class
Usage: <class name>.count()\n"""
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
        print(count)

    def _exec(self, arg):
        """helper function parsing filtring replacing"""
        methods = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        args = match[0][0]+" "+match[0][2]
        _list = args.split(", ")
        _list[0] = _list[0].replace('"', "").replace("'", "")
        if len(_list) > 1:
            _list[1] = _list[1].replace('"', "").replace("'", "")
        args = " ".join(_list)
        if match[0][1] in methods:
            methods[match[0][1]](args)

    def default(self, arg):
        """default if there no command found"""
        match = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(match) != 0 and match[0][1] == "update" and "{" in arg:
            _dict = re.search(r'{([^}]+)}', arg).group()
            _dict = json.loads(_dict.replace("'", '"'))
            for k, v in _dict.items():
                _arg = arg.split("{")[0]+k+", "+str(v)+")"
                self._exec(_arg)
        elif len(match) != 0:
            self._exec(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
