# Summary

This summary brings together the most important concepts from the **Documentation and Code Style** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Documentation and Code Style

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **variables, objects, built-in functions, naming, formatting, comments and docstrings**. The main goal is to understand how Python names refer to objects, how basic functions can display and inspect them, and how consistent conventions make source code easier to read and maintain.

A **literal** is a value written directly in Python code. Common literals include strings, integers, floating-point numbers, Boolean values `True` and `False`, and `None`, which represents the absence of a value. A **variable** is a name that refers to an object, and the `=` operator assigns a name to an object. Strings, numbers, Boolean values and `None` are all objects in Python.

Python strings can use single or double quotation marks, while triple quotes can create strings that span multiple lines. A triple-quoted string is still a string, not a comment. Triple-quoted strings also have a documentation use when they appear in the appropriate position as docstrings.

Assignment creates references between names and objects rather than placing values inside variable boxes. When one name is assigned from another, both names can refer to the same object. Reassigning one name changes its reference without automatically changing the other.

```py
first_count = 10
second_count = first_count
first_count = 20

print(first_count) # 20
print(second_count) # 10
```

A name can be reassigned to an object of a different type. **Multiple assignment** assigns corresponding values to several names, while **chained assignment** assigns the same value to several names. In multiple assignment, the number of values must match the number of names. The conventional name `_` can receive a value that is intentionally not needed. It is a normal Python name, not an empty position.

```py
user_name = "Vardenis"
user_name = 100

x, y, z = 1, 2, 3
x = y = z = 10

x, _, z = 1, 2, 3
print(x) # 1
print(z) # 3
```

Using an undefined name can produce a `NameError`, invalid syntax can produce a `SyntaxError`, and assigning the wrong number of values to multiple names can produce a `ValueError`. These errors provide useful feedback, while their investigation and correction are explored in **Testing and Debugging Level 1**.

A **function** is a reusable piece of code that performs a particular task. Python's **built-in functions** are available without importing anything first. A function is called using parentheses, and values supplied inside them are called **arguments**. The `print()` function displays values, `type()` identifies an object's type, and `len()` returns the length of an object that has a defined length. For strings, `len()` returns the number of characters.

```py
user_name = "Vardenis"
item_count = 5

print(user_name) # Vardenis
print(type(item_count)) # <class 'int'>
print(len(user_name)) # 8
```

The representation `<class 'int'>` identifies Python's integer type. The word `class` is part of the type representation, while classes are explored in a later level. Further details about Python data types are explored in **Data Types Level 1**.

The `dir()` function returns names associated with an object, including **attributes** and **methods**. Attributes provide information associated with an object, while methods are functions associated with an object. The `help()` function displays available documentation. You do not need to understand every name returned by `dir()` to use these functions for basic inspection.

```py
print(dir(user_name))
help(print)
```

Built-in functions are also objects. Entering a function's name without parentheses in an interactive Python session displays its representation rather than calling it.

```py
print # <built-in function print>
```

**Code style** consists of conventions that help source code remain clear and consistent. Meaningful names communicate the purpose of values, while formatting makes statements and expressions easier to scan. Python convention uses lowercase **snake_case** for variable names and uppercase names for values intended to remain constant.

```py
user_name = "Vardenis"
item_count = 5
total_price = 19.99

MAX_ATTEMPTS = 3
DEBUG = True
```

Uppercase naming is a convention rather than a restriction enforced by Python. A good name should communicate purpose without becoming unnecessarily long, and short names can still be appropriate in limited contexts.

Formatting conventions include spaces around operators, spaces after commas, consistent indentation, deliberate blank lines and reasonable line lengths. Python uses indentation to represent code-block structure, with **four spaces per indentation level** as the standard convention. Blank lines separate related groups of statements rather than appearing between every line.

```py
price = 100
tax = 20
total = price + tax
print(total) # 120

x, y, z = 1, 2, 3
```

**PEP 8** is Python's official style guide and recommends limiting most lines to **79 characters**. It also provides conventions for whitespace, indentation, naming, imports and other aspects of code style. Formatting and linting tools that automate many style checks are introduced in **Documentation and Code Style Level 2**.

A **comment** is text intended for people reading source code. Python ignores comment text during execution, and a single-line comment begins with `#`. Useful comments explain **why** something is done, clarify a non-obvious decision or provide context that the code itself cannot communicate clearly. A comment that merely repeats an obvious operation adds little information, while a more useful comment explains the reason behind the operation.

```py
retry_count = 0

# Count attempts so the retry process can be stopped at a limit.
retry_count = retry_count + 1
```

The increment does not itself stop the retry process. The logic that checks the limit is introduced with control flow. Meaningful names can also reduce the need for explanatory comments, and comments should remain accurate when code changes.

A **docstring** is a string literal in a special position that provides structured documentation Python can retain and documentation tools can use. A **module** is a Python file containing Python code. A string literal appearing as the first statement in a module serves as its docstring and describes the purpose of the file. Triple double quotes are the recommended convention.

```py
"""Demonstrate basic variables and built-in functions."""

user_name = "Vardenis"
print(user_name) # Vardenis
```

Unlike a `#` comment, a docstring can be accessed by Python as documentation. The special `__doc__` attribute provides direct access to a stored docstring, while `help()` presents available documentation in a more readable form.

```py
print(len.__doc__)
help(len)
```

Both statements access documentation associated with the same object. Special names and module-related details are explored in **Modules and Imports Level 1**. Later levels extend docstrings to user-defined functions and classes and explain how they document parameters, return values and more complex behavior.

The important distinction is that **comments explain relevant context within source code**, while **docstrings provide structured documentation that Python can retain and documentation tools can access**.

After reviewing Level 1, you should be able to explain **what literals, variables and objects are**, describe how **assignment and reassignment** affect references, distinguish **multiple and chained assignment**, explain the conventional use of `_`, use basic **built-in functions** to display and inspect objects, recognize the purpose of **naming and formatting conventions**, explain the role of **PEP 8**, distinguish **comments from docstrings**, and describe how Python can access stored documentation.
