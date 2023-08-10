import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    attr_str = ["name", "amenity_id", "place_id", "state_id", "user_id", "city_id",
                "description", "text", "email", "password", "first_name", "last_name"]
    attr_int = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    attr_float = ["latitude", "longitude"]

    def do_create(self, arg):
        if self.valid(arg):
            new = BaseModel()
            storage.save()
            print(new.id)

    def valid(self, arg, _id_flag=False, _att_flag=False):
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
        if len == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if _len == 3 and _att_flag:
            print("** value missing **")
            return False
        return True

    def do_show(self, arg):
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(storage.all()[_key])

    def do_destroy(self, arg):
        if self.valid(arg, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            del storage.all()[_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name\n"""
        args = arg.split()
        _len = len(args)
        my_list = []
        if _len >= 1:
            for key, value in storage.all().items():
                if args[0] in key:
                    my_list.append(str(value))
                else:
                    print("** class doesn't exist **")
                    return
        else:
            for key, value in storage.all().items():
                my_list.append(str(value))
        print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute\n"""
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            match = re.search(r'"([^"]+)"', arg).group(1)
            if args[2] in HBNBCommand.attr_str:
                setattr(storage.all()[_key], args[2], str(match))
            elif args[2] in HBNBCommand.attr_int:
                setattr(storage.all()[_key], args[2], int(match))
            elif args[2] in HBNBCommand.attr_float:
                setattr(storage.all()[_key], args[2], float(match))
            else:
                setattr(storage.all()[_key], args[2], match)

    def do_EOF(self, line):
        """Ctrl-D to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything\n"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
