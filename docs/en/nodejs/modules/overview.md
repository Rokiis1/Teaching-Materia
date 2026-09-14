# Overview

Modules provide a way to divide a Node.js program into smaller files with focused responsibilities. Instead of keeping all code in a single file, a program can separate related functions, values, and other logic into modules that can be loaded where they are needed. Node.js also provides built-in modules for common tasks, allowing programs to use existing functionality without creating it from scratch.

A project module can make selected values available through **`module.exports`**, while another file can load those values with **`require()`**. Built-in modules are also loaded with `require()`, but they are referenced by module name rather than by a relative file path. Together, these mechanisms allow Node.js programs to organize code into focused, reusable parts.

The **Modules** module develops from the foundations of CommonJS modules to other module formats and the rules Node.js uses when locating and loading modules. Each level builds on the previous one while expanding how code can be organized and shared between files.

**Level 1** introduces the foundations of modules in Node.js. It explains what a **module** is, how to load **built-in modules** with `require()`, and how built-in module names can be written with or without the `node:` prefix. It then introduces **CommonJS project modules**, showing how values are exported through `module.exports` and loaded from another file with `require()`. It also distinguishes built-in modules, which are referenced by name, from project modules, which are referenced using relative paths.

**Level 2** builds on these CommonJS foundations by introducing the **ES module format**, including **default and named exports**, module configuration through `package.json`, and the way Node.js locates modules when they are loaded.

Together, these concepts provide a foundation for organizing Node.js programs into clear and reusable parts. They support a progression from loading built-in functionality and sharing code between project files to understanding additional module formats, configuration, and module resolution.
