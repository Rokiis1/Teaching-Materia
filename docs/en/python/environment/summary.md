# Summary

This summary brings together the most important concepts from the **Python Environment** module. It provides a quick reference for reviewing the main components, relationships, and differences involved in creating and running Python programs.

## Table of Contents: Environment

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Python development environments, development tools, interactive and script workflows, project organization, and source files**. The main goal is to understand the responsibilities of these components and how they work together.

The **Python interpreter** is the program responsible for executing Python code. A **Python development environment** brings the interpreter together with the development tools, project folders, and source files used to create and run Python programs. The interpreter can receive code directly or from a saved source file.

The **PATH** is an operating system setting containing directories in which the system searches for executable programs. When Python is available through `PATH`, it can be started without specifying its complete file path. Common commands include `python`, `python3`, and `py`, depending on the system and installation.

!!! warning "Command Availability"

    A failed command may indicate that Python is not available through that command or the current `PATH`. It does not, by itself, establish that Python is not installed.

A **text editor** provides basic tools for editing plain text files, while a **code editor** adds features designed for source code. An **integrated development environment**, or **IDE**, combines a source code editor with additional development tools. Visual Studio Code and Neovim are examples of code editors, PyCharm is an IDE, and IDLE provides a source code editor together with an interactive Python shell. Visual Studio Code requires Python extension support for its Python development features, while the Python interpreter is installed separately.

Python supports **interactive and script workflows**. An interactive session accepts code directly at the `>>>` prompt and is commonly called a **REPL**, meaning *Read, Eval, Print, Loop*. A script contains code saved in a source file so that it can be edited, preserved, and executed repeatedly. An interactive session continues until it is exited, for example with `exit()` or `quit()`.

```py
>>> print("Hello, world")
Hello, world
```

!!! abstract "Interactive and Script Execution"

    **Interactive execution receives code directly**, while **script execution receives code from a saved source file**. Both workflows use the Python interpreter.

A **project folder** is a directory that keeps the files belonging to a program together. A project can contain source files as well as **subfolders**, and a subfolder can contain additional nested subfolders. Folder names should indicate the project or contents they represent. Lowercase letters are commonly used, with underscores separating words when a folder name contains more than one word.

```text
weather_app/
├── main.py
├── weather_data/
│   ├── cities.py
│   └── archived_data/
│       └── old_cities.py
└── utility_tools/
    └── converter.py
```

Folder names that are vague, contain spaces, or use inconsistent capitalization can make project paths less clear or less convenient to work with, even when the operating system accepts them.

A **Python source file** is normally a plain text file with the `.py` extension and normally uses **UTF-8** encoding. A source filename should indicate what the file contains, while `main.py` is commonly used for an application's starting file, or entry point. Python does not give `main.py` any special meaning. Source filenames should use a single `.py` extension and avoid forms that make file paths unnecessarily difficult to work with.

```py
print("Hello, world")
print()
print("Python source files contain executable code")
```

!!! abstract "Development Environment Components"

    **The interpreter executes code, development tools provide a workspace for creating and editing it, project folders organize related files, and source files preserve Python code.** These distinct responsibilities form the basic Python development environment.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python development environment are**, describe the purpose of **PATH**, distinguish **text editors, code editors, and IDEs**, explain **interactive and script workflows** and the role of the **REPL**, describe how **project folders, subfolders, and nested subfolders** organize a program, and identify **Python source files, UTF-8 encoding, source filename considerations, and the purpose of `main.py`**.
