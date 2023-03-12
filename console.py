#!/usr/bin/env python3
"""
Module console HBNBCommand class
"""
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(Cmd):
    classes = {"BaseModel", "User", "Amenity",
               "City", "Place", "Review", "State"}
    Cmd.prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exits the command line
        """
        return True

    def do_help(self, line):
        """Shows list of available commands
        """
        Cmd.do_help(self, line)

    def emptyline(self):
        """No input means nothing happens
        """
        pass

    def do_create(self, line):
        """Creates new instance of BaseModel,
        Saves it to JSON file and prints the id
        """
        if not line.strip():
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints string representation of instance
        based on class name and id
        """
        if not line.strip():
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(args) <= 1:
                print("** instance id missing **")
            else:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])

    def do_destroy(self, line):
        """Deletes instance based on class name and id
        """
        if not line.strip():
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(args) <= 1:
                print("** instance id missing **")
            else:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()

    def do_all(self, line):
        """Prints string representation of all instances
        Can be based on class name
        """
        if not line:
            lst = []
            for key, val in storage.all().items():
                lst.append(str(val))
            print(lst)
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif line in HBNBCommand.classes:
            '''
            dic = {}
            for key in storage.all().keys():
                clss = key.split('.')
                if clss[0] == line:
                    dic[key] = storage.all()[key]
            print(dic)
            '''
            lst = []
            for key, val in storage.all().items():
                clss = key.split('.')
                if line == clss[0]:
                    lst.append(str(val))
            print(lst)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        or updating attribute
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.classes:
                print("** class name doesn't exist **")
            elif len(args) <= 1:
                print("** instance id missing **")
            else:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                elif len(args) <= 2:
                    print("** attribute name missing **")
                elif len(args) <= 3:
                    print("** value missing **")
                elif len(args) >= 4:
                    nw = args[3]
                    nw = nw.strip("'")
                    nw = nw.strip('"')
                    storage.all()[name][args[2]] = nw


if __name__ == '__main__':
    HBNBCommand().cmdloop()
