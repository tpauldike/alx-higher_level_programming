# 0x0B. Python - Input/Output0x0B. Python - Input/Output
This project aimed at helping me understand practically how to read and
write files using python, it taught me the JSON encoder and decoder, and it
got me practicing how to automate certain processes in a program. It had 13
mandatory tasks and 2 advanced tasks, as follows:

## Tasks
#### 0. Read file
Write a function that reads a text file (`UTF8`) and prints it to stdout:
- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don't need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

#### 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the
number of characters written:
- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

#### 2. Append to a file
Write a function that appends a string at the end of a text file (`UTF8`)
and returns the number of characters added: