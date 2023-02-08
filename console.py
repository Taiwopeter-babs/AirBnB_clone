#!/usr/bin/python3
"""
    Command Interpreter for Models and Methods
"""
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
        obj_cls = new[0]
        if (obj_cls not in HBNBCommand.__classes):
            print("** class  doesn't exist **")
            return
        key = HBNBCommand.__classes[obj_cls]
        new = eval("{}()".format(key))
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
        obj_dict[attribute] = value
        all_objs[obj_key].__dict__.update(obj_dict)

        all_objs[obj_key].save()
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
