#!/usr/bin/python3
"""
    Command Interpreter for Models and Methods
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command line processor class
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """prompts for input again if no command is entered
        """
        return

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the console
        """
        print()
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel and
            prints the id

            Arg:
                arg(cls): BaseModel class
        """
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)
        if (new[0] != "BaseModel"):
            print("** class  doesn't exist **")
            return
        new = eval("{}()".format(new[0]))
        new.save()
        print(new.id)

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based the class name and id
        """
        if (not arg):
            print("** class name missing **")
            return
        
        new = shlex.split(arg)

        if (new[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        if (len(new) < 2 and new[0] == "BaseModel"):
            print("** instance id missing **")
            return

        key = "{}.{}".format(new[0], new[1])
        all_objs = storage.all()
        
        if (all_objs.get(key) is None):
            print("** no instance found **")
            return
        print_str = all_objs[key]
        print(print_str)

    def do_destroy(self, arg):
        """Deletes from JSON file storage an instance of class
        """
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)

        if (new[0] != "BaseModel"):
            print("** class doesn't exist **")
            return
        if (len(new) < 2 and new[0] == "BaseModel"):
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = "{}.{}".format(new[0], new[1])

        if (all_objs.get(key) is None):
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """
            Prints a string representation of all the instances
            of BaseModel
        """
        if (arg and arg != "BaseModel"):
            print("** class doesn't exist **")
            return
        all_objs = storage.all()

        list_instances = [str(all_objs[obj_id]) for obj_id in all_objs.keys()]
        print(list_instances)



if __name__ == "__main__":
    HBNBCommand().cmdloop()
