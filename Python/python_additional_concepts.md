


# Python Additional Concepts

- [__name__ in Python](#name-in-python)
- [Collections Module](#collections-module)
  - [defaultdict](#defaultdict)
  - [Counter](#counter)
- [Itertools Module](#itertools-module)
  - [Permutations](#permutations)
- [Set & FrozenSet](#set--frozenset)
- [Shallow Copy and Deep Copy](#shallow-copy-and-deep-copy)
- [Decorators](#decorators)

## __name__ in Python
Python built-in attribute.
- The name of the class, function, method, descriptor, or generator instance.
- [Documentation](https://docs.python.org/3/library/__main__.html)

## Collections Module
### defaultdict
- Regular dict: When using a regular dictionary, if you try to access or modify a key that doesn't exist, Python raises a KeyError.
- `defaultdict` simplifies this process by providing a default value (specified as a `default_factory`) when a key is accessed that doesn't exist.

Example:
```python
# Regular dict
fruit_count_regular = {}
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for fruit in fruits:
    if fruit in fruit_count_regular:
        fruit_count_regular[fruit] += 1
    else:
        fruit_count_regular[fruit] = 1
```

```python
# Default dict
from collections import defaultdict

fruit_count_defaultdict = defaultdict(int)  # int() gives 0 as default value
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

for fruit in fruits:
    fruit_count_defaultdict[fruit] += 1
```

### Counter
- A counter is a subclass of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element.

Example:
```python
# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# With dictionary
print(Counter({'A':3, 'B':5, 'C':2}))

# With keyword arguments
print(Counter(A=3, B=5, C=2))
```

Output:
```
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
```

## Itertools Module
### Permutations
- [Explain permutations here if needed]

## Set & FrozenSet
### Practical Differences
- **Mutability**: Sets (`set`) are mutable, while frozensets (`frozenset`) are immutable.
- **Hashability**: Frozensets can be used as dictionary keys or as elements of other sets because they are hashable, whereas mutable sets cannot.
- **Operations**: Sets support operations that modify the set (addition and removal of elements), while frozensets do not.

### When to Use Which
- Use a set when you need a collection that you will modify (add or remove elements).
- Use a frozenset when you need an immutable collection that you want to use as a dictionary key or as an element of another set.

## Shallow Copy and Deep Copy
- **Shallow Copy**: Copies the top-level structure and references of nested objects.
- **Deep Copy**: Recursively copies all nested objects, creating independent copies.

Example:
```python
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_list = original_list
deep_list = copy.deepcopy(original_list)

print(id(original_list))  # e.g., 4342131136
print(id(shallow_list))    # e.g., 4342131136
print(id(deep_list))       # e.g., 4342131264
```

## Decorators
- A decorator is a function that gives additional functionality to existing functions.
- In Python, decorators allow you to modify or extend the behavior of functions or methods without changing their actual code. They are often used for logging, access control, instrumentation, and other cross-cutting concerns.

Example:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

In this example:
- `my_decorator` is the decorator function.
- `say_hello` is the function being decorated.
- The `@my_decorator` syntax is shorthand for `say_hello = my_decorator(say_hello)`, meaning `say_hello` is replaced by the wrapper function.

### How to Write a Decorator
1. Define a function that takes a function as an argument.
2. Inside that function, define a nested function (wrapper) that will execute before and/or after the original function.
3. Return the wrapper function.

### Decorator Syntax
The `@decorator_name` syntax is syntactic sugar that simplifies the application of decorators. It's equivalent to:
```python
decorated_function = decorator_name(original_function)
```

Using decorators can make your code more readable and maintainable by separating concerns and avoiding repetition. They are a key feature of Python that leverages first-class functions and higher-order programming.

## Functions
- Functions are first-class objects and can be passed around as arguments (e.g., `int`, `string`, `float`, etc.).


