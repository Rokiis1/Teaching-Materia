# Summary

This summary brings together the most important concepts from the **Python Environment** module. It provides a quick reference for reviewing the main components, relationships, and differences involved in creating and running Python programs.

## Table of Contents: Environment

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Python development environments, development tools, interactive and script workflows, source files, and basic project organization**. The main goal is to understand the responsibilities of these components and how they work together.

The **Python interpreter** is the program responsible for executing Python code. A **Python development environment** brings the interpreter together with the development tools, source files, and project folders used to create and run Python programs. The interpreter can receive code directly or from a saved source file.

The **PATH** is an operating system setting containing directories in which the system searches for executable programs. When Python is available through `PATH`, it can be started without specifying its complete file path. Common commands include `python`, `python3`, and `py`, depending on the system and installation.

!!! warning "Command Availability"

    A failed command may indicate that Python is not available through that command or the current `PATH`. It does not, by itself, establish that Python is not installed.

A **text editor** provides basic tools for editing plain text files, while a **code editor** adds features designed for source code. An **integrated development environment**, or **IDE**, combines a source code editor with additional development tools. Visual Studio Code and Neovim are examples of code editors, PyCharm is an IDE, and IDLE provides a source code editor together with an interactive Python shell. Visual Studio Code requires Python extension support for its Python development features, while the Python interpreter is installed separately.

Python supports **interactive and script workflows**. An interactive session accepts code directly at the `>>>` prompt and is commonly called a **REPL**, meaning *Read, Eval, Print, Loop*. A script contains code saved in a source file so that it can be edited, preserved, and executed repeatedly.

```py
>>> print("Hello, world")
Hello, world
```

!!! abstract "Interactive and Script Execution"

    **Interactive execution receives code directly**, while **script execution receives code from a saved source file**. Both workflows use the Python interpreter.

A **Python source file** is normally a plain text file with the `.py` extension and normally uses **UTF-8** encoding. Descriptive filenames can reflect a file's purpose, while `main.py` is commonly used for an application's starting file, or entry point. Python does not give `main.py` any special meaning. A program can consist of a single source file or multiple files.

```py
print("Hello, world")
print()
print("Python source files contain executable code")
```

A **project folder** is a directory that keeps the files belonging to a program together. A small project may contain only one source file, while additional source files and resources can be placed in the same folder when needed.

``` text
greeting_app/
└── main.py
```

!!! abstract "Development Environment Components"

    **The interpreter executes code, source files preserve it, development tools provide a workspace for editing it, and project folders organize related files.** These distinct responsibilities form the basic Python development environment.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python development environment are**, describe the purpose of **PATH**, distinguish **text editors, code editors, and IDEs**, explain **interactive and script workflows** and the role of the **REPL**, identify **Python source files, UTF-8 encoding, and the purpose of `main.py`**, and describe how **project folders** organize the files belonging to a program.
