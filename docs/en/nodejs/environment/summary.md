# Summary

This summary brings together the most important concepts from the **Environment** module. It provides a quick reference for reviewing the main components, relationships, and differences involved in creating and running Node.js programs.

## Table of Contents: Environment

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **Node.js development environments, development tools, interactive and script workflows, project organization, and source files**. The main goal is to understand the responsibilities of these components and how they work together.

The **Node.js runtime** is the program responsible for executing JavaScript code outside the web browser. A **Node.js development environment** brings the runtime together with the development tools, project folders, and source files used to create and run JavaScript programs. The runtime can receive code directly or from a saved source file.

The **PATH** is an operating system setting containing directories in which the system searches for executable programs. When Node.js is available through `PATH`, it can be started without specifying the complete path to its executable. The installed Node.js version can be checked with `node --version` or `node -v`.

!!! warning "Command Availability"

    If the `node` command is not recognized or cannot be found, Node.js may not be available through the current `PATH`, or it may not be installed. A failed command does not, by itself, establish which of these situations is responsible.

A **text editor** provides basic tools for editing plain text files, while a **code editor** adds features designed for source code. An **integrated development environment**, or **IDE**, combines a source code editor with additional development tools. Visual Studio Code and Neovim are examples of code editors, while WebStorm is an IDE. The Node.js runtime must be installed separately from these development tools so that JavaScript programs can be executed.

Node.js supports **interactive and script workflows**. An interactive session accepts code directly at the `>` prompt and is commonly called a **REPL**, meaning *Read, Eval, Print, Loop*. A script contains code saved in a source file so that it can be edited, preserved, and executed repeatedly. An interactive session can be exited with `.exit`, by pressing `Ctrl+C` twice, or by using the operating system's end of input keyboard shortcut.

```js
> console.log("Hello, world")
Hello, world
```

!!! abstract "Interactive and Script Execution"

    **Interactive execution receives code directly**, while **script execution receives code from a saved source file**. Both workflows use the Node.js runtime.

A **project folder** is a directory that keeps the files belonging to a program together. A project can contain source files as well as **subfolders**, and a subfolder can contain additional nested subfolders. Folder names should clearly indicate the project or contents they represent and should avoid forms that make project paths unnecessarily difficult to work with.

```text
weather_app/
├── app.js
├── weather_data/
│   ├── cities.js
│   └── archived_data/
│       └── old_cities.js
└── utility_tools/
    └── converter.js
```

Folder names that are vague, contain spaces, or use inconsistent capitalization can make project paths less clear or less convenient to work with, even when the operating system accepts them.

A **JavaScript source file** is normally a plain text file with the `.js` extension and normally uses **UTF-8** encoding. A source filename should indicate what the file contains. Filenames such as `app.js`, `index.js`, and `main.js` are commonly used for an application's starting file, or entry point, but Node.js does not give these filenames any special meaning by default. Source filenames should use a single `.js` extension and avoid forms that make file paths unnecessarily difficult to work with.

```js
console.log("Hello, world");
console.log("JavaScript source files contain executable code");
```

!!! abstract "Development Environment Components"

    **The Node.js runtime executes JavaScript code, development tools provide a workspace for creating and editing it, project folders organize related files, and source files preserve JavaScript code.** These distinct responsibilities form the basic Node.js development environment.

After reviewing Level 1, you should be able to explain **what the Node.js runtime and a Node.js development environment are**, describe the purpose of **PATH**, distinguish **text editors, code editors, and IDEs**, explain **interactive and script workflows** and the role of the **REPL**, describe how **project folders, subfolders, and nested subfolders** organize a program, and identify **JavaScript source files, UTF-8 encoding, source filename considerations, and the purpose of common entry point filenames such as `app.js`, `index.js`, and `main.js`**.
