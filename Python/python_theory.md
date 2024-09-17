# Python Refresher

## Resources 
- [Harry: The Ultimate Python Handbook](https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/YouTube/The%20Ultimate%20Python%20Handbook.pdf)

## Data Types

### Mutable
- List
- Dictionary
- Set

### Immutable
- String
- Tuple

### Categories
- **Text Type:** `str`
- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `list`, `tuple`, `range`
- **Mapping Type:** `dict`
- **Set Types:** `set`, `frozenset`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`
- **None Type:** `NoneType`

## String
- All string methods return new values and do not change the original string.
- `index()` and `find()` methods:
  - `find()` returns `-1` if the substring is not found.
  - `index()` raises an error if the substring is not found.
- Strings are immutable.
- There is no `char` type in Python; it's just a `str` with a length of 1.

## Boolean
- The `bool()` function evaluates any value to `True` or `False`.
  - Example: `print(bool("Hello"))` outputs `True`.
- `True` is equivalent to `1` and `False` is equivalent to `0`.
- Any non-empty string, non-zero number, non-empty list, tuple, set, and dictionary evaluates to `True`.
- Values that evaluate to `False` include `()`, `[]`, `{}`, `""`, `0`, `None`, and `False`.

## List
- **Slicing:**
  - Syntax: `thelist[start:end:step]`
  - `start` is always included, `end` is always excluded.
- **Methods that change the list in place:**
  - `append()`
  - `extend()`
  - `insert()`
  - `remove()`
  - `pop()`
  - `reverse()`
  - `sort()`:
    - `sort(reverse=True)` for descending order.
    - `sort(key=myfunc)` to use a custom function.
    - Default sorting is case-sensitive.
- **List Comprehension:**
  - Syntax: `newlist = [expression for item in iterable if condition == True]`
  - Example: `fruits = ["apple", "banana", "cherry", "kiwi", "mango"]`
    - `newlist = [x if x != "banana" else "orange" for x in fruits]`
    - Output: `['apple', 'orange', 'cherry', 'kiwi', 'mango']`
- **Examples:**
  - `print(list({1: 'shivam', 2: 'satyam'}))` outputs `[1, 2]`
  - `print(list({1: 'shivam', 2: 'satyam'}.values()))` outputs `['shivam', 'satyam']`
  - `print(list({1: 'shivam', 2: 'satyam'}.items()))` outputs `[(1, 'shivam'), (2, 'satyam')]`
  - `thislist = ["apple", "banana", "cherry"]`
    - `thislist[1:2] = ["blackcurrant", "watermelon"]`
    - Output: `['apple', 'blackcurrant', 'watermelon', 'cherry']`
  - `thislist = ["apple", "banana", "cherry"]`
    - `thislist[1:3] = ["watermelon"]`
    - Output: `['apple', 'watermelon']`

## Tuple
- To create a single-item tuple, add a comma after the item: `d = (1,)`.
- Tuples are immutable, but you can convert them to lists, modify the lists, and convert them back to tuples.
- You can add tuples to tuples.
- **Unpacking:**
  - Example: `fruits = ("apple", "banana", "cherry")`
    - `(green, yellow, red) = fruits`
  - With `*` to collect remaining values:
    - `fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")`
      - `(green, yellow, *red) = fruits`
      - Output: `green = 'apple'`, `yellow = 'banana'`, `red = ['cherry', 'strawberry', 'raspberry']`
    - With `*` in the middle:
      - `fruits = ("apple", "mango", "papaya", "pineapple", "cherry")`
        - `(green, *tropic, red) = fruits`
        - Output: `tropic = ['mango', 'papaya', 'pineapple']`
- **Methods:** `count()`, `index()`

## Sets
- A set is unordered, unchangeable*, and does not allow duplicate values.
- Sets cannot contain lists; only immutable and hashable elements are allowed.
- Example: `print({"apple", "banana", "cherry", True, 1, 2})` outputs `{True, 2, 'banana', 'cherry', 'apple'}`.
- **Methods that change sets in place:**
  - `add()`
  - `update()`
  - `remove()`
  - `discard()`
  - `pop()`
  - `clear()`
- **Set Operations:**
  - `union()` or `|`:
    - Joins all items from both sets.
    - `union()` allows joining with all data types; `|` only works with sets.
  - `intersection()` or `&`:
    - Keeps only the duplicates.
    - `intersection_update()` modifies the original set.
  - `difference()` or `-`:
    - Keeps items in the first set that are not in the other set(s).
    - `difference_update()` modifies the original set.
  - `symmetric_difference()` or `^`:
    - Keeps all items except the duplicates.
    - `symmetric_difference_update()` modifies the original set.

