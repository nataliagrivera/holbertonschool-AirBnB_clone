# Holbertonschool-AirBnB_clone

## Project Description

This project shows the initial stage of the Airbnb Clone project: The console component. Within this repository, you will find a command interpreter and a set of classes, including the BaseModel class and various classes derived from it, such as User, State, City, Place, and others. The command interpreter, much like a shell, can be activated to accept user input and execute specific operations for handling object instances.

## Requirements of the Project

### Python Scripts

 * Allowed editors: vi, vim, emacs
 * All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
 * All your files should end with a new line
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file, at the root of the folder of the project, is mandatory
 * Your code should use the pycodestyle (version 2.7.*)
 * All your files must be executable
 * The length of your files will be tested using wc
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
 * A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
*  e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
*  e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3
* -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

 
## The Console  

The console is a command line interpreter. Through the command line interpreter allows us to perform various actions, such as:

* Creating a data model.
* Manage (create, update, destroy, etc) objects via a console / command interpreter.
* Store and retrieve objects from a file (JSON file).

## How to start the console


Clone the repository: git clone git@github.com:nataliagrivera/holbertonschool-AirBnB_clone.git   
Access the repository: cd holbertonschool-AirBnB_clone

## How to Use the Command Interpreter

| Commands |    Usage Example  |       Functionality           |    
|---|---|---|  
|  `help`    |    help    | Display help message. |  
|  `create`  | create <class>  | Create a new instance of BaseModel, save it to a JSON file, and print the ID. |  
|  `show`    | User .show('324') | Prints the string representation of an instance based on the class name and ID. |  
|  `destroy` | User .destroy('324') | Deletes an instance based on the class name and ID. |  
|  `update`  | User .update('321', {'name', : 'Bob'}) | Updates an instance based on the class name and ID by adding or updating an attribute. |   
|  `all`     | User .all() | Prints string representation of all instances based on the class name. |   
|  `quit`    | quit  | Exits the program. |  

## Usage

Interactive Mode

![Screenshot from 2023-11-01 13-55-32](https://github.com/nataliagrivera/holbertonschool-AirBnB_clone/assets/127802407/469092b6-0aea-4610-bc96-0266dc9cfed5)

Non-Interactive Mode  

![Screenshot from 2023-11-01 13-56-42](https://github.com/nataliagrivera/holbertonschool-AirBnB_clone/assets/127802407/cd7f1f03-9209-4897-a1d8-b3ef928f8f31)

## Authors
Natalia Rivera | Jose G. Nieves

## License   
Free Source Code
