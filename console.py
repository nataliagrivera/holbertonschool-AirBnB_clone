#!/usr/bin/python3
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

    # def __init__(self):what
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
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "State",
                        "City", "Amenity", "Review", "Place"]:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_instance = BaseModel()
            elif arg == "User":
                new_instance = User()
            elif arg == "State":
                new_instance = State()
            elif arg == "City":
                new_instance = City()
            elif arg == "Amenity":
                new_instance = Amenity()
            elif arg == "Review":
                new_instance = Review()
            elif arg == "Place":
                new_instance = Place()
            new_instance.save()
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
            # check if key exists in storage
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
                #save changes to JSON file
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """Prints the string representation of all instances of the specified class or all instances if no class is specified"""
        # split arg into list of arguments
        args = arg.split()
        if len(args) == 0:
            # print all instances
            for key, obj in storage.all().items():
                print(obj)
        else:
            # check if class name exists
            if args[0] not in globals() or not \
                    issubclass(globals()[args[0]], BaseModel):
                print("** class doesn't exist **")
                return
            # print all instances of the specified class
            for key, obj in storage.all().items():
                if key.split(".")[0] == args[0]:
                    print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State",
                            "City", "Amenity", "Review", "Place"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()