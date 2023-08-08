import cmd

class MyCmd(cmd.Cmd):
    intro = "Welcome to My Command Interpreter. Type 'help' to list commands."
    prompt = "(MyCmd) "
    file = None  # If you want to read commands from a file, you can set the file attribute here.

    def do_greet(self, line):
        """Greet the user."""
        print("Hello, user!")

    def do_add(self, line):
        """Add two numbers."""
        try:
            num1, num2 = map(int, line.split())
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is: {result}")
        except ValueError:
            print("Please provide two integers separated by space.")

    def do_quit(self, line):
        """Quit the command interpreter."""
        print("Goodbye!")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == "__main__":
    my_cmd = MyCmd()
    my_cmd.cmdloop()
