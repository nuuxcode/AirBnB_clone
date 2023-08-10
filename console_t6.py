import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        args = arg.split()
        print(args)
        _len = len(arg.split())
        if _len == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return
        new = BaseModel()
        storage.save()
        print(new.id)

    def do_show(self, arg):
        
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
