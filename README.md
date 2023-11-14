# Project: AirBnB Clone (@Holberton, @ALXAFRICA)
<p align="center">
  <img src="https://github.com/OmarDouiba/AirBnB_clone/blob/main/images/1.png">
</p>

## **0x00. AirBnB clone - The console**

- This repository covers the Parte 1 of an Airbnb clone project in python
- The full-stack project is divded into 7 parts


|                                                      Parts                                                 |                    Description                    |
| :--------------------------------------------------------------------------------------------------------  | :-----------------------------------------------  |
| [1. Console](https://github.com/OmarDouiba/AirBnB_clone#project-airbnb-clone-holberton-alxafrica)                                               |   Data model management via command interpreter   |


### Expected web static for the final product:

<p align="center">
  <img src="https://github.com/OmarDouiba/AirBnB_clone/blob/main/images/2.png">
  <img src="https://github.com/OmarDouiba/AirBnB_clone/blob/main/images/3.png">
</p>

### Web Stack for building the product:

<p align="center">
  <img src="https://github.com/OmarDouiba/AirBnB_clone/blob/main/images/4.png">
</p>

### Schemas:

<p align="center">
  <img src="https://github.com/OmarDouiba/AirBnB_clone/blob/main/images/5.jpg">
</p>

---

## Part 1: 0x00. AirBnB clone - The console

Part 1 of AirBnB Clone project @Holberton: The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp (dare we say mastery?) of both front & backend development.

The overall Project scope is:

- Build a command line interpreter to manipulate data without a visual interface.
- A front-end (user interface) and a back-end for the web app: static and dynamic
- Data storage via a database or a file storage
- An API that bridges the front-end and the data (retrieve, create, delete, update)

### Objectives For The BaseModel Class: A Class that defines all common attributes/methods for other classes:

#### Public instance attributes:

- **id:** string - assign with an uuid when an instance is created

- **created_at:** The current datetime when an instance is created

- **updated_at:** The current datetime when an instance is created, updated every time you change your object

- **__str__:** should print: [<class name>] (<self.id>) <self.__dict__>

#### Public instance methods:
- **save(self)**: updates the public instance with the current datetime
- **to_dict(self)**: returns a dictionary containing all keys/values of __dict__ of the instance. This method will be the first piece of the serialization/deserialization process to JSON format.

### Objectives For The Command Line Interpreter:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Operating In Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Operating In Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
**Example Usage:**
```

```
### Directory Tree Structure For Phase #1 of HBnB Clone:
```
.
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-310.pyc
│   │   ├── base_model.cpython-310.pyc
│   │   ├── city.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── place.cpython-310.pyc
│   │   ├── review.cpython-310.pyc
│   │   ├── state.cpython-310.pyc
│   │   └── user.cpython-310.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests

```
---
## Files

File Name | Description
--- | ---
`README.md` | A description of the Holberton AirBnB Project
`AUTHORS` | A listing of the project contributors
`console.py` | The program to launch the HBNB console
`basemodel.py` | Defines the BaseModel Class
`file_storage.py` | Defines the FileStorage Class & handles the database
`user.py` | Defines the User Class, a subclass of BaseModel
`city.py` | Defines the City Class, a subclass of BaseModel
`state.py` | Defines the User Class, a subclass of BaseModel
`amenity.py` | Defines the Amenity Class, a subclass of BaseModel
`review.py` | Defines the Review Class, a subclass of BaseModel
`place.py` | Defines the Place Class, a subclass of BaseModel
`tests/` | The test directory containing the unittest files for each Class
---

## Authors

* **DOUIBA OMAR** - [GitHub - DOUIBA OMAR](https://github.com/OmarDouiba) | [LinkedIn](https://www.linkedin.com/in/omar-douiba/) at [Holberton
School & AlxAfrica](http://holbertonschool.com & https://www.alxafrica.com/).