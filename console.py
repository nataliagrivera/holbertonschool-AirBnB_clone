#!/usr/bin/python3
"""Module that defines class HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_help(self, arg):
        """Display help message"""
        super().do_help(arg)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to a JSON file, and print the ID"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.all_classes()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and ID"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances based on the class name"""
        args = arg.split()
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in storage.all_classes():
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all_classes()[args[0]].all()])

    def do_update(self, arg):
        """Updates an instance based on the class name and ID by adding or updating an attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all_classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
