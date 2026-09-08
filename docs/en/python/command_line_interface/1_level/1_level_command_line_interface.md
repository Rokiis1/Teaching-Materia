# Level 1

## Table of Contents: Command Line

- [Understanding the Python Command Line](#understanding-the-python-command-line)
- [Running a Python Script](#running-a-python-script)
- [Quick Commands](#quick-commands)
- [Checking Python Version and Help](#checking-python-version-and-help)
- [Passing Arguments to a Program](#passing-arguments-to-a-program)

**Command Line Level 1** introduces the basic ways to start Python and run Python code from a terminal or Command Prompt. You will learn how to start the Python interpreter, run a Python script, execute a short piece of code directly, check the installed Python version, display command line help, and pass simple arguments to a program.

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

The options shown above affect the Python interpreter itself. When running a script, you can also place values after the script name so that the program can receive information when it starts.

## Passing Arguments to a Program

Values written after the script name can be passed to the Python program as **command line arguments**. Python passes these arguments to the program in the order in which they were written. Consider the following command.

```bash
python script.py hello world
```

A program can access these values through `sys.argv`.

```py
import sys

# Display the command line arguments received by the program
print(sys.argv) # ['script.py', 'hello', 'world']
```

The first element identifies the script being executed, while the remaining elements contain the arguments supplied after the script name. At this level, the important idea is that **Python delivers command line arguments to the program in order**, while the program itself decides what those arguments mean and how they should be used. More detailed command line argument processing belongs in **Command Line Level 2**.
