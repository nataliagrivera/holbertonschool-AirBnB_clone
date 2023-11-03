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
        # check if arg is empty
        if not arg:
            print("** class name missing **")
        # check if class name exists
        elif arg not in globals() or not \
            issubclass(globals()[arg], BaseModel):
            print("** class doesn't exist **")
        
        else:
        # create new instance of class
            new_instance = globals()[arg]()
            # save new instance to json file
            new_instance.save()
            # print id of new instance
            print(new_instance.id)

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
        if not arg:
            # print all instances
            for key, obj in storage.all().items():
                print(obj)
        elif args[0] not in storage.classes():
            # print error message
            print("** class doesn't exist **")
        else:
            # print all instances of class name
            print([str(obj) for obj in storage.classes()[args[0]].all()])


    def do_update(self, arg):
        """Updates an instance based on the class name and ID by adding or updating an attribute"""
        args = arg.split()
        # check if class name exists
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in globals():
            print("** class doesn't exist **")
            return
        # check if id is empty
        elif len(args) == 1:
            print("** instance id missing **")
            return
        # check if attribute name exists
        elif args[2] not in globals()[args[0]].__dict__:
            print("** attribute doesn't exist **")
            return
        # check if attribute value is empty
        elif args[3] == "":
            print("** attribute value cannot be empty **")
            return
        else:
            # concatenate class name and id
            key = args[0] + '.' + args[1]
            if key in storage.all():
                # get object from storage
                obj = storage.all()[key]
                # try to convert attribute value to int or float
                try:
                    setattr(obj, args[2], int(args[3]))
                except ValueError:
                    pass
                try:
                    setattr(obj, args[2], float(args[3]))
                except ValueError:
                    pass
                # save changes to json file
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