## Dictionary
- Ordered and changeable. No duplicate members.
- Keys must be immutable data types (tuple, string, number), but not lists.
- **Methods:**
  - `get()` or `dict['key_name']`: Access items.
  - `keys()`: Returns a list of keys.
  - `values()`: Returns a list of values.
  - `items()`: Returns items as tuples in a list.
  - `update()`: Updates the dictionary with items from another dictionary or iterable.
  - **Remove items:**
    - `pop('key')`
    - `popitem()`: Removes the last inserted item.
    - `del('key_name')`
    - `clear()`: Empties the dictionary.
  - **Copying:**
    - `copy()` or `dict()`
  - **Fromkeys():**
    - Returns a dictionary with specified keys and value.

## Conditional Statements and Loops

### If/Else
- **Ternary Operators:**
  - `print("A") if a > b else print("B")`
  - `print("A") if a > b else print("=") if a == b else print("B")`

### Loops
- **Continue Statement:**
  - Stops the current iteration and continues with the next.
- **Break Statement:**
  - Stops the loop before it finishes all iterations.
- **While Loop with Else:**
  - Example:
    ```python
    i = 1
    while i < 6:
      print(i)
      i += 1
    else:
      print("i is no longer less than 6")
    ```
- **For Loop with Else:**
  - Note: The else block will not execute if the loop is stopped by a break statement.
  - Example:
    ```python
    for x in range(6):
      print(x)
    else:
      print("Finally finished!")
    ```

## Functions

- **Definition:** Use `def` keyword.
- **Arguments vs. Parameters:**
  - A parameter is a variable listed in the function definition.
  - An argument is the value sent to the function.
- **Arbitrary Arguments (`*args`):**
  - Use `*` before the parameter name to receive a tuple of arguments.
- **Keyword Arguments (`**kwargs`):**
  - Use `**` before the parameter name to receive a dictionary of arguments.
  - Example:
    ```python
    def my_function(**kid):
      print("His last name is " + kid["lname"])

    my_function(fname = "Tobias", lname = "Refsnes")
    ```
- **Positional-Only Arguments:**
  - Use `, /` to specify that arguments before it are positional-only.
  - Example: `def my_function(x, /)`
- **Keyword-Only Arguments:**
  - Use `*` to specify that arguments after it are keyword-only.
  - Example: `def my_function(*, x)`
- **Combine Positional-Only and Keyword-Only:**
  - Example:
    ```python
    def my_function(a, b, /, *, c, d):
      print(a + b + c + d)

    my_function(5, 6, c = 7, d = 8)
    ```

## Lambda Functions
- **Syntax:** `lambda arguments : expression`
- **Example:**
  - `x = lambda a, b : a * b`
  - `print(x(5, 6))`
- **Use Case:**
  - Use lambda functions for anonymous functions for a short period.

## Arrays
- Arrays hold more than one value at a time.
- Accessing elements and calculating length is similar to lists.
- To work with arrays in Python, you need to import a library such as NumPy.

# Python Classes and Objects

## Introduction
- Almost everything in Python is an object, with its properties and methods.
- A **Class** is like an object constructor or a "blueprint" for creating objects or an empty form.
- **Instance (objects) attributes** take preference over **Class attributes**.

- Class creation: 
      class MyClass:
          x = 5
- Object creation:
      p1 = MyClass()

- The __init__() Function: 
  - All classes have a function called __init__(), which is always executed when the class is being initiated.
  - It is called automatically every time the class is being used to create a new object.
  - This is called a dunder menthod, which is automatically called.
  - Use the __init__() function to assign values to object properties, or other operations that are necessary 
    to do when the object is being created:

    Eg:
    
          class Person:
          def __init__(self, name, age):
            self.name = name
            self.age = age
  
          p1 = Person("John", 36)
    
          print(p1.name) #John
          print(p1.age) #36

Certainly! Here's the code converted into the same Markdown format:

- The `__str__()` Function:
  - The `__str__()` function controls what should be returned when the class object is represented as a string.
  - If the `__str__()` function is not defined, the default string representation of the object is returned:
    ```
    <__main__.ClassName object at memory_address>
    ```
  - Define the `__str__()` function to provide a meaningful string representation of the object, which is helpful for debugging and logging.

  Example 1: Without `__str__()` Function

    ```python
    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

    p1 = Person("John", 36)

    print(p1)  # Output: <__main__.Person object at 0x15039e602100>
    ```

  Example 2: With `__str__()` Function

    ```python
    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def __str__(self):
        return f"{self.name}, ({self.age})"

    p1 = Person("John", 36)

    print(p1)  # Output: John, (36)
    ```
