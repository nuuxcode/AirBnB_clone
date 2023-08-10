import cmd

class test(cmd.Cmd):
    prompt="this prompt> "


    def do_create(self, arg):
        print(arg.split())
        len(arg.split())
        print(f"arg1:{arg.split()[0]} arg2:{arg.split()[2]}")
        
    def do_quit(self, line):
        """this the help\n"""
        return True

    def do_EOF(self, line):
        """this the end of file"""
        return True

    def help_quit(self):
        print("NEW HELP FOR QUIT")

    def emptyline(self):
        pass
    
if __name__ == '__main__':
    test().cmdloop()
