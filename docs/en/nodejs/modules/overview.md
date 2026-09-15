# Overview

Modules provide a way to divide a Node.js program into smaller files with focused responsibilities. Instead of keeping all code in a single file, a program can separate related functions, values, and other logic into modules that can be loaded where they are needed. Node.js also provides built-in modules for common tasks, allowing programs to use existing functionality without creating it from scratch.

Node.js supports different module formats for organizing and sharing code. **CommonJS** uses `require()` and `module.exports`, while **ECMAScript modules**, usually called **ES modules** or **ESM**, use the standardized `import` and `export` syntax. Understanding both formats makes it possible to work with different Node.js projects and recognize how modules are configured and loaded.

The **Modules** module develops from the foundations of CommonJS to ES modules and the rules Node.js uses when locating and loading modules. Each level builds on the previous one while expanding how code can be organized, shared, and accessed across files.

**Level 1** introduces the foundations of modules in Node.js. It explains what a **module** is and how to load **built-in modules** with `require()`, including the optional `node:` prefix. It then introduces **CommonJS project modules**, showing how values are made available through `module.exports` and loaded from another file with `require()`. The level also explains the difference between built-in module names and relative project paths such as `./` and `../`, how Node.js can resolve `.js` files when the extension is omitted, and what happens when a CommonJS module does not export any values.

**Level 2** builds on these CommonJS foundations by introducing **ECMAScript modules** and the `import` and `export` syntax. It explains how Node.js recognizes ES modules through `"type": "module"` in `package.json` or the `.mjs` extension, and develops the use of **default and named exports**, imports, re-exports, and **barrel files**. It also introduces different module specifiers and the rules Node.js uses to locate modules when they are loaded.

Together, these concepts provide a foundation for organizing Node.js programs into clear and reusable modules. They support a progression from loading built-in functionality and sharing code between CommonJS files to working with standardized ES module syntax, project configuration, re-exports, and module resolution.
