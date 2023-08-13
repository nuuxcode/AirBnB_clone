# 0x00. AirBnB clone - The console

## Contents:

* [1 Introduction](#1-Introduction)
* [2 Tools](#2-Tools)
* [3 Installation](#3-Installation)
* [4 Testing](#4-Testing)
* [5 Usage](#5-Usage)
* [6 Authors](#6-Authors)
* [7 License](#7-license)

# ``1-Introduction``
Team project to build a clone of [AirBnB](https://www.airbnb.com/).

## AirBnB Clone Console

Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

The console will perform the following tasks:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

## Overview

The AirBnB Clone Console is a Python-based command-line interface (CLI) that allows you to manage AirBnB objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

## ``2-Tools``
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a><!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> </a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
* Style :
    * [PEP8](https://pep8.org/)


## ``3-Installation``
1.  Clone this GitHub repository to your local machine.

`git clone https://github.com/nuuxcode/AirBnB-Clone.git`

2.  Navigate to the project directory.

`cd AirBnB-Clone` 

3.  Execute the console.

`./console.py`

### Execution 

Interactive mode

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
Non Interactive mode
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

## ``4-Usage``

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

* create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
(hbnb) create BaseModel
57262839-51d7-4a9a-93e2-35ed8e91d823
$
```

* show 

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb)
(hbhb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) all
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
(hbnb) all BaseModel
[BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)}
```
* destroy

>*Deletes an instance of a given class with a given ID.*
>*Update the file.json*

```bash
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823
(hbnb) all
[]
```

* count 

> *Prints the number of instances of a given class.*

```bash
(hbnb) create User
ce5f7ac5-4b2e-4c90-933d-6c78e69ab1c7
(hbnb) create User
dd697519-4ac9-42e0-80e2-fa7b3ac61193
(hbnb) create User
52c4036b-f018-49d0-8d93-d7a2d56bcdad
(hbnb) count User
3
```

## ``5-Testing``

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run TEST interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run TEST non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```

## ``6-Authors``

-   [Soumia Ouzat](https://github.com/SouaOui)
-   [Mounssif Bouhlaoui](https://github.com/nuuxcode)

## ``7- License``

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
