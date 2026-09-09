# Summary

This summary brings together the most important concepts from the **Documentation and Code Style** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Documentation and Code Style

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **comments, literals, variables, objects, assignment, built-in functions, naming, and basic spacing**. The main goal is to understand how Python names refer to objects, how `print()` displays values, and how simple conventions make source code easier to read and maintain.

A **comment** is text intended for people reading source code. Python ignores comment text during execution, and a single-line comment begins with `#`. Comments can appear on their own line or after a statement. In this course, comments after `print()` statements commonly show expected output.

```py
# Display a greeting
print("Hello, world!") # Hello, world
```

Useful comments explain **why** something is done, clarify non-obvious decisions, or provide context that the code itself cannot communicate clearly. They are particularly valuable when other developers need to understand the code, when returning to it after some time, or when documenting a known limitation or bug. Comments should remain accurate as code changes and should not merely repeat obvious operations.

!!! tip "Useful comments"

    Prefer meaningful names and clear code. Add comments when they provide context that would otherwise be difficult to understand, especially the reason behind a decision or a known limitation.

A **literal** is a value written directly in Python code. Common literals include strings, integers, floating-point numbers, Boolean values `True` and `False`, and `None`, which represents the absence of a value. A **variable** is a name that refers to an object, and the `=` operator assigns a name to an object. Strings can use single or double quotation marks, and strings, numbers, Boolean values, and `None` are all objects in Python.

**Assignment establishes references between names and objects.** When one name is assigned from another, both names can refer to the same object. Reassigning one name changes its reference without automatically changing the other.

```py
first_count = 10
second_count = first_count
first_count = 20

print(first_count) # 20
print(second_count) # 10
```

A name can be reassigned to an object of a different type. **Multiple assignment** assigns corresponding values to several names, while **chained assignment** assigns the same value to several names. Multiple assignment requires the number of values to match the number of names. The conventional name `_` can receive a value that is intentionally not needed, but it remains a normal Python name rather than an empty position.

```py
user_name = "Vardenis"
user_name = 100

x, y, z = 1, 2, 3
x = y = z = 10

x, _, z = 1, 2, 3
```

Using an undefined name can produce a `NameError`, invalid syntax can produce a `SyntaxError`, and assigning the wrong number of values to multiple names can produce a `ValueError`. These errors provide useful feedback, while their investigation and correction are explored in **Testing and Debugging Level 1**.

A **function** is a reusable piece of code that performs a particular task. Python's **built-in functions** are available without importing anything first. A function call uses parentheses, and values supplied inside them are called **arguments**. The `print()` function displays values, including literals and objects referenced by names.

```py
print("Hello, world") # Hello, world

user_name = "Vardenis"
print(user_name) # Vardenis
```

The parentheses call the function, while the argument determines what is displayed. Other built-in functions, including `type()` and `len()`, are introduced in **Data Types Level 1**, where they can be practiced with the types they help inspect.

**Code style** consists of conventions that help source code remain clear and consistent. Meaningful names communicate purpose, while basic spacing makes statements and expressions easier to scan. Python convention uses lowercase **snake_case** for variable names and uppercase names for values intended to remain constant. Uppercase naming is a convention rather than a restriction enforced by Python, and short names can be appropriate when their meaning is clear from context.

```py
user_name = "Vardenis"
item_count = 5
total_price = 19.99

MAX_ATTEMPTS = 3
DEBUG = True
```

Basic formatting includes spaces around operators and spaces after commas. These conventions make the structure of an expression easier to recognize without changing its behavior.

```py
price = 100
tax = 20
total = price + tax
print(total)  # 120

x, y, z = 1, 2, 3
```

!!! abstract "Readable source code"

    **Comments provide useful context, names communicate purpose, and spacing makes expressions easier to scan.** Together, these practices help make source code understandable to its author and other developers.

After reviewing Level 1, you should be able to explain **what comments, literals, variables, and objects are**, distinguish **assignment from reassignment**, describe how references behave when names are reassigned, distinguish **multiple and chained assignment**, explain the conventional use of `_`, recognize common assignment-related errors, use **`print()` with literals and variables**, and explain how **meaningful names and basic spacing** improve readability.
