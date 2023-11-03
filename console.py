import cmd
from engine.file_storage import FileStorage
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()