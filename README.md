# Holbertonschool-AirBnB_clone

## Project Description

This project shows the initial stage of the Airbnb Clone project: The console component. Within this repository, you will find a command interpreter and a set of classes, including the BaseModel class and various classes derived from it, such as User, State, City, Place, and others. The command interpreter, much like a shell, can be activated to accept user input and execute specific operations for handling object instances.

## Requirements

### Language Used

* Python

### Libraries Used

* cmd: This is a standard library module in Python that provides a framework for building line-oriented command interpreters.
* datetime: This library is used for working with dates and times.
* uuid: This library provides functions for generating and working with universally unique identifiers (UUIDs)
* json: This library is used for working with JSON data, including encoding and decoding JSON data.
* unittest: This is the Python standard library's unit testing framework. It is used for writing and running unit tests for your code.
    
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