- **Object Methods:**
  - Functions inside a class that define the behavior of class instances.
  - If a method does not need to access instance-specific data, it can be defined as a static method using the `@staticmethod` decorator.

  Example:

    ```python
    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def myfunc(self):
        print("Hello my name is " + self.name)

      @staticmethod
      def greet():
        print("Good Morning")

    p1 = Person("John", 36)
    p1.myfunc()  # Output: Hello my name is John
    ```

- **Class Method:**
  - A method bound to the class and not the instance of the class.
  - Defined using the `@classmethod` decorator and takes a `cls` parameter referring to the class itself.

  Example:

    ```python
    class Employee:
      a = 1
      
      @classmethod
      def show(cls):
        print(f"The class attribute of a is {cls.a}")

    e = Employee()
    e.a = 45

    e.show()  # Output: The class attribute of a is 1
    ```

- **@property:**
  - Allows defining a method that can be accessed like an attribute.
  - Useful for adding logic when getting or setting an attribute.

  Example:

    ```python
    class Person:
      def __init__(self, name):
        self._name = name

      @property
      def name(self):
        return self._name

      @name.setter
      def name(self, value):
        if len(value) > 0:
          self._name = value
        else:
          print("Name cannot be empty")

    p = Person("John")
    print(p.name)  # Output: John
    p.name = "Jane"  # Sets name to Jane
    print(p.name)  # Output: Jane
    ```

- **The `self` Parameter:**
  - A reference to the current instance of the class used to access class variables and methods.
  - It does not have to be named `self`; it can be any name but must be the first parameter in any instance method.

  Example:

    ```python
    class Person:
      def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

      def myfunc(abc):
        print("Hello my name is " + abc.name)

    p1 = Person("John", 36)
    p1.myfunc()  # Output: Hello my name is John
    ```

- **Inheritance:**
  - Allows a class (child class) to inherit methods and properties from another class (parent class).
  - The parent class is also known as the base class, and the child class is the derived class.
  - To maintain the parent’s `__init__()` function, call it from the child class.

  Example:

    ```python
    class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

      def printname(self):
        print(self.firstname, self.lastname)

    # Creating an object of Person
    x = Person("John", "Doe")
    x.printname()  # Output: John Doe

    class Student(Person):
      pass

    # Creating an object of Student
    x = Student("Mike", "Olsen")
    x.printname()  # Output: Mike Olsen

    # Keeping the parent's __init__() function
    class Student(Person):
      def __init__(self, fname, lname):
        super().__init__(fname, lname)
    ```

- **Polymorphism:**
  - Refers to methods/functions/operators with the same name that can operate on different objects or classes.
  
  - **Function Polymorphism:** Example with `len()` function.

  - **Class Polymorphism:** Methods with the same name across different classes.

    Example:

    ```python
    class Car:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model

      def move(self):
        print("Drive!")

    class Boat:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model

      def move(self):
        print("Sail!")

    class Plane:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model

      def move(self):
        print("Fly!")

    car1 = Car("Ford", "Mustang")
    boat1 = Boat("Ibiza", "Touring 20")
    plane1 = Plane("Boeing", "747")

    for x in (car1, boat1, plane1):
      x.move()
      # Output:
      # Drive!
      # Sail!
      # Fly!
    ```

  - **Inheritance Class Polymorphism:** Overriding methods in child classes while inheriting from a parent class.

    Example:

    ```python
    class Vehicle:
      def __init__(self, brand, model):
        self.brand = brand
        self.model = model

      def move(self):
        print("Move!")

    class Car(Vehicle):
      pass

    class Boat(Vehicle):
      def move(self):
        print("Sail!")

    class Plane(Vehicle):
      def move(self):
        print("Fly!")

    car1 = Car("Ford", "Mustang")
    boat1 = Boat("Ibiza", "Touring 20")
    plane1 = Plane("Boeing", "747")

    for x in (car1, boat1, plane1):
      print(x.brand)
      print(x.model)
      x.move()
      # Output:
      # Ford
      # Mustang
      # Move!
      # Ibiza
      # Touring 20
      # Sail!
      # Boeing
      # 747
      # Fly!
    ```

