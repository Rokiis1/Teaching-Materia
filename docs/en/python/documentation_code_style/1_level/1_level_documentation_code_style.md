# Documentation and Code Style Level 1

- [Variables, Literals, and Objects](#variables-literals-and-objects)
- [Built-in Functions](#built-in-functions)
- [Naming and Formatting](#naming-and-formatting)
- [Comments and Docstrings](#comments-and-docstrings)

**Documentation and Code Style Level 1** introduces the foundations needed to write small Python programs that are understandable as well as correct. We begin with variables, literal values, and the idea that variable names refer to objects. We then use several built-in functions to display and inspect those objects.

Once these foundations are in place, the focus shifts from making code run to making code readable. We explore meaningful naming, basic formatting, comments, and docstrings. The goal is not to memorize every Python style rule, but to begin writing code that communicates its purpose clearly.

## Variables, Literals, and Objects

A **literal** is a value written directly in Python code. At this level, common literals include strings, integers, floating-point numbers, Boolean values, and `None`.

```py
"Vardenis"
5
19.99
True
None
```

Strings represent text. Integers represent whole numbers, floating-point numbers represent numbers with a fractional part, and Boolean values represent the logical values `True` and `False`. The special value `None` represents the absence of a value.

A **variable** is a name that refers to a value so that the value can be used again later. The `=` operator assigns a name to a value.

```py
user_name = "Vardenis"
item_count = 5
price = 19.99
is_active = True
selected_item = None
```

Python strings can be written with either single or double quotation marks.

```py
user_name = "Vardenis"
city = 'Vilnius'
```

Triple quotes can be used to create strings that span multiple lines.

```py
description = """Line one
Line two
Line three"""
```

This is a string value, not a comment. Triple-quoted strings also have a special documentation use when they appear in certain positions in Python code. We will return to that idea in the **Comments and Docstrings** section.

A variable can later be assigned another value.

```py
item_count = 5
item_count = 10
```

Python also allows a name to be reassigned to an object of a different type.

```py
user_name = "Vardenis"
user_name = 100
```

This is valid Python. The name `user_name` first refers to a string object and later refers to an integer object.

Multiple names can be assigned in one statement.

```py
x, y, z = 1, 2, 3
```

Several names can also refer to the same value.

```py
x = y = z = 10
```

To understand assignment more precisely, it helps to think of variables as **names that refer to objects** rather than boxes that contain values.

```py
user_name = "Vardenis"
item_count = 5
is_active = True
```

The values `"Vardenis"`, `5`, and `True` are objects. The names `user_name`, `item_count`, and `is_active` refer to those objects.

This distinction becomes clearer when one name is assigned using another name.

```py
first_count = 10
second_count = first_count
```

After the second assignment, both names refer to the value `10`. The statement does not create a permanent connection between the two names. It assigns `second_count` to the object currently referenced by `first_count`.

![Variables referring to objects](./assets/images/variables_referring_to_objects.png)

In Python, the values we work with are objects. Strings, integers, floating-point numbers, Boolean values, and `None` are examples of objects. Later levels will explore objects in greater depth. For now, the important idea is that **variable names let us refer to objects and reuse them in code**.

When learning Python, errors are also a normal source of feedback. For example, using a name that has not been defined can produce a `NameError`, while invalid Python syntax can produce a `SyntaxError`. Later in the **Testing and Debugging Level 1** we explore errors and debugging in more detail.

Now that we have names and objects, we can use tools provided by Python to display and inspect them.

## Built-in Functions

A **function** is a reusable piece of code that performs a particular task. Python provides many functions that are available without importing anything first. These are called **built-in functions**.

A function is called by writing its name followed by parentheses. Values supplied inside the parentheses are called **arguments**.

```py
print("Hello, world")
```

Here, `print` is the function name and `"Hello, world"` is an argument passed to it.

The `print()` function displays a value.

```py
user_name = "Vardenis"
print(user_name)
```

The `type()` function tells us the type of an object.

```py
item_count = 5
print(type(item_count))
```

The `len()` function returns the length of an object that has a defined length. For a string, it returns the number of characters.

```py
user_name = "Vardenis"
print(len(user_name))
```

The `dir()` function returns a list of names that describe what an object can do and what information it holds. These names include **attributes** (information about the object) and **methods** (actions the object can perform).

```py
print(dir(user_name))
```

At this **Python Documentation and Code Style Level 1**, you do not need to understand every name returned by `dir()`. Its purpose here is to show that Python objects provide information and behavior that can be inspected.

The `help()` function displays documentation that is available for a Python object. It is especially useful for built-in functions and other objects that include documentation. The amount of information displayed depends on the documentation available for the object, so some objects may provide more detailed information than others.

```py
help(print)
```

Built-in functions themselves are also objects. If you enter the name of a built-in function without calling it in an interactive Python session, Python shows a representation of that function object.

```py
print
```

A typical interactive result is similar to the following.

```text
<built-in function print>
```

This reinforces an important idea. Functions are also objects in Python. At this level, however, we only need to understand what a function is, how to call built-in functions, and how to use them with the objects introduced so far.

With these basic tools in place, we can shift our attention from whether code merely works to whether it is easy to read and understand.

## Naming and Formatting

At the beginning of programming, it is natural to focus mainly on whether code executes and produces the expected result. Correct behavior is essential, but working code can still be unnecessarily difficult to read. Code is often read many times after it is written, whether by you returning to your own program later or by another developer who needs to understand and modify it.

Python places a strong emphasis on readability. **Code style** refers to conventions that help code remain clear and consistent. At this level, we focus on meaningful names, spacing, indentation, blank lines, and reasonable line length. These conventions make the program's intent easier to recognize and reduce the effort required to follow its logic.

Names communicate the purpose of values in a program. Compare these assignments.

```py
n = "Vardenis"
a = 25
```

The names are valid, but their meaning is unclear without additional context. More descriptive names make the same information easier to understand.

```py
user_name = "Vardenis"
user_age = 25
```

For variables, Python convention uses lowercase **snake_case** names.

```py
user_name = "Vardenis"
item_count = 5
total_price = 19.99
```

Uppercase names are conventionally used for values that are intended to remain constant.

```py
MAX_ATTEMPTS = 3
DEBUG = True
```

> **Note:** Uppercase naming is a convention. Python does not prevent an uppercase variable from being reassigned.

A good name should communicate purpose without becoming unnecessarily long. Short names such as `x` can be appropriate in limited contexts, but names such as `user_name`, `item_count`, and `total_price` usually communicate more useful information in ordinary application code.

Formatting provides the visual structure that makes names and expressions easier to scan. Consider the following code.

```py
price=100
tax=20
total=price+tax
print(total)
```

The code works, but the missing spacing makes its structure less clear. The same statements are easier to read with consistent spacing.

```py
price = 100
tax = 20
total = price + tax
print(total)
```

Spaces are normally placed around common operators, and commas are normally followed by a space.

```py
total_price = price + tax
x, y, z = 1, 2, 3
```

Python also uses indentation to represent the structure of code blocks. The standard convention is **four spaces for each indentation level**. You will encounter indented blocks when later material introduces statements that contain other statements. For now, you only need to recognize that indentation can affect program structure and must therefore be consistent.

Blank lines can separate distinct parts of a program and make code easier to scan.

```py
user_name = "Vardenis"
user_age = 25

print(user_name)
print(user_age)
```

Line length is another part of readable formatting. Very long lines are harder to read, especially when code is viewed beside other files or on smaller screens. **PEP 8 recommends limiting most lines to 79 characters.** At this level, treat 79 characters as a useful target and prefer clear expressions over unnecessarily wide statements.

These conventions are collected in Python's official style guide, **PEP 8**, which provides recommendations for indentation, whitespace, naming, line length, imports, and other aspects of Python code style. You do not need to memorize the entire guide at this level. The goal is to recognize the basic conventions and begin applying them intentionally. Later levels will introduce formatting and linting tools that can automate many style checks.

Good naming and formatting make code communicate more clearly on its own. Sometimes, however, additional written explanation is useful. Python provides comments and docstrings for this purpose.

## Comments and Docstrings

A **comment** is text in source code that is intended for people reading the program. Python ignores comment text when executing the program. A single-line comment begins with `#`.

```py
# Store the maximum number of attempts
MAX_ATTEMPTS = 3
```

Comments are most useful when they explain **why** something is done, clarify a non-obvious decision, or provide context that the code itself cannot communicate clearly. A comment that simply repeats what the code already expresses usually adds little useful information.

```py
retry_count = retry_count + 1  # Increase retry_count by 1
```

In this example, the comment only describes the operation that is already visible in the code. A more useful comment explains the reason behind the statement.

```py
# Prevent the retry process from continuing indefinitely
retry_count = retry_count + 1
```

Clear code usually needs fewer comments because meaningful names can often communicate information directly. For example, an unclear name may require an additional comment:

```py
# User age
a = 25
```

A descriptive name communicates the same information more clearly without requiring the comment.

```py
user_age = 25
```

Comments must also remain accurate. When code changes, related comments should be updated so that they do not describe behavior that no longer exists.

Earlier in this level, we saw that triple quotes create strings rather than comments.

```py
description = """Line one
Line two"""
```

A triple-quoted string has a special role when it appears in certain positions in Python code: it can become a **docstring**. A docstring provides structured documentation that Python can retain and documentation tools can use.

At this level, we focus on module docstrings. A **module** is a Python file containing Python code. When a triple-quoted string appears as the first statement in a Python file, it serves as that module's docstring and describes the purpose of the file.

```py
"""Demonstrate basic variables and built-in functions"""

user_name = "Vardenis"
print(user_name)
```

Unlike a `#` comment, a docstring can be accessed by Python as documentation. Python stores docstrings so they can be accessed through the special `__doc__` attribute. We can see this using the built-in `len` function introduced earlier.

```py
print(len.__doc__)
```

This displays the documentation stored for `len`. For now, you only need to recognize that docstrings are stored by Python and can be accessed as documentation. Special names and module-related details will be explored in **Modules and Imports Level 1**.

The `help()` function introduced earlier provides another way to view the documentation associated with an object.

```py
help(len)
```

Both examples access documentation associated with the same built-in function. `__doc__` gives direct access to its stored docstring, while `help()` presents the available documentation in a more readable form.

Later, after user-defined functions and classes have been introduced, we can extend docstrings to those objects and explore how they document parameters, return values, and more complex behavior.
