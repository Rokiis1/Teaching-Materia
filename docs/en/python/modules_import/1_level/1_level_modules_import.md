# Level 1

## Table of Contents: Modules and Import

- [What is a module?](#what-is-a-module)
- [Importing and using a module](#importing-and-using-a-module)

**Python Modules and Import Level 1** introduces modules as a way to organize and reuse Python code. A module groups related functions, variables, constants, and other definitions under one name, allowing programs to use existing functionality without keeping every piece of code in one file or writing the same functionality again. In earlier material, we used built-in functions such as `print()`, `type()`, `len()`, `dir()`, and `help()`. We will now build on that knowledge by learning how modules make additional functionality available to a program.

## What is a module?

A **module** is a named collection of related Python functionality. Modules can contain functions, variables, constants, and other Python definitions. A simple way to think about modules is to compare them to cooking. When preparing a meal, you do not create every ingredient yourself. You use ingredients that are already available and bring them together when you need them. Python modules work in a similar way. Instead of writing every useful function or value yourself, you can use code that has already been organized for you.

When you create your own modules, each module is normally a separate `.py` file. For example, a small project could keep reusable calculations in `calculator.py` and use them from `main.py`.

```text
project/
├── calculator.py
└── main.py
```

In this structure, `calculator.py` is a module named `calculator`, while `main.py` is another Python file in the same project. Working with modules across multiple files, including how one file imports a module such as `calculator`, will be explained in **Python Modules and Import Level 2**. Python also provides ready-made modules through its **standard library**. These modules provide functionality for many common programming tasks and are available with a normal Python installation.

!!! info "Module files"

    A module that you create yourself is normally a `.py` file. Some standard library modules are implemented partly or entirely outside normal `.py` files. At this level, it is enough to understand a module as a named collection of related Python functionality.

Now that we know what a module represents, we can learn how to import a module, use the names it provides, and inspect unfamiliar modules when we need more information.

## Importing and using a module

Before using functionality from a module, the module usually needs to be **imported**. The `import` statement makes a module available in the current Python file. Import statements are conventionally placed near the beginning of a file so that the modules used by the program are easy to identify. Python's standard library includes a module named `math`, which provides mathematical functions and constants.

```py
import math

number = 16
result = math.sqrt(number)

print(result) # 4.0
print(math.pi) # 3.141592653589793
```

After `import math` runs, the name `math` refers to the imported module. The expression `math.sqrt(number)` uses **dot notation** to access `sqrt()` through that module. Here, `math` identifies the module and `sqrt` identifies a function provided by it. Similarly, `math.pi` accesses the constant `pi`. Keeping these names under `math` creates a **module namespace**, which groups the names belonging to the module and makes their origin clear.

Because `import math` keeps the module's names under the `math` namespace, `sqrt()` is not introduced as a separate name in the current file. It must be accessed as `math.sqrt()` with this import style.

!!! failure "Using a module name incorrectly"

    ```py
    import math

    sqrt(16) # NameError
    ```

    Python does not know a separate name called `sqrt` here. With `import math`, use `math.sqrt(16)` instead.

The module name itself must also be correct. If Python cannot find the module named in an `import` statement, it raises a `ModuleNotFoundError`.

```py
import maths # ModuleNotFoundError
```

Checking the spelling of the module name is a useful first step when this error appears. Python supports other forms of importing modules and individual names, but those forms will be introduced in a later level. For now, using `import module_name` keeps the relationship between a module and the names it provides easy to see.

The same pattern works with other standard library modules. The `random` module provides tools for working with random values, while the `datetime` module provides functionality for working with dates and times.

```py
import random
import datetime

dice_roll = random.randint(1, 6)
today = datetime.date.today()

print(dice_roll)
print(today)
```

`random.randint(1, 6)` can produce any integer from `1` through `6`, so the displayed value may differ each time the program runs. The value produced by `datetime.date.today()` depends on the current local date. Although these expressions access different kinds of functionality, they follow the same basic pattern as `math.sqrt()`. Start with the imported module name, then use dot notation to reach a name provided through it. In `datetime.date.today()`, more than one dot appears because the expression accesses functionality in several steps. At this level, it is enough to read the expression from left to right without studying the object-oriented details behind `date`.

When working with an unfamiliar module, the built-in `dir()` and `help()` functions can help you explore it. `dir()` returns a list containing many names available through an object, while `help()` displays available documentation. These functions can be used directly with an imported module or with a particular object provided by that module.

```py
import math

print(dir(math))
help(math)
help(math.sqrt)
```

The result of `dir(math)` contains many names because `math` provides a range of mathematical functionality. At this level, you can focus on recognizable public names such as `sqrt`, `pi`, `floor`, and `ceil`. Names beginning with underscores can be ignored for now because they represent special or implementation-related details that are not needed for basic module use. `help(math)` displays documentation for the module, while `help(math.sqrt)` focuses on the `sqrt()` function. Because `help()` displays documentation directly, it does not need to be wrapped in `print()`.

Together, these ideas form the main **Python Modules and Import Level 1** workflow. Import a module with `import`, access its functionality through the module name and dot notation, and use `dir()` or `help()` when you need to explore what the module provides. **Python Modules and Import Level 2** will build on this foundation by introducing additional import forms, working with modules across multiple files, and more detailed module behavior.
