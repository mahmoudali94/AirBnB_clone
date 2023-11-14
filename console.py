#!/usr/bin/python3
"""
console.py module
"""
from cmd import Cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(Cmd):
    """
    Interactive command interpreter for HBNB project.

    Attributes:
        prompt: print (hbnb) and
        waiting for the commands
        class_name: Class Attribute list
        classes in Airbnb Project

    Methods:
        do_create(self, args): Create a new
        instance of a class.
        do_show(self, args): Show information
        about an instance.
        do_destroy(self, args): Delete an instance.
        do_all(self, args): Print all instances.
        emptyline(self): Print all instances.
        do_quit(self, args): Quit the command
        interpreter.
        do_EOF(self, args): Exit on EOF (Ctrl+D).
    """
    prompt = "(hbnb) "
    class_name = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review}
    class_fun = ['all', 'show', 'update', 'create']

    def do_create(self, args):
        """
        Create a new instance of a class.

        - create <class name>
        Example:
            create BaseModel
        """
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.class_name.keys():
            new_obj = HBNBCommand.class_name[args_list[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

        # if not args_list:
        #     print("** class name missing **")
        # else:
        #     for arg in args_list[:]:
        #         for key, val in self.class_name.items():
        #             if key == arg.strip():
        #                 obj = self.class_name[key]()
        #                 print(obj.id)
        #                 obj.save()
        #             elif arg not in self.class_name.keys():
        #                 print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show information about an instance.

        - show <class name> <id>
        Example:
            show BaseModel 1234-1234-1234
        """
        args_list = shlex.split(args)

        if len(args_list) < 1:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")

        else:
            id_list = []
            key_list = []

            for key in models.storage.all().keys():
                key_list = key.split('.')[1]
                id_list.append(key_list)

            if args_list[1] in id_list:
                key = ".".join([args_list[0], args_list[1]])
                # key = f"{args_list[0]}.{args_list[1]}"
                obj = models.storage._FileStorage__objects
                try:
                    print(obj[key])
                except Exception:
                    pass
            else:
                return print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance.

        - destroy BaseModel 1234-1234-1234
        Example:
            show <class name> <id>
        """
        args_list = shlex.split(args)

        if len(args_list) < 1:
            print("** class name missing **")
        elif not args_list[0] in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            input_key = f"{args_list[0]}.{args_list[1]}"
            obj = models.storage._FileStorage__objects

            if input_key in obj.keys():
                del obj[input_key]
                models.storage.save()
            else:
                return print("** no instance found **")

    def do_all(self, args):
        """
        Print all instances.

        - destroy <class name> <id>
        Example:
            destroy BaseModel 1234-1234-1234
        """
        args_list = shlex.split(args)
        obj = models.storage._FileStorage__objects

        obj_list = []
        if len(args_list) == 0:
            for val in obj.values():
                obj_list.append(str(val))
            return print(obj_list)
        elif args_list[0] in HBNBCommand.class_name.keys():
            for key, val in obj.items():
                key = key.split(".")[0]
                if args_list[0] == key:
                    obj_list.append(str(val))
            return print(obj_list)
        else:
            return print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute

        - update <class name> <id> <attribute name> "<attribute value>"
        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args_list = shlex.split(args)
        obj = models.storage._FileStorage__objects

        if len(args_list) < 1:
            print("** class name missing **")
        elif not args_list[0] in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            class_key = f"{args_list[0]}.{args_list[1]}"
            if class_key not in obj.keys():
                print("** no instance found **")
            elif len(args_list) < 3:
                print("** attribute name missing **")
            elif len(args_list) < 4:
                print("** value missing **")
            else:
                try:
                    if args_list[3].isdigit():
                        args_list[3] = int(args_list[3])
                    elif args_list[3].replace('.', '').isdigit():
                        args_list[3] = float(args_list[3])

                    obj_dict = obj[class_key]
                    setattr(obj_dict, args_list[2], args_list[3])
                    models.storage.save()
                except Exception:
                    pass

    def default(self, args):
        """text"""
        args_list = args.split(".")

        if args_list[0] in self.class_name.keys():
            fun = args_list[1].split('("')

            if args_list[1].strip('()') == "all":
                self.do_all(args_list[0])
            elif fun[0].strip('') == "show":
                arg1 = fun[0].strip('')
                arg2 = fun[1].rsplit('")')
                id = arg2[0]
                self.do_show({arg1[1]}, {args_list[0]}, {id})
            else:
                pass

    def emptyline(self):
        """Do nothing on empty line."""
        return False

    def do_quit(self, args):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, args):
        """Exit on EOF (Ctrl+D)."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
