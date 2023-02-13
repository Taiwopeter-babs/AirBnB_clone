#!/usr/bin/python3
"""
    Command Interpreter for Models and Methods
"""
import re
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command line processor class
    """

    prompt = "(hbnb) "

    __classes = {"BaseModel": "BaseModel", "User": 'User', "State": 'State',
                 "City": 'City', "Place": 'Place', "Amenity": 'Amenity',
                 "Review": 'Review'}
    __methods = {"all()": "all", "count()": "count", "show": "show",
                 "destroy": "destroy"}

    def emptyline(self):
        """prompts for input again if no command is entered
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help documentation for do_quit command"""
        help_text = "Quit command to exit the program\n"
        print(help_text)

    def do_EOF(self, arg):
        """EOF (Ctrl + D) to exit the console"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel and
        prints the id
        """
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)
        obj_cls = new[0]
        if (obj_cls not in HBNBCommand.__classes):
            print("** class  doesn't exist **")
            return
        key = HBNBCommand.__classes[obj_cls]
        new = eval("{}()".format(key))
        new.save()
        print(new.id)

    def help_show(self):
        """Help for [show] command"""
        text = "Prints information about an object from storage"\
               " based on the class name and id"\
               "\nExample: (prompt) show ClassName id\nobj displayed on next"\
               " line"
        print(text)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based the class name and id: show ClassName id
        """
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)
        obj_cls = new[0]

        if (obj_cls not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return
        if (len(new) < 2):
            print("** instance id missing **")
            return

        key = HBNBCommand.__classes[obj_cls]
        obj_id = new[1]

        obj_key = "{}.{}".format(obj_cls, obj_id)
        all_objs = storage.all()

        if (all_objs.get(obj_key) is None):
            print("** no instance found **")
            return
        print_str = all_objs[obj_key]
        print(print_str)

    def do_destroy(self, arg):
        """Deletes from JSON file storage an instance of class
        """
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)
        obj_cls = new[0]

        if (obj_cls not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return
        if (len(new) < 2):
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_id = new[1]

        obj_key = "{}.{}".format(obj_cls, obj_id)

        if (all_objs.get(obj_key) is None):
            print("** no instance found **")
            return
        del all_objs[obj_key]
        storage.save()

    def do_all(self, arg):
        """
            Prints a string representation of all the instances
            of BaseModel
        """
        all_objs = storage.all()
        cls_based_list = []

        if (arg):
            if (arg not in HBNBCommand.__classes):
                print("** class doesn't exist **")
                return
            else:
                for obj_id in all_objs.keys():
                    class_and_id = obj_id.split(".")
                    if class_and_id[0] == arg:
                        cls_based_list.append(str(all_objs[obj_id]))
                print(cls_based_list)
        else:
            list_instances = [str(all_objs[obj_id]) for obj_id in
                              all_objs.keys()]
            print(list_instances)

    def do_update(self, arg):
        """Updates an instance of class specified in arg"""
        if (not arg):
            print("** class name missing **")
            return

        new = shlex.split(arg)
        all_objs = storage.all()

        obj_cls = new[0]
        if (obj_cls not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return
        if (len(new) == 1):
            print("** instance id missing **")
            return

        # check existence of object id
        obj_id = new[1]
        obj_key = "{}.{}".format(obj_cls, obj_id)
        if (all_objs.get(obj_key) is None):
            print("** no instance found **")
            return

        if (len(new) == 2):
            print("** attribute name missing **")
            return
        if (len(new) == 3):
            print("** value missing **")
            return

        attribute = new[2]
        value = new[3]

        obj_dict = dict(all_objs[obj_key].__dict__)

        if hasattr(all_objs[obj_key], new[2]):
            cast = str(type(getattr(all_objs[obj_key], new[2])).__name__)
            obj_dict[attribute] = eval("{}({})".format(cast, value))
            all_objs[obj_key].__dict__.update(obj_dict)

        else:
            obj_dict[attribute] = value
            all_objs[obj_key].__dict__.update(obj_dict)

        all_objs[obj_key].save()
        storage.save()

    def do_count(self, arg):
        """Counts the number of instances based on a class"""
        all_objs = storage.all()
        instance_count = 0

        for obj_id in all_objs.keys():
            cls_id = obj_id.split(".")
            cls_name = cls_id[0]

            if (cls_name == arg):
                instance_count += 1
        print(instance_count)

    def onecmd(self, line):
        """defines user input as a shortcut for do_xxx methods"""

        try:
            cmds = line.split(".")
            cmd1 = cmds[0]  # do_xx if len(cmd) == 1, otherwise a class
            cmd2 = cmds[1]  # do_xx if len(cmds) > 1
        except IndexError:
            pass

        if len(cmds) == 1:
            line = "{}".format(cmd1)
        elif len(cmds) > 1:
            if cmd1 in HBNBCommand.__classes:
                try:
                    cmd_and_id = [arg for arg in re.split(r'[()]', cmd2)
                                  if arg.strip]
                    cmd_do = cmd_and_id[0]
                    id_do = cmd_and_id[1]
                except IndexError:
                    pass

                if cmd_do and id_do:
                    line = "{} {} {}".format(HBNBCommand.__methods[cmd_do],
                                             cmd1, id_do)
                else:
                    line = "{} {}".format(HBNBCommand.__methods[cmd2],
                                          cmd1)
        r = super(HBNBCommand, self).onecmd(line)
        return r


if __name__ == "__main__":
    HBNBCommand().cmdloop()
