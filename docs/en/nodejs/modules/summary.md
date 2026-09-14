# Summary

This summary brings together the most important concepts from the **Modules** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Modules

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **modules, built-in modules, CommonJS, `require()` and `module.exports`**. The main goal is to understand how Node.js divides programs into separate files and how those files make code available to one another.

A **module** is a file containing JavaScript code that can be used by other files. Dividing a program into modules helps keep related functionality together and makes larger programs easier to organize and maintain. Code in one file is not automatically available in another file, so values that need to be shared must be explicitly exported and loaded.

Node.js provides **built-in modules** for common tasks such as working with file paths, the operating system and the file system. A built-in module can be loaded by passing its name to `require()`.

```js
const path = require("node:path");

console.log(path.sep); // Displays \ on Windows or / on macOS and Linux
```

The `node:` prefix explicitly identifies a built-in Node.js module. For most built-in modules, the prefix is optional, so `require("node:path")` and `require("path")` both load the built-in `path` module.

```js
const path = require("path");
const os = require("os");
const fs = require("fs");
```

A project can also contain its own modules. In the **CommonJS** module format, a file makes values available to other files through **`module.exports`**. Multiple values can be placed on the exported object.

```js
// math_utils.js
function add(a, b) {
    return a + b;
}

const PI = 3.14159;

module.exports = { add, PI };
```

This module exports the `add` function and the `PI` constant. Another file can load the exported object by passing the module's relative path to **`require()`**. A project module in the same directory is referenced with a path beginning with `./`.

```js
// main.js
const math = require("./math_utils.js");

console.log(math.add(2, 3)); // 5
console.log(math.PI); // 3.14159
```

Here, `require("./math_utils.js")` returns the object exported through `module.exports`. Assigning that object to `math` keeps the module name visible when accessing `math.add` and `math.PI`.

The exported object can also be **destructured** when selected values should be assigned to separate variables.

```js
// main.js
const { add, PI } = require("./math_utils.js");

console.log(add(2, 3)); // 5
console.log(PI); // 3.14159
```

Both forms load the same module. Assigning the whole exported object accesses values through the module variable, while destructuring creates separate variables for selected exports.

The important distinction is that **built-in modules are referenced by module name**, while **project modules are referenced by a relative path**. In CommonJS, **`module.exports` determines what a module makes available**, while **`require()` loads the value exported by another module**.

After reviewing Level 1, you should be able to explain **what a module is and why modules are useful**, recognize and load **built-in Node.js modules**, describe the purpose of the **`node:` prefix**, export project values with **`module.exports`**, load project modules with **`require()`**, distinguish **module names from relative module paths**, and use either the complete exported object or **destructuring** to access exported values.
