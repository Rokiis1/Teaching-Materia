# Summary

This summary brings together the most important concepts from the **Python Environment** module. It provides a quick reference for reviewing the main components, relationships, and differences involved in creating and running Python programs.

## Table of Contents: Environment

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Python development environments, development tools, interactive and script workflows, source files, and basic project organization**. The main goal is to understand the responsibilities of these components and how they work together.

A **Python development environment** is the collection of tools and files used to create and run Python programs. The **Python interpreter** executes code, development tools provide a workspace for creating and editing it, source files preserve it, and project folders keep related files together. The interpreter can receive code directly or from a saved file, while editors and IDEs provide tools for working with the code.

The **PATH** is an operating system setting containing directories in which the system searches for executable programs. When Python is available through `PATH`, it can be started without specifying its complete file path. Common commands include `python`, `python3`, and `py`, depending on the system and installation. A command that is not recognized does not necessarily mean Python is absent.

!!! warning "Command availability"

    A failed command may indicate that Python is not available through that command or the current `PATH`. It does not, by itself, establish that Python is not installed.

A **text editor** provides basic tools for editing plain text files, while a **code editor** adds features designed for source code. An **integrated development environment**, or **IDE**, combines a source code editor with additional development tools. Visual Studio Code and Neovim are examples of code editors, PyCharm is an IDE, and IDLE provides a source code editor together with an interactive Python shell. Visual Studio Code requires Python extension support for its Python development features, and the Python interpreter must be installed separately.

Python supports **interactive and script workflows**. An interactive session accepts code directly at the `>>>` prompt and is commonly called a **REPL**, meaning *Read, Eval, Print, Loop*. A script contains code saved in a source file, allowing it to be edited, preserved, and executed repeatedly.

```py
>>> print("Hello, world")
Hello, world
```

The example shows interactive input and its output. A saved script contains the Python statement without the `>>>` prompt.

!!! abstract "Interactive and script execution"

    **Interactive execution receives code directly**, while **script execution receives code from a saved source file**. Both workflows use the Python interpreter.

A **Python source file** is normally a plain text file with the `.py` extension. Source files normally use **UTF-8** encoding, which supports characters from many writing systems. Descriptive filenames can reflect a file's purpose, while `main.py` is commonly used for an application's starting file, or entry point. Python does not give `main.py` any special meaning.

``` py
print("Hello, world")
print()
print("Python source files contain executable code")
```

A source file can contain one or multiple statements. The example contains three statements that display text and a blank line. A program can consist of a single source file or multiple files.

A **project folder** is a directory that keeps the files belonging to a program together. A small project may contain only one source file, while additional source files and resources can be placed in the same folder when needed.

``` text
greeting_app/
└── main.py
```

!!! abstract "Development environment components"

    **The interpreter executes code, source files preserve it, development tools provide a workspace for editing it, and project folders organize related files.** These distinct responsibilities form the basic Python development environment.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python development environment are**, describe the purpose of **PATH**, distinguish **text editors, code editors, and IDEs**, explain **interactive and script workflows** and the role of the **REPL**, identify **Python source files, UTF-8 encoding, and the purpose of `main.py`**, and describe how **project folders** organize the files belonging to a program.
