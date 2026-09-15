# Summary

This summary brings together the most important concepts from the **Code Quality and Formatting** module. It is designed as a quick reference for revision and preparation for questions where the main concepts, tools, configuration choices, and differences need to be explained clearly.

## Table of Contents: Code Quality and Formatting

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **code quality, formatting, linting, ESLint, Prettier, project configuration, package scripts, and editor integration**. The main goal is to understand the separate responsibilities of linting and formatting and how automated tools can provide a consistent code-quality workflow for a JavaScript project.

**Code quality** describes characteristics that make source code easier to understand, maintain, and change. **Formatting** controls the visual presentation of that code, including indentation, spacing, quotation style, semicolons, and line wrapping. A program can work correctly while still containing code-quality problems or inconsistent formatting, so automated tools are useful for checking these concerns consistently.

**Linting** and **formatting** solve different problems. ESLint analyzes source code for problems that match configured rules, while Prettier rewrites supported code into a consistent visual style. A useful distinction is that **ESLint checks the code, while Prettier formats how the code looks**.

For example, the following code is formatted clearly but contains an unused variable.

```js
const userName = "Example";

console.log("Hello");
```

ESLint can report `userName` because it is assigned a value but never used. This is a code-quality problem rather than a formatting problem.

Prettier instead handles code such as the following.

```js
const message="Hello"
console.log( message )
```

After formatting, the same code can be presented consistently.

```js
const message = 'Hello';
console.log(message);
```

ESLint and Prettier are development tools, so they are normally installed as **development dependencies**. ESLint uses `eslint.config.js` to define the configuration applied when source files are checked. The recommended JavaScript configuration from `@eslint/js` provides a useful starting point.

```js
import js from "@eslint/js";

export default [
  js.configs.recommended,
];
```

When ESLint checks a project, a reported problem identifies the location, severity, message, and rule responsible for the report. For example, an unused variable can produce output similar to this.

```bash
2:7  error  'unusedValue' is assigned a value but never used  no-unused-vars
✖ 1 problem (1 error, 0 warnings)
```

The rule name, such as `no-unused-vars`, can be looked up in the [official ESLint rules documentation](https://eslint.org/docs/latest/rules/). Rule pages explain what a rule checks, provide examples, and describe available options. ESLint can also be extended with **plugins** when a project requires rules for a particular environment or technology. The [official ESLint plugin documentation](https://eslint.org/docs/latest/use/configure/plugins) explains how plugins are added to a configuration.

Some ESLint rules support automatic fixes. The `--fix` option asks ESLint to apply fixes that can be performed safely, but not every reported problem has an automatic solution. Problems that cannot be fixed safely remain for the developer to review and correct.

**Prettier** uses its own configuration to define formatting preferences. A project can store these options in `.prettierrc.json`.

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 80
}
```

These options configure semicolons, preferred quotation style, indentation width, and preferred line width. The [official Prettier options documentation](https://prettier.io/docs/options) provides the reference for available formatting options and their supported values.

Prettier can either change files or only check them. The `--write` option formats supported files and saves the changes, while `--check` reports whether files already follow the configured formatting without modifying them. Paths that should not be formatted can be placed in `.prettierignore`.

Prettier supports many common file formats directly and can also be extended when additional language or formatting support is required. The [official Prettier plugin documentation](https://prettier.io/docs/plugins) explains how Prettier plugins extend its capabilities.

ESLint and Prettier can be used in the same project, but their responsibilities should remain separate. **`eslint-config-prettier`** disables ESLint rules that are known to conflict with Prettier. It is placed after other ESLint configurations so conflicting stylistic rules can be disabled.

```js
import js from "@eslint/js";
import eslintConfigPrettier from "eslint-config-prettier";

export default [
  js.configs.recommended,
  eslintConfigPrettier,
];
```

This configuration does not make ESLint run Prettier. ESLint continues to lint the code, while Prettier continues to format it. `eslint-config-prettier` only prevents unnecessary conflicts between those responsibilities.

Common linting and formatting tasks can be stored as **package scripts** in `package.json`. The script definitions belong to the project rather than to a particular package manager, so the same named tasks can be used through the package manager chosen by the project.

```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check ."
  }
}
```

The `lint` script checks the project, `lint:fix` requests supported ESLint fixes, `format` asks Prettier to rewrite supported files, and `format:check` verifies formatting without modifying files. Package scripts provide predictable project commands without requiring developers to remember the complete underlying tool commands.

Code editors can also integrate with these tools. In **Visual Studio Code**, the ESLint extension can display linting feedback while code is being edited, while the Prettier extension can provide formatting and format-on-save behavior. Editor integration improves the development experience, but project configuration and package scripts remain important because they can be used independently of a particular editor.

When additional rules, options, or plugins are needed, the official ESLint and Prettier documentation should be the starting point. A developer should first determine whether the required behavior is already built into the tool and then introduce a plugin or additional configuration only when the project has a specific need for it.

After reviewing Level 1, you should be able to explain **why code quality and consistent formatting matter**, distinguish **linting from formatting**, describe the separate roles of **ESLint and Prettier**, configure ESLint with `eslint.config.js`, recognize the information in an ESLint error report, explain the purpose and limits of `--fix`, configure Prettier with `.prettierrc.json`, distinguish `--write` from `--check`, explain the purpose of `.prettierignore`, describe how **`eslint-config-prettier` prevents conflicts**, define reusable **package scripts**, explain the role of optional **editor integration**, and use the official ESLint and Prettier documentation to investigate additional **rules, options, and plugins**.