## Scope:

- **Naming Variables:**
  - If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function).

- **Global Keyword:**
  - If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.

- **Nonlocal Keyword:**
  - The `nonlocal` keyword is used to work with variables inside nested functions.
  - The `nonlocal` keyword makes the variable belong to the outer function.

  Example:

    ```python
    def myfunc1():
      x = "Jane"
      def myfunc2():
        nonlocal x
        x = "hello"
      myfunc2()
      return x

    print(myfunc1())  # Output: hello
    ```

## Modules:

- A module is a file containing a set of functions you want to include in your application.
- To create a module, save the code you want in a file with the file extension `.py`: E.g., `mymodule.py`.
- To use a module: `import mymodule`.
- Note: When using a function from a module, use the syntax: `module_name.function_name`.
- **Variables:** The module can contain functions, as well as variables of all types (arrays, dictionaries, objects, etc.):

  Example:

  ```python
  # File Name: mymodule.py
  person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
  }

  import mymodule
  a = mymodule.person1["age"]
  print(a)
  ```

- **Re-naming Module:** Create an alias for `mymodule` called `mx`. (Built-in: `platform`)
- **dir() Function:**
  - The `dir()` function is a built-in function to list all the function names (or variable names) in a module.
  - The `dir()` function can be used on all modules, including the ones you create yourself.

  Example:

  ```python
  import platform

  x = dir(platform)  # List all the defined names belonging to the platform module
  print(x)
  ```

## Datetime:

- A date in Python is not a data type of its own, but we can import a module named `datetime` to work with dates as date objects.

## Math Functions:

- **Built-In:** `min`, `max`, `pow`
- Import `math`: `import math` (e.g., `math.sqrt()`, `math.ceil()`, `math.floor()`, `math.pi`)

## JSON:

- JSON is a syntax for storing and exchanging data.
- JSON is text, written with JavaScript object notation.
- Python has a built-in package called `json`, which can be used to work with JSON data. (import `json`)
- JSON is an unordered collection of key and value pairs, resembling Python's native dictionary.
  - Keys are unique Strings that cannot be null.
  - Values can be anything from a String, Boolean, Number, list, or even null.
- When we encode Python objects into JSON, we call it serialization.
- When we convert JSON encoded/formatted data into Python types, we call it JSON deserialization or parsing.

- **JSON Parsing:**
  - `json.loads()`: If you have a JSON string, you can parse it by using this method. Returns a Python dictionary.
    - Dictionary: `x = {"name": "John", "age": 30, "city": "New York"}`
    - JSON string: `x = '{ "name":"John", "age":30, "city":"New York"}'`
  - `json.dumps()`: If you have a Python object, you can convert it into a JSON string by using this method. Returns a string.

  - `json.dumps` to encode JSON Data into native Python String.
  - `json.dump` to encode and write JSON into a file.
  - How to read JSON data from a file using `json.load()` and convert it into a Python dict (to parse JSON from a file).
  - Convert JSON response or JSON string to Python dictionary using `json.loads()` (to parse JSON from String).

- When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

  | Python | JSON  |
  |--------|-------|
  | dict   | Object|
  | list   | Array |
  | tuple  | Array |
  | str    | String|
  | int    | Number|
  | float  | Number|
  | True   | true  |
  | False  | false |
  | None   | null  |

  Example:

  ```python
  import json

  x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
      {"model": "BMW 230", "mpg": 27.5},
      {"model": "Ford Edge", "mpg": 24.1}
    ]
  }

  y = json.dumps(x, indent=4, sort_keys=True)
  print(y)

  # Output:
  # {
  #     "age": 30,
  #     "cars": [
  #         {
  #             "model": "BMW 230",
  #             "mpg": 27.5
  #         },
  #         {
  #             "model": "Ford Edge",
  #             "mpg": 24.1
  #         }
  #     ],
  #     "children": [
  #         "Ann",
  #         "Billy"
  #     ],
  #     "divorced": false,
  #     "married": true,
  #     "name": "John",
  #     "pets": null
  # }
  ```

## RegEx:

