# Summary

This summary brings together the most important concepts from the **Command Line** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Command Line

- [Level 1](#level-1)
- [Level 2](#level-2)

## Level 1

Level 1 establishes the foundations of **starting the Python interpreter, running scripts, executing short commands and checking interpreter information**. The main goal is to understand how Python can be started from a terminal or Command Prompt.

The **Python interpreter** executes Python code. On many systems, `python` starts the interpreter, although `python3` may be used depending on the installation. Windows also provides the `py` launcher with many Python installations. The general command form is `python [options] [-c command | file] [arguments]`, which shows that Python can receive options, code to execute, a file, or arguments for a program.

Entering `python` without a file or another execution option starts an **interactive session**, where Python code can be entered and executed directly. For example, entering `print("Hello, world")` displays `Hello, world`.

A **Python script** is a file containing Python code and normally uses the `.py` filename extension. Supplying a script filename tells Python to execute its statements and exit when the program finishes. For example, `python hello.py` executes a file in the current directory, while `python examples/hello.py` supplies a relative path to a file in another directory. On Windows, `py hello.py` can also be used when the Python launcher is available.

The **`-c` option** executes a short piece of Python code directly from the command line without requiring a separate script file. For example, `python -c "print(2 + 2)"` displays `4`, while `python -c "print('Hello from Python')"` displays `Hello from Python`.

!!! tip "Choosing an execution method"

    Use `-c` for small, temporary tasks. A Python file is usually easier to read, edit and reuse for larger programs.

Python also provides options for checking the interpreter version and displaying built-in command line help. The shorter options perform the same basic tasks as their longer forms.

```bash
python --version
python -V

python --help
python -h
```

The version commands display the installed Python version, while the help commands display available command line options. These commands provide information about the interpreter and exit without running a program.

After reviewing Level 1, you should be able to explain **what the Python interpreter and a Python script are**, distinguish **interactive execution from script execution**, use **`-c`** for short commands, recognize the purpose of **`--version`, `-V`, `--help` and `-h`**, and describe the role of the Windows **`py` launcher**.

## Level 2

Level 2 develops a deeper understanding of **execution context, working directories, module search paths, module execution, command line arguments, argument validation and exit codes**. The main goal is to understand how the way Python is invoked affects program behavior and how programs can validate input and communicate their completion status.

An **execution context** is established when Python processes a command before executing user code. It includes the current working directory and the locations Python uses when searching for modules. These details become important when a program uses relative file paths, imports code from other files, or is executed as part of a package.

The **current working directory** is normally the directory from which the Python command was executed. A **relative path** identifies a file in relation to the current working directory, while an **absolute path** identifies a file independently of that directory. Relative file paths are not automatically resolved from the directory containing the script. Consider the following project structure.

```text
project/
├── scripts/
│   └── main.py
└── data/
    └── input.txt
```

If the terminal is inside `project`, running `python scripts/main.py` executes the script while the working directory remains `project`. If the script opens `data/input.txt`, Python resolves that relative path to `project/data/input.txt`, not to a file inside `scripts`.

For example, `/home/user/project/scripts/main.py` identifies the script by its absolute path.

!!! warning "Script location and working directory"

    The script path identifies the file to execute, while the working directory determines how relative file paths are resolved. Supplying an absolute script path does not change the working directory.

Python uses a **module search path** to locate modules during imports. The list of search locations is available through `sys.path`, which can be displayed with `import sys` followed by `print(sys.path)`. When a Python file is executed directly, the directory containing that script is normally placed at the beginning of the module search path. A script can therefore import a module beside itself while a relative file path refers to another directory.

The **`-m` option** executes a module or package by name through Python's import system rather than identifying a script by a direct filesystem path. For a package executed this way, Python runs its `__main__.py` module. Consider a package containing `__init__.py`, `__main__.py` and `utils.py` inside `project/my_package`.

```bash
# Execute the package by name from project
python -m my_package

# Execute a file directly
python my_package/__main__.py
```

The first command locates the package through Python's import system, while the second identifies a file by its filesystem path. Direct script execution normally uses the script's directory as the initial module search location, while `-m` uses the current working directory. Package execution is often preferable for package-based projects because it follows the package structure.

The `-m` option can also execute individual modules, including standard-library modules such as `http.server` and `venv`. For example, `python -m http.server` starts a simple HTTP server, while `python -m venv .venv` creates a virtual environment.

The invocation method can also affect `sys.argv[0]`. With direct script execution, it normally represents the script path supplied for execution. With `-m`, Python locates the module first, and `sys.argv[0]` normally refers to the resulting module file rather than simply containing the module name.

Level 2 introduces **command line arguments** as values supplied after the script name. Python makes them available in order through `sys.argv`, a list provided by the `sys` module. The program interprets these strings according to its own rules and should validate required values before using them.

For example, `python main.py input.txt --verbose` supplies a filename and an optional **flag** that can enable more detailed output. The program can access these values by index, with `0` referring to the program, `1` to the input filename and `2` to the flag.

```py
import sys

program_name = sys.argv[0]
input_file = sys.argv[1]
option = sys.argv[2]

print(program_name)  # main.py
print(input_file)  # input.txt
print(option)  # --verbose
```

!!! warning "Missing arguments"

    Accessing an index that does not exist raises an `IndexError`. Required arguments should therefore be checked before they are accessed.

The main **argument validation** techniques are checking whether required values exist, handling an unsuccessful access with `try` and `except`, checking the expected argument count with `len()`, and validating particular values before using them. The following fragments summarize these distinct approaches.

```py
# Check whether at least one argument was supplied
if not sys.argv[1:]:
    sys.exit(1)

# Check the exact number of arguments
if len(sys.argv) != 3:
    sys.exit(1)
```

The slice `sys.argv[1:]` contains all arguments after the program reference. It is empty when no additional arguments are supplied. An alternative is to access `sys.argv[1]` inside a `try` block and handle `IndexError` in an `except` block. Checking first is often clearer when the required number of arguments is known, while exception handling responds directly to an unsuccessful access.

A program can also validate a file path with `os.path.exists(file_path)` and check an optional flag with `"--verbose" in sys.argv[2:]`. In this example, the file path is expected first, so the flag is checked among the remaining arguments.

!!! info "File existence and readability"

    An existence check does not guarantee that a path refers to a readable file. Larger command line programs often use dedicated argument parsing tools to handle more complex requirements.

An **exit code** communicates whether a command line program completed successfully. A status of `0` conventionally indicates success, while a nonzero status indicates unsuccessful completion. Python programs can explicitly choose a status with `sys.exit()`.

```py
import sys

if not sys.argv[1:]:
    print("Provide an input file")  # Displayed when the argument is missing
    sys.exit(1)  # Report unsuccessful completion

print("Argument received")  # Displayed when an argument is supplied
sys.exit(0)  # Report successful completion
```

Exit codes are useful when Python programs are started by other scripts, tools or automated processes because those programs can inspect the status instead of relying on printed output. A program normally exits successfully when it reaches the end without an error, so an explicit `sys.exit(0)` is not usually necessary.

!!! abstract "Arguments and exit codes"

    **Arguments provide information to a program when it starts**, while **exit codes report its completion status**. Together with the execution context, these mechanisms explain how Python programs interact with their surrounding environment.

After reviewing Level 2, you should be able to explain **how the working directory differs from the script's location**, describe how relative and absolute paths affect file execution, explain the purpose of **`sys.path`**, distinguish **direct script execution from `python -m`**, recognize how invocation affects **`sys.argv[0]`**, validate required arguments using **slicing, exception handling and `len()`**, check simple flags and file paths, and explain how **exit codes** communicate successful or unsuccessful completion.
