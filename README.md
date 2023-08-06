
# AirBnB Clone Console

Welcome to the AirBnB Clone Console! This is the first step towards building the AirBnB clone project, a full web application that mimics some functionalities of the popular accommodation rental platform, Airbnb.

## Overview

The AirBnB Clone Console is a Python-based command-line interface (CLI) that allows you to manage AirBnB objects, such as users, states, cities, places, and more. With this console, you can perform various operations on these objects, including creating, retrieving, updating, and deleting them.

## Getting Started

### Prerequisites

-   Python 3.8.5 or higher

### Installation

1.  Clone this GitHub repository to your local machine.

`git clone https://github.com/nuuxcode/AirBnB-Clone.git` 

2.  Navigate to the project directory.

`cd AirBnB-Clone` 

3.  Execute the console.

`./console.py` 

## Usage

The console provides a set of commands to interact with the AirBnB objects. Here are some of the available commands:

-   `help`: Display a list of documented commands and their descriptions.
-   `quit`: Exit the console.

Please refer to the AirBnB concept page for more details on the supported objects and their functionalities.

## Examples

### Interactive Mode

`$ ./console.py`
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb) quit
$` 

### Non-Interactive Mode

`$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)` 

## Running Tests

To ensure the proper functionality of the console, run the unit tests using the following command:

`python3 -m unittest discover tests` 

## Learning Objectives

-   Understand how to create a Python package.
-   Build a command interpreter in Python using the `cmd` module.
-   Implement Unit testing in a large project.
-   Serialize and deserialize a class.
-   Read and write JSON files.
-   Handle datetime objects.
-   Use UUIDs for unique identifiers.
-   Utilize `*args` and `**kwargs` for handling variable arguments.

## Authors

-   [Soumia Ouzat](https://github.com/SouaOui)
-   [Mounssif Bouhlaoui](https://github.com/nuuxcode)

