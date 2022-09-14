# 0x06. Python - Classes and Objects
A project designed to give me a first hand experiece of class and objects
in python programming. Made up of 0 - 6 mandatory tasks and some advanced
tasks as follows:
### 0. My first square
An empty class Suare that defines a square
### 1. Square with size
A class Square that defines a square by: (based on 0-square.py)
### 2. Size validation
A class Square that defines a square by: (based on 1-square.py)
### 3. Area of a square
A class Square that defines a square by: (based on 2-square.py)
### 4. Access and update private attribute
A class Square that defines a square by: (based on 3-square.py)
### 5. Printing a square
A class Square that defines a square by: (based on 4-square.py)
### 6. Coordinates of a square
A class Square that defines a square by: (based on 5-square.py)


## Advanced tasks
7. Singly linked list


Write a class Node that defines a node of a singly linked list by:
- Private instance attribute: data:
  - property def data(self): to retrieve it
  - property setter def data(self, value): to set it:
     - data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
-Private instance attribute: next_node:
	 - property def next_node(self): to retrieve it
	 - property setter def next_node(self, value): to set it:
	   - next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
- Instantiation with data and next_node: def __init__(self, data, next_node=None):


And a class SinglyLinkedList that defines a singly linked list by:
- Private instance attribute: head (no setter or getter)
- Simple instantiation: def __init__(self):
- Should be printable:
  - print the entire list in stdout
  - one node number by line
- Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
- You are not allowed to import any module
8. Print Square instance  
Write a class Square that defines a square by: (based on 6-square.py)
9. Compare 2 squares  
Write a class Square that defines a square by: (based on 4-square.py)
10. ByteCode -> Python #5  
Write the Python class MagicClass that does exactly the same as the following Python bytecode: