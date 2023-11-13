AirBnB Clone ― The ALX-Holberton BnB
Optional Text

Description of the project
The ALX-Holberton B&B sums up the implementation of my four months of studies at the ALX-Holberton School - the fullstack software engineering program. The goal of the project is to deploy a replica of the Airbnb Website using my server. The final version of this project will have:

A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
A website (front-end) with static and dynamic functionalities
A comprehensive database to manage the backend functionalities
An API that provides a communication interface between the front and backend of the system.
General concepts in review
As you navigate this code base, it is great to note the following concepts, while completing this project.

How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
Files and Directories
models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py.
