# Level 1

## Table of Contents: Modules and Import

- [What is a module?](#what-is-a-module)
- [Importing and using a module](#importing-and-using-a-module)
- [Built-in modules](#built-in-modules)
- [Inspecting a module](#inspecting-a-module)

**Python Modules and Import Level 1** introduces modules as a way to organize and reuse Python code. A module provides a shared place for related functions, variables, constants, and other definitions, allowing programs to use existing functionality without keeping every piece of code in one file or writing the same functionality again.

In earlier material, we used built-in functions such as `print()`, `type()`, `len()`, `dir()`, and `help()`. We will now build on that knowledge by learning how Python modules make additional functionality available to a program.

## What is a module?

A **module** is a Python file or built-in collection of Python code that groups related functionality under one name. A module can contain functions, variables, constants, and other Python definitions.

A simple way to think about modules is to compare them to cooking. When preparing a meal, you do not create every ingredient yourself. You use ingredients that are already available and bring them together when you need them. Python modules work in a similar way. Instead of writing every useful function or value yourself, you can use code that has already been organized inside a module.

When you create your own modules, each module is normally a separate `.py` file. For example, a small project could keep reusable calculations in `calculator.py` and use them from `main.py`.

```text
project/
├── calculator.py
└── main.py
```

In this structure, `calculator.py` is a module named `calculator`, while `main.py` represents another Python file in the same project. Working with modules across multiple files, including how one file imports a module such as `calculator`, will be explained in **Python Modules and Import Level 2**.

Python also provides ready-made modules through its **standard library**. These modules provide functionality for common programming tasks and are available with a normal Python installation.

> **Note:** Some standard library modules are implemented partly or entirely outside normal `.py` files. At this level, it is enough to understand a module as a named collection of related Python functionality. A module that you create yourself is normally a `.py` file.

Now that we know what a module represents, we can learn how to make one available in a program with `import`.

## Importing and using a module

Before using functionality from a module, the module usually needs to be **imported**. Importing is similar to bringing an ingredient into the kitchen before using it. The `import` statement makes a module available in the current Python file.

Python includes a standard library module named `math`, which provides mathematical functions and constants.

``` py
import math
```

After this statement runs, the name `math` refers to the imported module. Import statements are conventionally placed near the beginning of a Python file so that the modules used by the program are easy to identify.

Once a module has been imported, its names can be accessed through the module name. The `math` module, for example, provides the `sqrt()` function.

``` py
import math

number = 16
result = math.sqrt(number)

print(result) # 4.0
```

The expression `math.sqrt(number)` contains two names with different roles. `math` identifies the module, while `sqrt` identifies a function provided by that module. The dot tells Python to look inside `math` for the name `sqrt`.

This organization is called a **namespace**. A module namespace keeps the names belonging to a module grouped under the module's name. This is why `sqrt()` is not available directly after only writing `import math`.

```py
import math

sqrt(16) # NameError
```

With this import style, the function must be accessed through the module namespace.

```py
import math

print(math.sqrt(16)) # 4.0
print(math.pi) # 3.141592653589793
```

Here, `sqrt` is a function and `pi` is a constant provided by the same module. Writing `math.sqrt` and `math.pi` makes their origin clear and helps prevent unrelated names from conflicting with one another.

Because the module name acts as the entry point to that namespace, spelling it correctly is essential. If Python cannot find the module named in an `import` statement, it raises a `ModuleNotFoundError`.

``` py
import maths # ModuleNotFoundError
```

If this error appears, checking the spelling of the module name is a useful first step.

> **Note:** Python supports other forms of importing modules and individual names. Those forms will be introduced later. At this level, we use `import module_name` because it clearly shows which module provides each name.

This same import and namespace pattern applies to other standard library modules, which lets us use ready-made functionality for many different tasks.

## Built-in modules

Python's standard library contains modules for many common programming tasks. You do not need to memorize these modules at this level. Different modules group functionality for different purposes, while the basic import and access pattern remains the same.

The `random` module provides tools for working with random selections and values. Its `randint()` function can produce a random integer within an inclusive range.

```py
import random

dice_roll = random.randint(1, 6)

print(dice_roll)
```

The result can be any integer from `1` through `6`, so the displayed value may be different each time the program runs.

The `datetime` module provides functionality for working with dates and times. The following example accesses `date` through the `datetime` module and then calls its `today()` method to obtain the current local date.

```py
import datetime

today = datetime.date.today()

print(today)
```

This expression contains more than one dot, but it follows the same access pattern. In `datetime.date.today()`, `datetime` identifies the module, `date` identifies a name provided by that module, and `today()` identifies functionality available from `date`. Each dot moves one level deeper into the organized names being accessed. At this **Python Modules and Import Level 1**, you only need to read the expression from left to right rather than understand the object-oriented details behind `date`.

The exact output depends on the date when the program runs. Although `random.randint()` and `datetime.date.today()` access different kinds of functionality, they follow the same basic idea introduced with `math.sqrt()`. Start with the imported module name, then use dot notation to reach the functionality you need.

As programs begin using unfamiliar modules, knowing how to import them is only part of the process. We also need a way to discover which names a module provides and read the documentation associated with them.

## Inspecting a module

The built-in `dir()` and `help()` functions introduced earlier can also be used with modules. This connects the inspection tools we already know with the module system introduced in this level.

The `dir()` function returns a list containing many of the names in an object. When the object is a module, the result includes names defined by that module.

```py
import math

print(dir(math))
```

The output contains many names because `math` provides a range of mathematical functionality. At this level, you do not need to understand every item. You can focus on recognizable public names such as `sqrt`, `pi`, `floor`, and `ceil`. Names beginning with underscores, including names surrounded by double underscores, can be ignored for now because they represent special or implementation-related details that are not needed for basic module use.

The `help()` function displays available documentation for an object. Passing the module itself displays documentation for the module.

```py
import math

help(math)
```

Because `help()` displays the documentation directly, it does not need to be wrapped in `print()`. If you only need information about one particular name, you can pass that object to `help()` instead.

```py
import math

help(math.sqrt)
```

Using `dir()` and `help()` together provides a simple beginner workflow. `dir()` can help you see which names are available, while `help()` can explain a module or a particular object in more detail.

At this **Python Modules and Import Level 1**, the main pattern is to recognize a module as an organized collection of functionality, use `import` to make it available, access its names through the module namespace, and use familiar inspection tools when you need to explore it. **Python Modules and Import Level 2** will build on this foundation by introducing additional import forms, working with modules across multiple files, and more detailed module behavior.