- [Regular Expressions in Python](https://www.w3schools.com/python/python_regex.asp)

## Pip:

- **pip list:** Use the `list` command to list all the packages installed on your system.

## Try....Except:

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `else` block lets you execute code when there is no error.
- The `finally` block lets you execute code, regardless of the result of the `try` and `except` blocks.
- `finally` is useful inside a function. A function usually doesn't run further if the return statement has been used. But `finally` will execute in that case also. This is why `finally` is special.

  Example:

  ```python
  def main():
      try:
          a = int(input("Hey, Enter a number: "))
          print(a)
          return
      except Exception as e:
          print(e) 
          return
      finally:
          print("Hey I am inside of finally")

  main()
  ```

## Built-in Functions:

- **reversed():** The `reversed()` function returns a reversed iterator object.

## Iterators:

- An iterator is an object that contains a countable number of values.
- Technically, in Python, an iterator is an object which implements the iterator protocol, which consists of the methods `__iter__()` and `__next__()`.

- **Iterator vs Iterable:**
  - Lists, tuples, dictionaries, strings, and sets are all iterable objects.
    - They are iterable containers which you can get an iterator from.
    - All these objects have an `iter()` method which is used to get an iterator:

    Example:

    ```python
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)
    print(myit)          # <tuple_iterator object at 0x15097316b370>
    print(next(myit))   # apple
    print(next(myit))   # banana
    print(next(myit))   # cherry

    # We can also use a for loop for iterator object.
    # The for loop actually creates an iterator object and executes the `next()` method for each loop.
    ```

- **Create an Iterator:**
  - To create an object/class as an iterator, you have to implement the methods `__iter__()` and `__next__()` in your object.
  - All classes have a function called `__init__()`, which allows you to do some initializing when the object is being created.
  - The `__iter__()` method acts similarly; you can do operations (initializing, etc.), but it must always return the iterator object itself.
  - The `__next__()` method also allows you to do operations and must return the next item in the sequence.

  - **StopIteration:**
    - To prevent the iteration from going on forever, you can use the `StopIteration` statement.
    - In the `__next__()` method, you can add a terminating condition to raise an error if the iteration is done a specified number of times:

    Example:

    ```python
    class MyNumbers:
      def __iter__(self):
        self.a = 1
        return self

      def __next__(self):
        if self.a <= 20:
          x = self.a
          self.a += 1
          return x
        else:


          raise StopIteration

    myclass = MyNumbers()
    myiter = iter(myclass)

    for x in myiter:
      print(x)
    ```

## File Handling:

- The key function for working with files in Python is the `open()` function.
- The `open()` function takes two parameters: filename and mode.
- There are four different methods (modes) for opening a file:
  - `"r"` - Read - Default value. Opens a file for reading, error if the file does not exist.
  - `"a"` - Append - Opens a file for appending, creates the file if it does not exist.
  - `"w"` - Write - Opens a file for writing, creates the file if it does not exist.
  - `"x"` - Create - Creates the specified file, returns an error if the file exists.

- In addition, you can specify if the file should be handled as binary or text mode:
  - `"t"` - Text - Default value. Text mode.
  - `"b"` - Binary - Binary mode (e.g., images).

- The `with` statement in Python is used to wrap the execution of a block of code with methods defined by a context manager. When you open a file using the `with` statement, it automatically handles closing the file for you when the block of code exits, even if an exception occurs within the block.

- On the other hand, when you open a file using the traditional `open()` function without using the `with` statement, you are responsible for explicitly closing the file after you're done working with it.

- **Read:**
  - `print(f.read(5))` - Will return only 5 characters.
  - `f.readlines()` - Will return a list.
  - `print(f.readline())` - Will return a single line of str type. It will return the line until we get an empty string.

  Example:

  ```python
  # Define the number for which we want to create the multiplication table
  number = 20

  # Specify the file path where you want to write the table
  file_path = "multiplication_table_20.txt"

  # Open the file in write mode
  with open(file_path, 'w') as file:
      file.write(f"Multiplication Table of {number}\n")
      file.write("---------------------------\n")
      for i in range(1, 11):  # Multiplication table from 1 to 10
          result = number * i
          file.write(f"{number} x {i} = {result}\n")

  print(f"Multiplication table of {number} has been written to {file_path}")
  ```

## OS Module:

- **os.listdir(base_path):** List all the directories in a base path.

----

## Advanced Concepts:

1. **Walrus Operator:**

  - The walrus operator (`:=`) in Python, introduced in Python 3.8, allows you to assign values to variables as part of an expression. It's useful in situations where you want to assign a value to a variable and use that value in the same expression. Here's a simple example to illustrate its usage:

    ```python
    # Example without walrus operator
    nums = [1, 2, 3, 4, 5]
    filtered_nums = []

    for num in nums:
        if num > 2:
            filtered_nums.append(num)

    print(filtered_nums)  # Output: [3, 4, 5]

    # Example with walrus operator
    nums = [1, 2, 3, 4, 5]
    filtered_nums = [num for num in nums if (threshold := num) > 2]

    print(filtered_nums)  # Output: [3, 4, 5]
    print(threshold)      # Output: 5
    ```

2. **Type Definitions in Python:**

  - Type hints are added using the colon (`:`) syntax for variables and the `->` syntax for function return types.

    ```python
    # Variable type hint
    age: int = 25

    # Function type hints
    def greeting(name: str) -> str:
        return f"Hello, {name}!"

    # Usage
    print(greeting("Alice")) # Output: Hello, Alice!
    ```

  - **Advanced Type Hints:**

    ```python
    from typing import List, Tuple, Dict, Union

    # List of integers
    numbers: List[int] = [1, 2, 3, 4, 5]

    # Tuple of a string and an integer
    person: Tuple[str, int] = ("Alice", 30)

    # Dictionary with string keys and integer values
    scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

    # Union type for variables that can hold multiple types
    identifier: Union[int, str] = "ID123"
    identifier = 12345 # Also valid
    ```

3. **Merge and Update Operators in Dictionary:**

  - New operators `|` and `|=` allow for merging and updating dictionaries.

    ```python
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = dict1 | dict2
    print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}
    ```

4. **if __name__ == '__main__':**

  - `__name__` evaluates to the name of the module in Python from where the program is run. If the module is being run directly from the command line, `__name__` is set to the string `"__main__"`. Thus, this behavior is used to check whether the module is run directly or imported into another file.

---
## Python Collections (Arrays):

- There are four collection data types in the Python programming language:

  - **List:** A collection that is ordered and changeable. Allows duplicate members.
  - **Tuple:** A collection that is ordered and unchangeable. Allows duplicate members.
  - **Set:** A collection that is unordered, unchangeable*, and unindexed. No duplicate members.
  - **Dictionary:** A collection that is ordered** and changeable. No duplicate members.

  - *Set items are unchangeable, but you can remove and/or add items whenever you like.
  - **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    
---
## Functions: first-class objects:
[first-class objects](https://colab.research.google.com/drive/1YYJIQ3LgTLipJx9mg1nwwfLpjp7yGxhl#scrollTo=qK0IGbw5kqBF)

In Python, functions are called "first-class objects" because they possess all the properties of first-class citizens in programming languages. Specifically, this means that functions in Python:

1. **Can be Assigned to Variables**: Functions can be assigned to variables, just like any other object. For example:
   ```python
   def greet(name):
       return f"Hello, {name}!"
   
   greeting = greet  # Assigning the function to a variable
   print(greeting("Alice"))  # Output: Hello, Alice!
   ```

2. **Can Be Passed as Arguments**: Functions can be passed as arguments to other functions. This allows for higher-order functions and functional programming techniques. For example:
   ```python
   def apply_function(func, value):
       return func(value)
   
   def square(x):
       return x * x
   
   result = apply_function(square, 5)  # Passing the function `square` as an argument
   print(result)  # Output: 25
   ```

3. **Can Be Returned from Other Functions**: Functions can be created and returned from other functions. This is often used in function factories or decorators. For example:
   ```python
   def multiplier(factor):
       def multiply(x):
           return x * factor
       return multiply
   
   double = multiplier(2)  # `double` is now a function that multiplies its input by 2
   print(double(10))  # Output: 20
   ```

4. **Can Be Stored in Data Structures**: Functions can be stored in data structures like lists, tuples, or dictionaries. For example:
   ```python
   def add(x, y):
       return x + y

   def subtract(x, y):
       return x - y

   operations = [add, subtract]  # Storing functions in a list
   print(operations[0](5, 3))  # Output: 8 (calling `add` function)
   print(operations[1](5, 3))  # Output: 2 (calling `subtract` function)
   ```

5. **Can Have Attributes and Methods**: Functions can have attributes and methods just like objects. For instance, you can add attributes to functions:
   ```python
   def my_function():
       pass

   my_function.description = "This is a custom function"
   print(my_function.description)  # Output: This is a custom function
   ```

### Summary

The term "first-class object" or "first-class citizen" refers to entities in a programming language that can be manipulated in the same way as other values, such as integers or strings. In Python, because functions can be assigned to variables, passed around, returned from other functions, and stored in data structures, they exhibit the characteristics of first-class objects. This flexibility makes Python a powerful and expressive language for various programming paradigms.    
