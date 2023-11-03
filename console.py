#!/usr/bin/python3
"""Module that defines class HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


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
        elif arg not in globals() or not \
            issubclass(globals()[arg], BaseModel):
            print("** class doesn't exist **")
        
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and ID"""
        args = arg.split()
        if not arg:
            # check if arg is empty
            print("** class name missing **")
            return
            # check if class name exists
        elif args[0] not in globals() or not \
            issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        # check if id is empty
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            #concatenate class name and id
            key = args[0] + '.' + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID"""
        # split arg into list of arguments
        args = arg.split()
        # check if arg is empty
        if not arg:
            print("** class name missing **")
            #checks if class name exists
        elif args[0] not in globals() or not \
            issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            # check if id is empty
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            # concatenate class name and id
            key = args[0] + '.' + args[1]
            # check if key exists in storage
            if key in storage.all():
                del storage.all()[key]
                # save changes to json file
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances based on the class name"""
        args = arg.split()
        # check if class name exists
        if not arg:
            # print all instances
            for key, obj in storage.all().items():
                print(obj)
            # check if class name exists
        elif args[0] not in storage.classes():
            # print error message
            print("** class doesn't exist **")
            # print all instances of class name
        else:
            print([str(obj) for obj in storage.all_classes()[args[0]].all()])

    def do_update(self, arg):
        """Updates an instance based on the class name and ID by adding or updating an attribute"""
        args = arg.split()
        # check if class name exists
        if not arg:
            print("** class name missing **")
        # check if class name exists 
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
        # check if id is empty   
            print("** instance id missing **")
        elif len(args) == 2:
        # check if attribute name is empty
            print("** attribute name missing **")
        elif len(args) == 3:
        # check if value is empty
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
