# Summary

This summary brings together the most important concepts from the **Command Line** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Command Line

- [Level 1](#level-1)
- [Level 2](#level-2)

## Level 1

Level 1 establishes the foundations of **starting the Python interpreter, running scripts, executing short commands, checking interpreter information and passing command line arguments**. The main goal is to understand how Python can be started from a terminal or Command Prompt and how a program receives values supplied when it starts.

The **Python interpreter** executes Python code. On many systems, the command `python` starts the interpreter, although `python3` may be used depending on the installation. Windows also provides the `py` launcher with many Python installations. The general command form is `python [options] [-c command | file] [arguments]`, which shows that Python can receive options, code to execute, a file, or arguments for a program.

Entering `python` without a file or another execution option starts an **interactive session**, where Python code can be entered and executed directly. A **Python script** is a file containing Python code and normally uses the `.py` filename extension. Supplying a script filename tells Python to execute its statements and exit when the program finishes.

```bash
python
```

```py
print("Hello, world") # Hello, world
```

```bash
python hello.py
python examples/hello.py
```

The first script command runs a file in the current directory, while the second supplies a relative path to a file in another directory. On Windows, `py hello.py` can also be used when the Python launcher is available. Throughout the module, `python` represents invoking the interpreter, while the exact command available depends on the installation.

The **`-c` option** executes a short piece of Python code directly from the command line without requiring a separate script file. Python executes the code inside the quotation marks and then exits.

```bash
python -c "print(2 + 2)" # Displays 4
python -c "print('Hello from Python')" # Displays Hello from Python
```

Short commands are useful for small tasks, while a Python file is usually easier to read, edit and reuse for larger programs. The `-c` option belongs to the interpreter command rather than to a script's own arguments.

Python also provides options for checking the interpreter version and displaying built-in command line help. The shorter options perform the same basic tasks as their longer forms.

```bash
python --version
python -V

python --help
python -h
```

The version commands display the installed Python version, while the help commands display available command line options. These commands provide information about the interpreter and exit without running a program.

**Command line arguments** are values written after the script name and passed to the program in the order supplied. Python makes them available through `sys.argv`, which is a list provided by the `sys` module. The first element identifies the script being executed, while the remaining elements contain the supplied arguments.

```bash
python script.py hello world
```

```py
import sys

print(sys.argv) # ['script.py', 'hello', 'world']
```

The important distinction is that **interpreter options control how Python starts or executes code**, while **arguments after the script name provide information for the program itself to interpret**. Level 1 introduces how those arguments are received, while more detailed validation and processing belong in Level 2.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python script are**, distinguish **interactive execution from script execution**, use **`-c`** for short commands, recognize the purpose of **`--version`, `-V`, `--help` and `-h`**, describe the role of the Windows **`py` launcher**, and explain how **`sys.argv`** receives command line arguments in order.

## Level 2

Level 2 develops a deeper understanding of **execution context, working directories, module search paths, module execution, argument validation and exit codes**. The main goal is to understand how the way Python is invoked affects program behavior and how programs can validate input and communicate their completion status.

An **execution context** is established when Python processes a command before executing user code. It includes the current working directory and the locations Python uses when searching for modules. These details become important when a program uses relative file paths, imports code from other files, or is executed as part of a package.

The **current working directory** is normally the directory from which the Python command was executed. Relative file paths used by a program are resolved from that directory rather than automatically from the directory containing the script.

```text
project/
├── scripts/
│   └── main.py
└── data/
    └── input.txt
```

```bash
cd project
python scripts/main.py
```

If `main.py` opens `data/input.txt`, the path refers to `project/data/input.txt` because the command was executed from `project`. The script's location and the working directory are separate concepts.

```py
with open("data/input.txt") as file:
    print(file.read())  # Display the file's contents
```

An **absolute path** identifies a file independently of the current working directory, but supplying an absolute path to a script does not itself change the working directory.

```bash
# macOS and Linux
python /home/user/project/scripts/main.py

# Windows
python C:\Users\User\project\scripts\main.py
```

The important distinction is that **the script path identifies which file Python executes**, while **the current working directory determines how relative file paths used by the program are resolved**.

Python uses a **module search path** to locate modules during imports. The list of search locations is available through `sys.path`.

```py
import sys

print(sys.path)  # Display the module search locations
```

When a Python file is executed directly, the directory containing that script is normally placed at the beginning of the module search path. For example, running `python scripts/main.py` normally places `scripts` first in the search path. This differs from relative file access, which uses the current working directory. A script can therefore import a module beside itself while a relative file path refers to another directory.

The **`-m` option** executes a module or package by name through Python's import system rather than identifying a script by a direct filesystem path. For a package executed this way, Python runs its `__main__.py` module.

```text
project/
└── my_package/
    ├── __init__.py
    ├── __main__.py
    └── utils.py
```

```bash
# Execute the package by name from project
python -m my_package

# Execute a file directly
python my_package/__main__.py
```

The first command locates the package through Python's import system, while the second identifies a file by its filesystem path. When `-m` is used, the current working directory is used as the initial module search location instead of the directly executed script's directory. Package execution is often preferable for package-based projects because it follows the package structure.

The `-m` option can also execute individual modules, including modules from Python's standard library.

```bash
# Start a simple HTTP server
python -m http.server

# Create a virtual environment
python -m venv .venv
```

The invocation method can also affect `sys.argv[0]`. With direct script execution, it normally represents the script path supplied for execution. With `-m`, Python locates the module first, and `sys.argv[0]` normally refers to the resulting module file rather than simply containing the module name.

Level 2 extends **command line argument processing** by accessing individual values, checking that required arguments exist, and validating them before the program continues. Arguments remain strings in `sys.argv` and are interpreted according to the program's own rules.

```bash
python main.py input.txt --verbose
```

```py
import sys

program_name = sys.argv[0]
input_file = sys.argv[1]
option = sys.argv[2]

print(program_name) # main.py
print(input_file) # input.txt
print(option) # --verbose
```

Here, `input.txt` supplies a value, while `--verbose` is a **flag** that can enable a particular behavior. The exact value of the first element can depend on how Python was started. Accessing an index that does not exist raises an `IndexError`, so required arguments should be checked before they are accessed.

The slice `sys.argv[1:]` contains all arguments after the program reference. When no additional arguments are supplied, the slice is empty and evaluates to false. This provides a simple way to check whether at least one argument exists.

```py
import sys

if not sys.argv[1:]:
    print("Provide an input file")  # Displayed when no argument is supplied
    sys.exit(1)

input_file = sys.argv[1]
print(input_file) # input.txt
```

An alternative is to handle the attempted access with `try` and `except`. Checking first is often clearer when the required number of arguments is known, while exception handling responds directly to an unsuccessful access.

```py
import sys

try:
    input_file = sys.argv[1]
except IndexError:
    print("Provide an input file") # Displayed when the argument is missing
    sys.exit(1)

print(input_file) # input.txt
```

When a program requires a specific number of arguments, `len()` can validate the size of `sys.argv`. A program requiring an input filename and an output filename expects three elements, including the program reference at index `0`.

```py
import sys

if len(sys.argv) != 3:
    print("Usage: python main.py input.txt output.txt")  # Displayed for an incorrect argument count
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

print(input_file) # input.txt
print(output_file) # output.txt
```

Arguments can also be checked for particular values or validated before the program acts on them. The following example combines a required file path, a check that the path exists, and an optional flag.

```py
import os
import sys

if not sys.argv[1:]:
    print("Provide a file path") # Displayed when no path is supplied
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print("The specified file does not exist") # Displayed when the path does not exist
    sys.exit(1)

print("File found") # Displayed when the path exists

# The flag is expected after the file path.
if "--verbose" in sys.argv[2:]:
    print("Verbose output enabled") # Displayed when --verbose is supplied
```

The first argument is reserved for the file path, so the optional flag is checked in `sys.argv[2:]`. This assumes that the file path comes first and the flag appears afterward. The existence check does not guarantee that the path refers to a readable file. These checks are basic forms of **argument validation**, while larger command line programs often use dedicated argument parsing tools.

An **exit code** communicates whether a command line program completed successfully. A status of `0` conventionally indicates success, while a nonzero status indicates unsuccessful completion. Python programs can explicitly choose a status with `sys.exit()`.

```py
import sys

if not sys.argv[1:]:
    print("Provide an input file") # Displayed when the argument is missing
    sys.exit(1) # Report unsuccessful completion

print("Argument received") # Displayed when an argument is supplied
sys.exit(0) # Report successful completion
```

Exit codes are useful when Python programs are started by other scripts, tools or automated processes because those programs can inspect the status instead of relying on printed output. A program normally exits successfully when it reaches the end without an error, so an explicit `sys.exit(0)` is not usually necessary. Explicit exit calls are most useful when a program needs to stop at a particular point or communicate a particular status.

The important distinction is that **arguments provide information to a program when it starts**, while **exit codes communicate the program's completion status back to the environment that started it**. Together with the execution context, these mechanisms explain how Python programs interact with their surrounding environment.

After reviewing Level 2, you should be able to explain **how the working directory differs from the script's location**, describe how relative and absolute paths affect file execution, explain the purpose of **`sys.path`**, distinguish **direct script execution from `python -m`**, recognize how invocation affects **`sys.argv[0]`**, validate required arguments using **slicing, exception handling and `len()`**, check simple flags and file paths, and explain how **exit codes** communicate successful or unsuccessful completion.
