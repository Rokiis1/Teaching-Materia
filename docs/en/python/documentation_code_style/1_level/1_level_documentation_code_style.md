# Level 1

## Table of Contents: Documentation and Code Style

- [Comments](#comments)
- [Variables, Literals, and Objects](#variables-literals-and-objects)
- [Built-in Functions](#built-in-functions)
- [Naming and Formatting](#naming-and-formatting)

**Documentation and Code Style Level 1** introduces the foundations needed to write small Python programs that are understandable as well as correct. We begin with literals, variables, and objects, then introduce `print()` to display values. The focus then shifts to readable code through naming, basic spacing, and comments.

## Comments

A **comment** is text in source code intended for people reading the program. Python ignores comment text when executing the program, and a single-line comment begins with `#`. Comments can provide explanations, clarify decisions, and make source code easier to understand.

```py
# Display a greeting
print("Hello, world") # Hello, world
```

The first comment appears on its own line, while the second appears after a statement. In both cases, Python ignores the comment text. Comments placed after `print()` statements can also be used to show the expected output. Comments are most useful when they explain **why** something is done, clarify a non-obvious decision, or provide context that the code itself cannot communicate clearly. A comment that merely repeats the code adds little useful information. Comments should remain accurate when code changes, and meaningful names should be preferred over comments that merely explain unclear names.

!!! tip "Write comments for future readers"

    Comments are especially useful when a decision is difficult to understand from the code alone, when another developer needs important context, or when you return to your own code after some time. They can also explain the reason for a workaround or document a known limitation while a bug is being investigated. Describe the relevant context rather than merely repeating the code, and update or remove comments when the situation changes.

With comments established, we can now use them to explain Python examples as we explore literals, variables, and objects.

## Variables, Literals, and Objects

A **literal** is a value written directly in Python code. Common literals include strings for text, integers for whole numbers, floating-point numbers for numbers with a fractional part, Boolean values `True` and `False`, and `None`, which represents the absence of a value. A **variable** is a name that refers to an object so that it can be used again later. The `=` operator assigns a name to an object.

```py
user_name = "Vardenis"
item_count = 5
price = 19.99
is_active = True
selected_item = None
```

The values on the right are literals, while the names on the left allow us to refer to their objects later. Python strings can use either single or double quotation marks.

To understand assignment more precisely, it helps to think of variables as **names that refer to objects** rather than boxes that contain values. The following diagram shows how names refer to objects and how those references change when a name is reassigned.

![Variables referring to objects](./assets/images/variables_referring_to_objects.png)

The first stage shows `first_count` referring to the integer object `10`. In the second stage, `second_count = first_count` makes both names refer to the same object. In the third stage, assigning `20` to `first_count` changes only that name's reference; `second_count` continues to refer to `10`.

```py
first_count = 10
second_count = first_count
first_count = 20

print(first_count) # 20
print(second_count) # 10
```

Assignment does not create a permanent connection between names. Reassigning one name does not automatically reassign another. A name can also be reassigned to an object of a different type, and Python allows several names to be assigned in one statement or several names to receive the same value.

```py
user_name = "Vardenis"
user_name = 100

x, y, z = 1, 2, 3
x = y = z = 10
```

The first two statements demonstrate reassignment to a different type, while the last two demonstrate **multiple assignment** and **chained assignment**. In multiple assignment, the number of values must match the number of names. If a value is intentionally not needed, the conventional name `_` can be used to receive it.

```py
x, _, z = 1, 2, 3

print(x) # 1
print(z) # 3
```

Here, `_` receives `2`, but communicates that we do not intend to use it. It is a normal Python name, not an empty position. For example, `x, y, z = 1, 3` raises a `ValueError` because there are too few values, while `x, , z = 1, 2, 3` is invalid syntax. These assignment forms are useful to recognize, although separate assignments are often clearer when values have different purposes.

!!! info "Errors are useful feedback"

    Using a name that has not been defined can produce a `NameError`, invalid Python syntax can produce a `SyntaxError`, and assigning the wrong number of values to multiple names can produce a `ValueError`. These errors are normal feedback while learning. We will explore errors and debugging in more detail in **Testing and Debugging Level 1**.

These foundations allow us to use `print()` to display the values referenced by names.

## Built-in Functions

A **function** is a reusable piece of code that performs a particular task. Python provides **built-in functions** that are available without importing anything first. A function is called by writing its name followed by parentheses, and values supplied inside the parentheses are called **arguments**. The `print()` function displays values, allowing us to see the results of a program.

```py
print("Hello, world") # Hello, world

user_name = "Vardenis"
print(user_name) # Vardenis
```

Here, `print` is the function name and `"Hello, world"` is an argument. The first call displays a literal directly, while the second displays the object referenced by `user_name`. The parentheses call the function, and the argument determines what is displayed. Other built-in functions, including `type()` and `len()`, are introduced in **Data Types Level 1**, where they can be practiced with the types they help inspect.

With this basic tool in place, we can shift from whether code works to whether it is easy for people to read and understand.

## Naming and Formatting

Correct behavior is essential, but working code can still be unnecessarily difficult to read. Code is often read many times after it is written, either by the original author or by other developers who need to understand and modify it. **Code style** refers to conventions that help code remain clear and consistent. The initial focus is on meaningful names and basic spacing.

Names communicate the purpose of values in a program. Compare the following assignments.

```py
n = "Vardenis"
a = 25
```

The names are valid, but their meaning is unclear without additional context. Descriptive names make the same information easier to understand. Python convention uses lowercase **snake_case** names for variables, with words separated by underscores. Uppercase names are conventionally used for values intended to remain constant.

```py
user_name = "Vardenis"
item_count = 5
total_price = 19.99

MAX_ATTEMPTS = 3
DEBUG = True
```

!!! note "Constants are a naming convention"

    Uppercase naming communicates that a value is intended to remain constant. Python does not prevent an uppercase variable from being reassigned.

Names should communicate purpose without becoming unnecessarily long. Short names such as `x` are appropriate when their meaning is clear from context.

Formatting provides the visual structure that makes names and expressions easier to scan. The following code works, but its missing spacing makes it harder to read.

```py
price=100
tax=20
total=price+tax
print(total) # 120
```

Spaces around operators and after commas make the same statements easier to scan.

```py
price = 100
tax = 20
total = price + tax

print(total) # 120

x, y, z = 1, 2, 3
```

Good naming and basic spacing make code easier to read. Together with comments, these practices provide a foundation for more detailed documentation and code-style work.

!!! info "Documentation and Code Style Level 2"

    Level 2 develops more detailed documentation and formatting practices, including PEP 8, indentation, blank lines, line length, and formatting and linting tools. It also introduces practical use of `dir()` and `help()`, attributes and methods, and docstrings, including triple-quoted documentation strings, module documentation, `__doc__`, and documentation for functions and classes when those concepts have been introduced.
