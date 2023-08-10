import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    all_class = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]
    
    def valid(self, arg, id=False):
        args = arg.split()
        if arg:
            print("Input have first argument")
            if arg.split()[0] in HBNBCommand.all_class:
                print("Input have first argument (classname) and it valid")
                if id == True:
                    print("This command need id")
                    if len(arg.split()) < 2:
                        print("** instance id missing **")
                    else:
                        print("Input have second argument (id)")
                        Key = '.'.join(arg.split()[:2])
                        if Key in storage.all():
                            print("Object with this id exist")
                            return True
                        else:
                            print("** no instance found **")
                else:
                    print("This command dont need id")
                    return True
            else:
                print("Input have first argument (classname) and it NOT valid")
                print("** class doesn't exist **")
        else:
            print("Input dont first argument")
            print("** class name missing **")
        return False

    def do_create(self, arg):
        """Creates a new instance, saves it (to the JSON file) and prints the id\n"""
        if self.valid(arg):
            new = BaseModel()
            print(new.id)
            new.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id\n"""
        if self.valid(arg, True):
            Key = '.'.join(arg.split()[:2])
            print(f"\nThis the type of return storage.all():\n{type(storage.all())}\n this type for the value of one of key of storage.all():\n{type(storage.all()[Key])}\n")
            print(storage.all()[Key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id\n"""
        if self.valid(arg, True):
            Key = '.'.join(arg.split()[:2])
            del storage._FileStorage__objects[Key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name\n"""
        output_list = []
        if arg:
            if arg.split()[0] in HBNBCommand.all_class:
                for key, value in storage.all().items():
                    if arg.split()[0] in key:
                        output_list.append(str(value))
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                    output_list.append(str(value))
        print(output_list)


    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute\n"""
        if self.valid(arg, True):
            Key = '.'.join(arg.split()[:2])
            del storage._FileStorage__objects[Key]
            storage.save()

    def do_EOF(self, line):
        """Ctrl-D to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn’t execute anything\n"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

"""
TODO
change the way the class doesnt exist error
you should loop through objects and if u didnt find it then u show error


"""
