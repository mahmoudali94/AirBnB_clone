#!/usr/bin/python3
'''Define class HBNBCommand'''
import cmd
from models import BaseModel, storage, User
from models import Review, State, City, Amenity, Place


class HBNBCommand(cmd.Cmd):
    '''class HBNBCommand'''

    prompt = "(hbnb) "
    className = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}

    def complete_create(self, text, line, begidx, endidx):
        """Custom tab completion for the 'create' command's argument"""
        return [name for name in self.className if name.startswith(text)]

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id'''
        args = line.split()
        if len(args) > 1:
            return
        if not className_errors(args, check_id=False):
            return
        obj = self.className[line]()
        obj.save()
        print(obj.id)

    @staticmethod
    def make_dict():
        '''
        Return a dictionary with the key: id and value: object
        '''
        dic = {}
        all_objs = storage.all()
        for obj in all_objs.values():
            dic[obj.to_dict()["id"]] = obj
        return dic

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class
        name and id'''
        args = line.split()
        if not className_errors(args, check_id=True):
            return
        if args[1] and len(args) == 2:
            dic = self.make_dict()
            if args[1] not in dic:
                print("** no instance found **")
            else:
                print(dic[args[1]])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if not className_errors(args, check_id=True):
            return
        if args[1] and len(args) == 2:
            dic = self.make_dict()
            if args[1] not in dic:
                print("** no instance found **")
            else:
                dic = storage.all()
                del dic[args[0] + "." + args[1]]
                storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not
        on the class name'''
        args = arg.split()
        all_objs = storage.all()
        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in self.className:
            print("** class doesn't exist **")
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])

    def do_update(self, line):
        '''Updates an instance based on the class name and id by adding or
        updating attribute'''
        args = line.split()
        if not className_errors(args, check_id=True):
            return
        if args[1] and len(args) >= 2:
            dic = self.make_dict()
            if args[1] not in dic:
                print("** no instance found **")
            else:
                if len(args) == 2:
                    print("** attribute name missing **")
                else:
                    if len(args) == 3:
                        print("** value missing **")
                    else:
                        obj = dic[args[1]]
                        if args[3][0] == '"':
                            values = args[3].split('"')
                        else:
                            return
                        setattr(obj, args[2], values[1])
                        storage.save()

    def default(self, line):
        '''execute custom command'''
        names = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

        commands = {"all()": self.do_all,
                    "count()": self.do_count,
                    "show()": self.do_show,
                    "destroy()": self.do_destroy,
                    "update()": self.do_update}
        args = line.split('.')
        if args[0] in names and args[1] in commands:
            commands[args[1]](args[0])

    def do_count(self, line):
        ''' retrieve the number of instances of a class'''
        all_objs = storage.all()
        args = line.split()
        count = 0
        for key in all_objs.keys():
            k = key.split('.')
            if k[0] == args[0]:
                count += 1
        print(count)

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program\n'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True


def className_errors(args, check_id):
    '''checks errors to run a validate classname'''
    if len(args) == 0:
        print("** class name missing **")
        return False
    if args[0] not in HBNBCommand.className:
        print("** class doesn't exist **")
        return False
    if len(args) == 1 and check_id:
        print("** instance id missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
