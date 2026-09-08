# Summary

This summary brings together the most important concepts from the **Python Environment** module. It provides a quick reference for reviewing the main components, relationships and differences involved in creating and running Python programs.

## Table of Contents: Environment

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Python development environments, interactive and script workflows, source files, development tools and basic project organization**. The main goal is to understand how the interpreter, source files, editors and project folders work together to support the creation and execution of Python programs.

A **Python development environment** is the collection of tools and files used to create and run Python programs. The **Python interpreter** reads and executes Python code, development tools provide a workspace for creating and editing it, source files preserve it, and project folders keep related files together. These components have different responsibilities but work together as parts of the same development environment.

The **PATH** is an operating system setting containing directories in which the system searches for executable programs. When the Python executable is available through `PATH`, it can be started without specifying its complete file path. The command used to access Python can differ between systems and installations, with `python`, `python3` and `py` being common examples. A command that is not recognized does not necessarily mean Python is absent, since it may not be available through that command or the current `PATH`.

Python code can be executed interactively or stored in a source file and executed as a **script**. An **interactive session** accepts code directly at the `>>>` prompt. The interactive process is commonly called a **REPL**, meaning *Read, Eval, Print, Loop*. Python reads the entered code, evaluates or executes it, displays a result when appropriate, and waits for more input.

``` py
>>> print("Hello, world")
Hello, world

>>> 2 + 2
4
```

Interactive execution is useful for experimenting with expressions and small pieces of code because results can be inspected immediately. A **script** contains Python code stored in a source file, allowing the code to be edited, preserved and executed repeatedly.

``` py
print("Hello, world")
```

The important distinction is that **interactive execution receives code directly as input**, while **script execution receives code from a saved source file**. Both workflows use the Python interpreter to execute Python code.

A **Python source file** is normally a plain text file with the `.py` filename extension. The extension identifies Python source code and helps development tools recognize the language. Source files can contain variable assignments, expressions, function calls and other Python statements.

``` py
user_name = "Vardenis"

print(user_name)
```

Python source files normally use **UTF-8** as their text encoding. UTF-8 defines how characters are represented when the file is stored and supports characters from many writing systems. A Python program can consist of a single source file or multiple files, and the same plain text source file can be opened with different development tools.

A **text editor** provides basic tools for creating and editing plain text files. A **code editor** is designed specifically for source code and commonly provides features such as syntax highlighting, automatic indentation, file navigation and code search. An **integrated development environment**, or **IDE**, combines a source code editor with additional development tools in one application.

Visual Studio Code and Neovim are examples of code editors, while PyCharm is an example of an IDE. **IDLE** provides a source code editor together with an interactive Python shell. These tools differ in their interfaces and features, but the choice of development tool does not define the Python program itself. Word processors such as Microsoft Word are designed for formatted documents rather than plain source code and are not appropriate for writing Python programs.

A **project folder** keeps the files belonging to a program together and provides a clear location for them on the computer. A small project may contain only one source file.

``` text
greeting_app/
└── main.py
```

The name `main.py` is commonly used for a file that acts as the starting file of an application, although Python does not require this filename. A descriptive filename can be used instead. As a program grows, additional files can be added to the same project folder.

The important relationship is that **the interpreter executes code, source files preserve it, development tools provide a workspace for editing it, and project folders organize related files**. Together, these components provide the basic structure needed to create and maintain Python programs.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python development environment are**, describe the purpose of **PATH**, distinguish **interactive execution from script execution**, explain the role of the **REPL**, identify **Python source files and UTF-8 encoding**, distinguish **text editors, code editors and IDEs**, and describe how **project folders** organize the files belonging to a program.
