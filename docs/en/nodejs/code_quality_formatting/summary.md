# Summary

This summary brings together the most important concepts from the **Code Quality and Formatting** module. It is designed as a quick reference for reviewing what should be understood from Level 1, including the main tools, configuration choices, commands, and differences between workflows.

## Table of Contents: Code Quality and Formatting

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **code quality, linting, formatting, ESLint, Prettier, project configuration, package scripts, and editor integration**. The main idea to understand is that linting and formatting have separate responsibilities, even when they are connected as part of the same development workflow. **Code quality** concerns keeping source code understandable, consistent, and easier to maintain as a project grows. **Linting** analyzes source code for problems according to configured rules, while **formatting** controls how source code is visually presented. In this workflow, ESLint handles linting and Prettier handles formatting.

A useful distinction to remember is that **ESLint checks code according to rules, while Prettier formats how code is presented**. For example, an unused variable can be reported by ESLint even when the code is already formatted correctly. Prettier can correct inconsistent spacing, indentation, quotation style, semicolons, and line wrapping, but it does not replace ESLint's code quality rules.

ESLint is configured through a flat configuration file such as `eslint.config.js` or `eslint.config.mjs`. For the Node.js JavaScript project used in Level 1, the generated configuration contains the main structure shown below.

```js
import { defineConfig } from "eslint/config";
import globals from "globals";
import js from "@eslint/js";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: { globals: globals.node },
  },
]);
```

`defineConfig` defines the exported ESLint configuration. `files` selects the JavaScript files to which the configuration applies. `plugins: { js }` registers the imported `@eslint/js` package under the local name `js`, allowing `"js/recommended"` to provide ESLint's recommended JavaScript checks. `globals.node` tells ESLint about global names provided by the Node.js environment.

Project specific ESLint rules are added through the `rules` property.

```js
rules: {
  "no-unused-vars": "warn",
  eqeqeq: "error",
  curly: "error",
}
```

