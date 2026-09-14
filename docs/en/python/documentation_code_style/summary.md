# Summary

This summary brings together the most important concepts from the **Documentation and Code Style** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships, and differences need to be explained clearly.

## Table of Contents: Documentation and Code Style

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **comments, objects, memory, literals, variables, assignment, built-in functions, naming, and basic spacing**. The main goal is to understand how Python manages objects in working memory, how variable names refer to those objects, how `print()` displays values, and how simple conventions make source code easier to read and maintain.

A **comment** is text intended for people reading source code. Python ignores comment text during execution, and a single-line comment begins with `#`. Comments can appear on their own line or after a statement, and comments after `print()` statements commonly show expected output.

```py
# Display a greeting
print("Hello, world!") # Hello, world
```

Useful comments explain **why** something is done, clarify non-obvious decisions, or provide context that the code itself cannot communicate clearly. They should remain accurate as code changes and should add useful context rather than simply repeat the code.

!!! tip "Useful comments"

    Prefer meaningful names and clear code. Add comments when they provide context that would otherwise be difficult to understand, especially the reason behind a decision.

Python programs work with **objects**, which Python manages in **random-access memory (RAM)** while a program runs. Every object has an **identity**, a **type**, and represents a specific value. A **variable** is a **name that refers to an object** rather than a box that contains a value, and the type belongs to the object rather than to the variable name.

A **literal** is a value written directly in Python source code. Common literals include strings, integers, floating-point numbers, Boolean values `True` and `False`, and `None`.

```py
"Vardenis"
5
19.99
True
None
```

The `=` operator performs **assignment** and is called the **assignment operator**. Assignment makes a name refer to an object, while **reassignment** changes what that name refers to without automatically changing other names.

```py
first_count = 10
second_count = first_count
first_count = 20

print(first_count) # 20
print(second_count) # 10
```

String literals can use single or double quotation marks, while **triple quotation marks** can create strings that span multiple lines.

```py
greeting = "Hello"
message = 'Welcome'

description = """Line one
Line two
Line three"""
```

Triple quotation marks create a multiline string, not a comment.

A name can later refer to an object of a different type because the type belongs to the object rather than to the variable name.

```py
user_name = "Vardenis"
user_name = 100
```

Python also supports **multiple assignment** and **chained assignment**.

```py
x, y, z = 1, 2, 3
x = y = z = 10
```

When a value is intentionally not needed, the conventional name `_` can receive it. It remains a normal Python name rather than an empty position.

```py
x, _, z = 1, 2, 3

print(x) # 1
print(z) # 3
```

Common assignment-related errors include `NameError` for an undefined name, `SyntaxError` for invalid Python syntax, and `ValueError` when multiple assignment receives the wrong number of values.

A **function** is a reusable piece of code that performs a particular task. Python provides **built-in functions** that can be used without importing anything first. A function call uses parentheses, values inside them are called **arguments**, and `print()` displays values.

``` py
print("Hello, world") # Hello, world

user_name = "Vardenis"
print(user_name) # Vardenis
```

Level 1 focuses on recognizing and calling built-in functions, while writing your own functions is introduced later in **Functions Level 1**.

**Code style** consists of conventions that help source code remain clear and consistent. Python convention uses lowercase **snake_case** for variable names and uppercase names for values intended to remain constant.

``` py
user_name = "Vardenis"
item_count = 5
total_price = 19.99

MAX_ATTEMPTS = 3
DEBUG = True
```

Variable names can contain letters, numbers, and underscores, but they cannot contain spaces or hyphens and cannot begin with a number.

Basic formatting includes spaces around operators and spaces after commas.

```py
price = 100
tax = 20
total = price + tax

print(total) # 120

x, y, z = 1, 2, 3
```

!!! abstract "Readable source code"

    **Objects represent values, variables refer to those objects, comments provide useful context, meaningful names communicate purpose, and consistent spacing makes code easier to read.** Together, these practices form the foundation of clear, understandable, and maintainable Python code.

After Level 1, you should be able to explain **what comments, objects, memory, literals, variables, and assignment are**, describe how variable names refer to objects in memory, distinguish **assignment from reassignment**, explain how references behave when names are reassigned, recognize **multiple and chained assignment**, use the conventional `_` name, identify common assignment-related errors, use **`print()` with literals and variables**, and explain how **meaningful names and basic spacing** improve readability.
