import cmd

class MyConsole(cmd.Cmd):
    prompt = ":) "
    def do_Hello(self, line):
        """Showing the welcome message on our console
        """
        print("Welcome how can I help you today!! ")
  
    def do_exit(self, line):
        """Exiting the console
        """
        print("Exiting the console")
        return True

if __name__ == "__main__":
   MyConsole().cmdloop()
