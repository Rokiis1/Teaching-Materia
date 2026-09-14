# Summary

This summary brings together the most important concepts from the **Command Line** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships, and differences need to be explained clearly.

## Table of Contents: Command Line

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **starting the Node.js runtime, running JavaScript scripts, executing short commands, and checking runtime information**. The main goal is to understand the basic ways Node.js can be started and used from a terminal or Command Prompt.

The **Node.js runtime** executes JavaScript code outside a web browser. The `node` command starts the runtime. The general command form `node [options] [file] [arguments]` shows that Node.js can receive command line options, a JavaScript file to execute, or arguments for a program.

Entering `node` without a file or another execution option starts an **interactive session** where JavaScript code can be entered and executed directly.

A **Node.js script** is a file containing JavaScript code and normally uses the `.js` filename extension. Supplying a script filename tells Node.js to execute the statements in that file and exit when the program finishes.

```js
// hello.js
console.log("Hello, world");
```

The script can be executed by giving its filename to Node.js. A path can be supplied when the file is located in another directory.

```bash
node hello.js
node examples/hello.js
```

The **`-e` option** executes a short piece of JavaScript code directly from the command line without requiring a separate script file.

```bash
node -e "console.log(2 + 2)"
node -e "console.log('Hello from Node.js')"
```

The first command displays `4`, while the second displays `Hello from Node.js`. Node.js exits after the supplied code finishes executing.

The **`-p` option** evaluates JavaScript code and displays the result of the final expression.

```bash
node -p "2 + 2"
```

This command displays `4`. Unlike `-e`, which is commonly used to execute statements, `-p` is convenient when the result of an expression should be displayed directly.

!!! tip "Choosing an execution method"

    Use `-e` or `-p` for small, temporary tasks. A JavaScript file is usually easier to read, edit, and reuse for larger programs.

Node.js also provides options for checking the installed runtime version and displaying built in command line help. The shorter options perform the same basic tasks as their longer forms.

```bash
node --version
node -v

node --help
node -h
```

The version commands display the installed Node.js version, while the help commands display information about available command line options. These commands provide information about the runtime and exit without running a JavaScript program.

The important distinction is that **`node` by itself starts an interactive session**, **a filename tells Node.js to execute a script**, **`-e` executes supplied JavaScript code**, and **`-p` evaluates code and prints the resulting expression value**. Options such as **`--version` and `--help` inspect the runtime itself** rather than execute a program.

After reviewing Level 1, you should be able to explain **what the Node.js runtime and a Node.js script are**, distinguish **interactive execution from script execution**, run JavaScript files with `node`, use **`-e` for short commands**, use **`-p` to evaluate and display expressions**, and recognize the purpose of **`--version`, `-v`, `--help`, and `-h`**.
