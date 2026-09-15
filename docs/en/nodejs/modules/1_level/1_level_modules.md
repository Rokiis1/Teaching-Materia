# Level 1

## Table of Contents: Modules

- [Understanding Modules](#understanding-modules)
- [Importing Built-in Modules with `require()`](#importing-built-in-modules-with-require)
- [Creating Your Own Module with `module.exports`](#creating-your-own-module-with-moduleexports)
- [Importing Your Own Module with `require()`](#importing-your-own-module-with-require)

**Modules Level 1** introduces the basic ways Node.js programs are divided into modules. You will learn what a module is, how to use built-in modules provided by Node.js, how to create your own module, and how to load it into another file.

## Understanding Modules

A **module** is a file containing JavaScript code that can be used by other files. As a program grows, keeping all of its code in a single file becomes difficult to navigate and maintain. Modules address this by letting a program be divided into smaller pieces, where each file focuses on a specific part of the program.

```mermaid
flowchart LR
    MAIN["main.js"]
    MATH["mathUtils.js"]

    MAIN -->|"loads"| MATH
```

Node.js treats each file as its own module, so code in one file is not automatically visible to other files. To share code in the CommonJS module format covered in this level, one file makes values available through `module.exports` and another loads them with `require()`.

Modules can come from different sources. We will begin with modules that Node.js already provides and examine how `require()` loads them into a program.

## Importing Built-in Modules with `require()`

Node.js provides **built-in modules** for common tasks such as working with file paths, the operating system, and the file system. A built-in module is loaded by passing its name to `require()`.

```js
const path = require("node:path");

console.log(path); // Displays the module object
```

This example loads the `node:path` module. Displaying `path` can help you inspect the module's exported properties, although some values may appear as `[Function]` or `[Getter]` rather than showing their full implementation.

The `node:` prefix identifies a built-in module but is not required for most built-in modules. For example, `require("node:path")` and `require("path")` both load the built-in `path` module. The same applies to other built-in modules such as `os` and `fs`. Using `node:` makes it explicit that the module is provided by Node.js.

Built-in modules provide functionality that is already available in Node.js, but programs often need modules containing project-specific code. Before those modules can be loaded with `require()`, they first need to define which values they make available to other files through `module.exports`.

## Creating Your Own Module with `module.exports`

A file can make values available to other files through **`module.exports`**, which initially refers to an empty object in a CommonJS module.

```js
// mathUtils.js
function add(a, b) {
    return a + b;
}

const PI = 3.14159;

module.exports = { add, PI };
```

This module exports the `add` function and the `PI` constant. Assigning `module.exports = { add, PI }` replaces the initial empty export object with the new object.

!!! info "Adding Exported Properties"

    Instead of replacing the export object, properties can be added to it individually. For example, `module.exports.add = add` adds an `add` property to the existing object. This level primarily uses `module.exports = { ... }` when exporting multiple values.

Exporting values defines what the module makes available, but another file must still load that module before it can use those values. We can now connect both sides of the CommonJS pattern by importing the module with `require()`.

## Importing Your Own Module with `require()`

A project module can be loaded with `require()` by providing a **relative path**. A path beginning with `./` refers to a location relative to the current module.

```js
// main.js
const { add, PI } = require("./mathUtils.js");

console.log(add(2, 3)); // 5
console.log(PI); // 3.14159
```

This example loads `mathUtils.js` and uses destructuring to assign its `add` and `PI` exports to separate variables. The entire exported object can instead be assigned to one variable. This can make the source of a value clearer and can avoid naming conflicts when the current file already uses a name such as `add`.

```js
// main.js
const math = require("./mathUtils.js");

console.log(math.add(2, 3)); // 5
console.log(math.PI); // 3.14159
```

Here, `require("./mathUtils.js")` returns the object exported by `mathUtils.js`, so its values are accessed through `math.add` and `math.PI`. Both forms load the same module. The difference is whether selected exports become separate variables or remain properties of the module object.

A CommonJS module does not have to export any values. If a file never changes `module.exports`, it keeps its initial empty object. Consider a module that creates a value without exporting it.

```js
// unexported.js
const message = "This value is not exported";
```

Requiring this module returns the initial empty export object because `unexported.js` never changes `module.exports`.

```js
// main.js
const unexported = require("./unexported.js");

console.log(unexported); // {}
```

The file is still loaded and executed, but `message` is unavailable through `unexported` because it was never exported. Only values made available through `module.exports` are returned by `require()`.

For CommonJS project modules, the `.js` extension can usually be omitted because Node.js first checks the requested path and can then try supported file extensions such as `.js` when resolving the module.

```js
const math = require("./mathUtils");

console.log(math.add(2, 3)); // 5
```

This loads the same module as `require("./mathUtils.js")`. Including the extension makes the filename explicit, while omitting it is also common in CommonJS code.

After a CommonJS module is loaded successfully, Node.js caches it for the lifetime of the process. Requiring the same module again does not execute its code again. Instead, `require()` returns the cached exported value, so files that require the same module receive the same exported object reference.

!!! info "Modules are loaded once"

    When more than one file requires the same module, those files share the same exported object. Changes made to that object can therefore be visible through another reference to it. More detailed caching and module resolution behavior is covered in **Modules Level 3**.

!!! warning "Cannot Find a Module"

    If Node.js cannot locate a requested module, it reports an error such as `Error: Cannot find module './mathUtils.js'`. Check that the filename and relative path are correct. A path beginning with `./` refers to a location relative to the current module. To load a module from a parent directory, a relative path can begin with `../`, as in `require("../shared/config.js")`.

The main files from the earlier examples might be organized like this.

```text
calculator-app/
├── main.js
└── mathUtils.js
```

When `node main.js` is run from the command line, Node.js loads `mathUtils.js`, makes its exported values available to `main.js`, and executes the program.

Built-in modules are referenced by name, while project modules are referenced by relative paths. Together, `module.exports` and `require()` provide the foundation for organizing Node.js programs with CommonJS modules. **Modules Level 2** builds on this foundation with the ES module format, including default and named exports, before examining module resolution in greater detail.