`no-unused-vars` reports variables that are declared but never used. `eqeqeq` requires strict equality operators such as `===` and `!==`. `curly` requires curly braces around control statements. ESLint rules can use `"off"`, `"warn"`, or `"error"` as severity levels. `"off"` disables a rule, `"warn"` reports a warning, and `"error"` reports an error that produces a nonzero exit code when a violation is found. An ESLint report identifies the location of the problem, its severity, the message, and the rule that reported it. The rule name can be used to find more information in the [official ESLint rules documentation](https://eslint.org/docs/latest/rules/). Some ESLint rules also support automatic fixes through `--fix`. This option applies fixes that ESLint can perform safely, while problems without an automatic fix still require a manual change.

ESLint can also exclude files and directories that should not be analyzed. With flat configuration, `globalIgnores` can be imported from `eslint/config`.

```js
import { defineConfig, globalIgnores } from "eslint/config";

export default defineConfig([
  globalIgnores(["dist/", "build/", "coverage/"]),
  // Existing project configuration
]);
```

`globalIgnores` controls files skipped by ESLint. This is separate from Prettier's ignore behavior. ESLint already ignores common locations such as `node_modules` and `.git` by default, so they normally do not need to be added manually.

Prettier can use its default formatting behavior without a custom configuration. When a project needs different formatting choices, they can be stored in `.prettierrc.json`.

```json
{
  "semi": true,
  "singleQuote": false,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "all",
  "printWidth": 80
}
```

These options control semicolons, quotation style, indentation, trailing commas, and preferred line width. The same options can instead be stored under the `prettier` property in `package.json`. A project normally chooses one configuration location rather than duplicating the same settings.

Prettier uses `.prettierignore` to identify files and directories that direct Prettier formatting should skip.

```text
# Build output
dist/
build/

# Test coverage
coverage/

# Generated and minified files
*.min.js
*.min.css
```

The important difference is that Prettier configuration defines **how files are formatted**, while `.prettierignore` defines **which files direct Prettier commands skip**. ESLint exclusions remain separate and are controlled through ESLint configuration such as `globalIgnores`. Prettier can either apply formatting or check whether formatting is already correct. `--write` formats files and saves the changes, while `--check` verifies formatting without modifying files. `--check` is useful when formatting should be verified rather than changed automatically, including verification workflows such as continuous integration.

ESLint and Prettier can work together in two different ways. When they remain independent, `eslint-config-prettier` disables ESLint rules that could conflict with Prettier.

```js
import { defineConfig, globalIgnores } from "eslint/config";
import globals from "globals";
import js from "@eslint/js";
import eslintConfigPrettier from "eslint-config-prettier/flat";

export default defineConfig([
  globalIgnores(["dist/", "build/", "coverage/"]),
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: { globals: globals.node },
    rules: {
      "no-unused-vars": "warn",
      eqeqeq: "error",
      curly: "error",
    },
  },
  eslintConfigPrettier,
]);
```

`eslint-config-prettier` only prevents conflicting ESLint formatting rules. It does not run Prettier. ESLint continues to lint the code, while Prettier continues to format it separately.

A project can instead use `eslint-plugin-prettier/recommended` to run Prettier through ESLint.

```js
import { defineConfig, globalIgnores } from "eslint/config";
import globals from "globals";
import js from "@eslint/js";
import eslintPluginPrettierRecommended from "eslint-plugin-prettier/recommended";

export default defineConfig([
  globalIgnores(["dist/", "build/", "coverage/"]),
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: { globals: globals.node },
    rules: {
      "no-unused-vars": "warn",
      eqeqeq: "error",
      curly: "error",
    },
  },
  eslintPluginPrettierRecommended,
]);
```

`eslint-plugin-prettier/recommended` enables the `prettier/prettier` rule and includes the configuration that prevents conflicting ESLint formatting rules. Prettier formatting differences can therefore be reported through ESLint. Custom Prettier options can also be supplied to `prettier/prettier` in `eslint.config.js`, so a separate `.prettierrc.json` is not required when those formatting options are kept there. The main difference to remember is that **`eslint-config-prettier` prevents conflicts while ESLint and Prettier remain separate, while `eslint-plugin-prettier/recommended` runs Prettier through ESLint**. When Prettier runs directly, `.prettierignore` controls which files Prettier skips. When Prettier runs through ESLint, ESLint controls which files reach the `prettier/prettier` rule, so ESLint file selection and `globalIgnores` control that workflow.

**Package scripts** provide reusable names for common linting and formatting tasks. When ESLint and Prettier remain independent, the project can use the following scripts.

```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "check": "eslint . && prettier --check .",
    "fix": "eslint . --fix && prettier --write ."
  }
}
```

`lint` checks the project with ESLint, while `lint:fix` applies supported ESLint fixes. `format` applies Prettier formatting, while `format:check` verifies formatting without changing files. `check` verifies both linting and formatting, while `fix` applies supported ESLint fixes and Prettier formatting.

When Prettier runs through `eslint-plugin-prettier`, the basic workflow can use ESLint alone.

```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix"
  }
}
```

In this workflow, `lint` can report ESLint rule violations and Prettier formatting differences, while `lint:fix` can apply supported fixes from both. Package managers use different syntax to execute package scripts, but the script definitions stored in `package.json` remain the same.

ESLint and Prettier are project dependencies, while editor extensions provide integration with the development environment. In Visual Studio Code, the ESLint extension can display linting feedback and apply supported fixes. When ESLint and Prettier run independently, the Prettier extension can provide Prettier formatting and formatting on save. When Prettier runs through ESLint, the ESLint extension can apply supported ESLint and Prettier fixes through the same save workflow.

After reviewing Level 1, the main concepts to know are **why code quality and consistent formatting matter**, **how linting differs from formatting**, **the separate responsibilities of ESLint and Prettier**, **how the generated ESLint configuration works**, **how rules and severity levels work**, **what ESLint reports contain**, **what `--fix` does**, **how `globalIgnores` controls ESLint exclusions**, **how Prettier configuration and `.prettierignore` differ**, **how `--write` differs from `--check`**, **how `eslint-config-prettier` differs from `eslint-plugin-prettier/recommended`**, **how package scripts reflect the selected workflow**, and **how editor integration works with the project tooling**.
