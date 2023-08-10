import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

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
        if self.valid(arg, True, True):
            args = arg.split()
            _key = args[0]+"."+args[1]
            print(_key)
            print("-----")
            print(storage.all()[_key].to_dict())
            print("+++++")
            print(storage.all()[_key])
            setattr(storage.all()[_key], args[2], args[3])
            print(storage.all()[_key].to_dict())
            
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
