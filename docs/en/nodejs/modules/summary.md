# Summary

This summary brings together the most important concepts from the **Modules** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, relationships and differences need to be explained clearly.

## Table of Contents: Modules

- [Level 1](#level-1)
- [Level 2](#level-2)

## Level 1

Level 1 establishes the foundations of **modules, built-in modules, CommonJS, `require()` and `module.exports`**. The main goal is to understand how Node.js divides programs into separate files and how those files make code available to one another.

A **module** is a file containing JavaScript code that can be used by other files. Dividing a program into modules helps keep related functionality together and makes larger programs easier to organize and maintain. Code in one file is not automatically available in another file, so values that need to be shared must be explicitly exported and loaded.

Node.js provides **built-in modules** for common tasks such as working with file paths, the operating system and the file system. A built-in module is loaded by passing its name to `require()`.

```js
const path = require("node:path");

console.log(path); // Displays the module object
```

The `node:` prefix explicitly identifies a built-in Node.js module. For most built-in modules, the prefix is optional, so `require("node:path")` and `require("path")` both load the built-in `path` module.

A project can also contain its own modules. In the **CommonJS** module format, a file makes values available to other files through **`module.exports`**, which initially refers to an empty object.

```js
// mathUtils.js
function add(a, b) {
    return a + b;
}

const PI = 3.14159;

module.exports = { add, PI };
```

This module exports the `add` function and the `PI` constant. Assigning a new object to `module.exports` determines the value that another module receives when it requires this file. Exported properties can also be added individually, such as with `module.exports.add = add`.

A project module is loaded with `require()` by providing a **relative path**. A path beginning with `./` refers to a location relative to the current module.

```js
// main.js
const { add, PI } = require("./mathUtils.js");

console.log(add(2, 3)); // 5
console.log(PI); // 3.14159
```

Here, destructuring assigns selected exports to separate variables. The complete exported object can instead be assigned to one variable.

```js
// main.js
const math = require("./mathUtils.js");

console.log(math.add(2, 3)); // 5
console.log(math.PI); // 3.14159
```

Both forms load the same module. Destructuring creates separate variables for selected exports, while assigning the whole object keeps those exports as properties of the module variable.

A CommonJS module does not have to export any values. If a file never changes `module.exports`, requiring it returns the initial empty object `{}`. Values declared inside that file remain unavailable through the returned object unless they are exported.

For project modules, `./` refers to a location relative to the current module, while `../` can refer to a location in a parent directory. For JavaScript files, the `.js` extension can usually be omitted because Node.js can automatically resolve a matching `.js` file. If Node.js cannot locate the requested module, it reports an error such as `Error: Cannot find module './mathUtils.js'`.

The important distinction is that **built-in modules are referenced by module name**, while **project modules are referenced by relative paths**. In CommonJS, **`module.exports` determines what a module makes available**, while **`require()` loads the exported value of another module**.

After reviewing Level 1, you should be able to explain **what a module is and why modules are useful**, recognize and load **built-in Node.js modules**, describe the purpose of the **`node:` prefix**, export project values with **`module.exports`**, load project modules with **`require()`**, distinguish **module names from relative module paths**, recognize the roles of **`./` and `../`**, explain optional `.js` resolution, and use either destructuring or the complete exported object to access exported values.

## Level 2

Level 2 builds on CommonJS by introducing **ECMAScript modules, `import`, `export`, module configuration, re-exports and module specifiers**. The main goal is to understand how the standardized ES module format organizes and loads code in modern Node.js projects.

Node.js supports both **CommonJS** and **ECMAScript modules**, usually called **ES modules** or **ESM**. CommonJS uses `require()` and `module.exports`, while ESM uses the standardized `import` and `export` syntax.

For Node.js to interpret `.js` files as ES modules, a project can declare `"type": "module"` in `package.json`. An individual file can instead use the `.mjs` extension to identify itself explicitly as an ES module.

```json
{
    "type": "module"
}
```

ES modules can provide **default exports** and **named exports**. A default export represents the module's single default value, while named exports allow a module to expose multiple values by name.

```js
// calculateTotal.js
export default function calculateTotal(price, quantity) {
    return price * quantity;
}
```

A default export is imported without braces, and the importing file chooses the local name.

```js
// main.js
import calculateTotal from "./calculateTotal.js";

console.log(calculateTotal(10, 3)); // 30
```

Named exports are imported with braces and use their exported names unless they are renamed with `as`.

```js
// mathUtils.js
export function add(a, b) {
    return a + b;
}

export const PI = 3.14159;
```

The named values can then be imported together.

```js
// main.js
import { add, PI } from "./mathUtils.js";

console.log(add(2, 3)); // 5
console.log(PI); // 3.14159
```

An ES module can also **re-export** values from other modules. A shared entry point used mainly to re-export related values is commonly called a **barrel file**.

```js
// utils/index.js
export { add } from "./math.js";
export { capitalize } from "./text.js";
```

Other modules can then import the re-exported values through the barrel rather than importing each source file separately. The `export * from` syntax can forward named exports without listing each one, but it does not forward a module's default export. A default export must be re-exported explicitly.

```js
// utils/index.js
export { default as calculateTotal } from "../calculateTotal.js";
```

Here, the barrel is located in `utils/index.js`, while `calculateTotal.js` is in the project root, so `../` moves up one directory. The default export becomes the named export `calculateTotal` of the barrel.

A **module specifier** is the string that identifies what an `import` statement loads. Relative specifiers such as `./mathUtils.js` and `../calculateTotal.js` identify project files, while built-in Node.js modules can use specifiers such as `node:path`. Package specifiers identify modules provided by installed packages. These different forms allow Node.js to determine where a requested module should be located.

!!! info "Barrel files are optional"

    A barrel file is an organizational convenience rather than a requirement of ES modules. Direct imports can remain simpler when only a small number of modules are involved.

After reviewing Level 2, you should be able to distinguish **CommonJS from ES modules**, explain how Node.js recognizes ESM through **`"type": "module"` and `.mjs`**, create and import **default and named exports**, recognize how named imports can be grouped or renamed, explain **re-exports and barrel files**, distinguish named re-exports from default re-exports, and describe how **module specifiers** identify project files, built-in modules and installed packages.
