# Level 1

## Table of Contents: Command Line

- [Understanding the Python Command Line](#understanding-the-python-command-line)
- [Running a Python Script](#running-a-python-script)
- [Quick Commands](#quick-commands)
- [Checking Python Version and Help](#checking-python-version-and-help)

**Command Line Level 1** introduces the basic ways to start Python and run Python code from a terminal or Command Prompt. You will learn how to start the Python interpreter, run a Python script, execute a short piece of code directly, check the installed Python version, and display command line help.

## Understanding the Python Command Line

The Python command line begins with a command that starts the **Python interpreter**. On many systems, this command is `python`, although it may instead be `python3` depending on how Python is installed. Windows also provides the `py` launcher with many Python installations.

```bash
python
```

A Python command can contain several parts, represented by the general form `python [options] [-c command | file] [arguments]`. You do not need to memorize this syntax. It shows that Python can be started with an option, given a short command to execute, given a Python file to run, or provided with arguments for a program.

When `python` is entered without a file or another execution option, it starts an **interactive session** where Python code can be entered and executed directly. The command line can also tell Python what code or file to execute. One of the most common uses of the Python command line is running a Python script.

## Running a Python Script

A **Python script** is a file containing Python code, and Python files normally use the `.py` filename extension. Suppose a file named `hello.py` contains the following code.

```py
print("Hello, world")
```

You can run the file by giving its name to Python. If the file is in another directory, you can provide a path to it instead.

```bash
python hello.py
python examples/hello.py
```

The interpreter starts, executes the statements in the specified file, and exits when the program finishes.

!!! info "Windows Python launcher"

    On Windows, the `py` launcher can also be used to run Python files.

    ```bash
    py hello.py
    ```

Throughout this material, `python` is used as the main command because it clearly represents invoking the Python interpreter. Running a script is useful when Python code is stored in a file. For small tasks, however, Python can also execute code directly from the command line without creating a separate file.

## Quick Commands

Python can execute a short piece of code directly from the command line with the `-c` option.

```bash
python -c "print(2 + 2)"
python -c "print('Hello from Python')"
```

The code inside the quotation marks is executed as Python code. The first command displays `4`, while the second displays `Hello from Python`. Python then exits after each command finishes.

!!! tip "When to use a script"

    For larger programs, using a Python file is usually easier to read, edit, and reuse.

In addition to executing Python code, the command line provides options for getting information about the interpreter itself. Two useful examples let you check the Python version and display built in help.

## Checking Python Version and Help

Python provides command line options for checking the interpreter version and displaying built in help.

```bash
# Display the Python version
python --version
python -V

# Display command line help
python --help
python -h
```

The shorter `-V` and `-h` options perform the same basic tasks as `--version` and `--help`. These commands provide information about the Python interpreter and exit without running a program. You do not need to understand every available option at this **Command Line Level 1**. The important idea is that these options let you quickly check the Python version or discover available command line options when needed.

Together, these commands provide the foundation for starting Python, executing code, and inspecting the interpreter from the command line. **Command Line Level 2** builds on these basics by examining how Python's execution context affects programs, how modules can be executed by name, and how command line arguments and exit codes allow programs to communicate with their environment.
