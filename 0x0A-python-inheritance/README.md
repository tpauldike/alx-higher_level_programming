# 0x0A. Python - Inheritance
**Contained in this directory is the very project that had its General objectives as follows:**
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and
`super` built-in functions

The only allowed editors were `vi`, `vim`, `emacs` and all files were
intepreted in ***Ubuntu 20.04 LTS using python3 (version 3.8.5)***

## Tasks
Contained in the sub-directory [***tests***](./tests) are test cases for
[task 1](./1-my_list.py) and [task 7](./7-base_geometry.py).

There were 12 mandatory tasks and 2 advanced task as follows:

#### [0. Lookup](./0-lookup.py)
A function that returns the list of available attributes and methods of an object:

#### [1. My list](./1-my_list.py)
A class `MyList` that inherits from `list`:

#### [2. Exact same object](./2-is_same_class.py)
A function that returns `True` if the object is *exactly* an instance of the specified class ; otherwise `False`

#### [3. Same class or inherit from](./3-is_kind_of_class.py)
A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`

#### [4. Only sub class of](./4-inherits_from.py)
A function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`

#### [5. Geometry module](./5-base_geometry.py)
An empty class `BaseGeometry`

#### [6. Improve Geometry](./6-base_geometry.py)
A class `BaseGeometry` (based on `5-base_geometry.py`)

#### [7. Integer validator](./7-base_geometry.py)
class `BaseGeometry` (based on `6-base_geometry.py`)

#### [8. Rectangle](./8-rectangle.py)
A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`)

#### [9. Full rectangle](./9-rectangle.py)
A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

#### [10. Square #1](./10-square.py)
A class `Square` that inherits from `Rectangle` (`9-rectangle.py`)

## Advanced tasks
#### [11. Square #2](./11-square.py)
A class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`)

#### [12. My integer](./100-my_int.py)
A class `MyInt` that inherits from `int`

#### [13. Can I?](./101-add_attribute.py)
A function that adds a new attribute to an object if it’s possible
