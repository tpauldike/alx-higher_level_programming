# JavaScript - Warm up
A project that had to do with the fundamentals of **JavaScript**

While doing this project, I learned:
- How to run a **JavaScript** script
- How to create variables and constants
- The differences between `var`, `const` and `let`
- The data types avaible in **JavaScript**
- How to use `if`, `if...else` statements
- How to use comments
- How to affect values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- Functions in **JavaScript**
- Scope of variables
- Arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

I did this project with the text editor `emacs` as none other (except `vi` and `vim`) were allowed. It was done in **Ubuntu 20.04 LTS** using `node` (version 14.21.1) and all the code were made `semistandard` compliant (version 16.0.1)

## Mandatory Tasks

### [0. First constant, first print](./0-javascript_is_amazing.js)
Write a script that prints “JavaScript is amazing”

### [1. 3 languages](./1-multi_languages.js)
Write a script that prints 3 lines

### [2. Arguments](./2-arguments.js)
Write a script that prints a message depending of the number of arguments passed

### [3. Value of my argument](./3-value_argument.js)
Write a script that prints the first argument passed to it

### [4. Create a sentence](./4-concat.js)
Write a script that prints two arguments passed to it, in the following format: “ is ”

### [5. An Integer](./5-to_integer.js)
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer

### [6. Loop to languages](./6-multi_languages_loop.js)
Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

### [7. I love C](./7-multi_c.js)
Write a script that prints x times “C is fun”

### [8. Square](./8-square.js)
Write a script that prints a square

### [9. Add](./9-add.js)
Write a script that prints the addition of 2 integers

### [10. Factorial](./10-factorial.js)
Write a script that computes and prints a factorial

### [11. Second biggest!](./11-second_biggest.js)
Write a script that searches the second biggest integer in the list of arguments

### [12. Object](./12-object.js)
Update this script to replace the value `12` with `89`
- You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$
```

### [13. Add file](./13-add.js)
Write a function that returns the addition of 2 integers
- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

**Tip**
```
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$
```

## Advanced Tasks

### [14. Const or not const](./100-let_me_const.js)
Write a file that modifies the value of `myVar` to `333`

### [15. Call me Moby](./101-call_me_moby.js)
Write a function that executes `x` times a function.

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$
```

### [16. Add me maybe](./102-add_me_maybe.js)
Write a function that increments and calls a function.

- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$
```

### [17. Increment object](./103-object_fct.js)
Update this script by adding a new function `incr` that increments the integer `value`.
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$
```
-----
Author: **Topman Paul-Dike**
- GitHub: [tpauldike](https://github.com/tpauldike)
- Email: [topman4loveworld@gmail.com](mailto:topman4loveworld@gmail.com)
- Alternative email: [topmanrloveworld@yahoo.com](mailto:topman4loveword@yahoo.com)
