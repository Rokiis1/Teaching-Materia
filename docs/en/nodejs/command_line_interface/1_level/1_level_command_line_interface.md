# Level 1

## Table of Contents: Command Line

- [Understanding the Node.js Command Line](#understanding-the-nodejs-command-line)
- [Running a Node.js Script](#running-a-nodejs-script)
- [Quick Commands](#quick-commands)
- [Checking Node.js Version and Help](#checking-nodejs-version-and-help)

**Command Line Level 1** introduces the basic ways to start Node.js and run JavaScript code from a terminal or Command Prompt. You will learn how to start the Node.js runtime, run a JavaScript script, execute a short piece of code directly, check the installed Node.js version, and display command line help.

## Understanding the Node.js Command Line

The Node.js command line begins with a command that starts the **Node.js runtime**. On all systems, this command is `node`.

```bash
node
```

A Node.js command can contain several parts, represented by the general form `node [options] [file] [arguments]`. You do not need to memorize this syntax. It shows that Node.js can be started with an option, given a short command to execute, given a JavaScript file to run, or provided with arguments for a program.

When `node` is entered without a file or another execution option, it starts an **interactive session** where JavaScript code can be entered and executed directly. The command line can also tell Node.js what code or file to execute. One of the most common uses of the Node.js command line is running a JavaScript script.

## Running a Node.js Script

A **Node.js script** is a file containing JavaScript code, and JavaScript files normally use the `.js` filename extension. Suppose a file named `hello.js` contains the following code.

```js
console.log("Hello, world");
```

You can run the file by giving its name to Node.js. If the file is in another directory, you can provide a path to it instead.

```bash
node hello.js
node examples/hello.js
```

The runtime starts, executes the statements in the specified file, and exits when the program finishes.

Throughout this material, `node` is used as the command because it clearly represents invoking the Node.js runtime. Running a script is useful when JavaScript code is stored in a file. For small tasks, however, Node.js can also execute code directly from the command line without creating a separate file.

## Quick Commands

Node.js can execute a short piece of code directly from the command line with the `-e` option.

```bash
node -e "console.log(2 + 2)"
node -e "console.log('Hello from Node.js')"
```

The code inside the quotation marks is executed as JavaScript code. The first command displays `4`, while the second displays `Hello from Node.js`. Node.js then exits after each command finishes.

Node.js also provides the `-p` option, which evaluates a piece of code and displays the result of the final expression.

```bash
node -p "2 + 2"
```

This command displays `4`. The `-p` option is useful for quickly checking the value of an expression without writing `console.log`.

!!! tip "When to use a script"

    For larger programs, using a JavaScript file is usually easier to read, edit, and reuse.

In addition to executing JavaScript code, the command line provides options for getting information about the runtime itself. Two useful examples let you check the Node.js version and display built in help.

## Checking Node.js Version and Help

Node.js provides command line options for checking the runtime version and displaying built in help. Command line options often have a **long form**, which begins with two hyphens, and a **short form**, which begins with one hyphen. In the following commands, `--version` and `--help` are long-form options, while `-v` and `-h` are their short-form equivalents.

```bash
# Display the Node.js version
node --version
node -v

# Display command line help
node --help
node -h
```

The shorter `-v` and `-h` options perform the same basic tasks as `--version` and `--help`. These commands provide information about the Node.js runtime and exit without running a program. You do not need to understand every available option at this **Command Line Level 1**. The important idea is that command line options can control what the runtime does, and their short and long forms provide different ways to request the same behavior when both forms are available.

**Command Line Level 2** builds on these basics by examining how command line arguments can be read by a program through `process.argv`, how exit codes allow programs to communicate their result, and how module type affects how files are executed.
