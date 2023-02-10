#!/usr/bin/env python3
"""Entry to the program
"""

import cmd
from models.base_model
import BaseModel

class HBNBCommand(cmd.Cmd):
    """cmd class
    """
    prompt = "(hbnb) "

    def do _create(self, line):
        """Creates a class instance
        """
        if not line:
            print("** class name missing **")
        else:
            class_dict = {"BaseModel":BaseModel}
            if line not in class_dict:
                print("** class doesn't exist **")
            else
            my_model = class_dict[line]()
            my_model.save{}
            print(my_model.id)

            def do_show(self, line)
            """prints the string repr of an instance
            """
            my_list = parse(line)
            if len(my_list) = = 0:
                print ("**

    def do_EOF(self, line):
        """Command to end the program
        """
        return True

    def do_quit(self, line):
        """Command to end the program
        """
        return True

    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
