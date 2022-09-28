# 0x0B. Python - Input/Output0x0B. Python - Input/Output
This project aimed at helping me understand practically how to read and write files using python, it taught me the JSON encoder and decoder, and it got me practicing how to automate certain processes in a program. It had 13 mandatory tasks and 2 advanced tasks, as follows:

## Tasks
> 0. Read file
	Write a function that reads a text file (`UTF8`) and prints it to stdout:
		- Prototype: `def read_file(filename=""):`
		- You must use the `with` statement
		- You don't need to manage `file permission` or `file doesn't exist` exceptions.
		- You are not allowed to import any module
>> guillaume@ubuntu:~/0x0B$ cat 0-main.py
>> #!/usr/bin/python3
>> read_file = __import__('0-read_file').read_file
>> 
>> read_file("my_file_0.txt")
>> . . .
	**No test cases needed**

---
	**Repo**
