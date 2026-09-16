# Level 1

## Table of Contents: Code Quality and Formatting

- [Why Code Quality and Formatting Matter](#why-code-quality-and-formatting-matter)
- [Development Environment and Editor Setup](#development-environment-and-editor-setup)
- [Setting Up ESLint](#setting-up-eslint)
- [Understanding the Generated ESLint Configuration](#understanding-the-generated-eslint-configuration)
- [Running ESLint](#running-eslint)
- [Configuring ESLint Rules](#configuring-eslint-rules)
- [Setting Up Prettier](#setting-up-prettier)
- [Configuring Prettier](#configuring-prettier)
- [Connecting ESLint and Prettier](#connecting-eslint-and-prettier)
- [Scripts for Linting and Formatting](#scripts-for-linting-and-formatting)

**Code Quality and Formatting Level 1** introduces the foundations of keeping JavaScript source code consistent, readable, and easier to maintain. It introduces linting and formatting as separate responsibilities and presents ESLint and Prettier as tools for these tasks. Throughout the level, you will learn how to set up and configure both tools, check code for problems, apply consistent formatting, use them together without conflicting responsibilities, create reusable package scripts, and integrate them with an editor.

## Why Code Quality and Formatting Matter

A program can execute correctly and still be difficult to read, change, or maintain. As a project grows, developers need source code that remains clear and consistent so they can understand existing work and make changes without unnecessary confusion.

Consistent code is easier to read because similar structures are presented in similar ways throughout a project. Developers can spend less time interpreting different styles and more time understanding what the code does. This becomes increasingly important when several people contribute to the same codebase.

Code quality also supports maintainability. Clear and consistent source code makes it easier to review changes, locate problems, and return to code after time has passed. Small inconsistencies may not prevent a program from running, but they can accumulate and make a project harder to work with as it becomes larger.

For example, the following JavaScript can work even though its structure is difficult to scan.

```js
const userName="Example"

if(userName){console.log("Hello, "+userName)}
```

The same behavior can be expressed more clearly.

```js
const userName = "Example";

if (userName) {
  console.log("Hello, " + userName);
}
```

The second version makes the structure easier to recognize without changing the intended behavior. Establishing consistent expectations for code helps keep this clarity throughout a project rather than relying on individual habits.

!!! info "Maintainable Code"

    Working code produces the expected result. Maintainable code also remains clear enough to understand, review,
    and change as the project develops.

As a project grows, maintaining these qualities manually becomes increasingly difficult. Automated tools can make the same expectations repeatable across the project. Before setting up those tools, it is useful to establish how the project environment and editor work with them.

## Development Environment and Editor Setup

Code-quality and formatting tools are installed as project dependencies, while editor extensions provide integration inside a development environment. This separation allows the project tooling to work from the terminal and through package scripts regardless of which editor a developer uses. This level uses **Visual Studio Code** as the editor example.

Visual Studio Code includes basic JavaScript formatting, so the Prettier extension is not required simply to format JavaScript. A project that specifically uses Prettier can install the [Prettier - Code formatter extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) to apply the project's Prettier formatting directly in the editor. The [Visual Studio Code JavaScript documentation](https://code.visualstudio.com/docs/languages/javascript) explains the built-in JavaScript formatting and editor features.

For ESLint integration, install the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint). It connects Visual Studio Code with ESLint in the project so linting problems can appear while code is being edited and supported fixes can be applied through editor actions. These extensions do not replace the ESLint or Prettier packages installed in the project. The project dependencies provide the actual tools and their versions, while the extensions add editor features.

Visual Studio Code supports project-specific settings through `.vscode/settings.json`. Create the `.vscode` directory in the project root and add `settings.json` inside it. The settings used in this file depend on how ESLint and Prettier are connected later in the level.

When ESLint and Prettier run independently, `.vscode/settings.json` can use the Prettier extension as the default formatter and format files when they are saved. These settings take effect once Prettier is installed later in this level.

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true
}
```

`editor.defaultFormatter` selects Prettier as the formatter, while `editor.formatOnSave` runs it whenever a file is saved. This allows the editor to use the same Prettier formatting behavior configured for the project.

If Prettier instead runs through `eslint-plugin-prettier`, the ESLint extension can apply ESLint fixes and supported Prettier formatting through the same save action.

```json
{
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}
```

In this workflow, a separate Prettier format-on-save action is unnecessary because Prettier is already part of the ESLint fix process.

!!! info "Choose the Editor Integration That Matches the Project"

    Use the Prettier extension when Prettier runs directly as the editor formatter. When Prettier runs through ESLint, the ESLint extension can provide the integrated save workflow instead.

With the development environment prepared and the role of project tooling and editor integration established, the next section sets up ESLint for automated JavaScript code-quality checks.

## Setting Up ESLint

ESLint analyzes JavaScript source code and reports problems according to a configured set of rules, providing a repeatable way to apply the same code-quality expectations as a codebase grows. The [official ESLint Getting Started guide](https://eslint.org/docs/latest/use/getting-started) provides the current setup process for adding ESLint to a project.

Before starting, the project should already contain a `package.json` file. Follow the Getting Started guide and use the setup command shown for the package manager used by the project. ESLint then asks several questions about the project so it can install the required dependencies and generate an appropriate configuration. For a Node.js JavaScript project, choose the following options.

1. **What do you want to lint?** Select **JavaScript**.
2. **How would you like to use ESLint?** Select **To check syntax and find problems**.
3. **What type of modules does your project use?** Select **JavaScript modules (import/export)**.
4. **Which framework does your project use?** Select **None of these**.
5. **Does your project use TypeScript?** Select **No**.
6. **Where does your code run?** Select **Node**.
7. When ESLint lists the required dependencies, choose to install them.
8. Select the package manager used by the project when ESLint asks how the dependencies should be installed.

These choices describe the project ESLint is being configured for. The project uses JavaScript with ECMAScript modules, does not use a framework or TypeScript, and runs in Node.js. ESLint uses these answers to determine the initial configuration and the packages needed to support it.

After setup is complete, ESLint creates a configuration file such as `eslint.config.js` or `eslint.config.mjs` and installs the dependencies required by the selected options. The configuration is generated from the choices made during setup rather than being written manually from the beginning.

!!! tip "Follow the Current ESLint Guide"

    ESLint setup can change as the tool develops. Use the official Getting Started guide for the current setup command and follow the project choices described in this level.

The setup process creates an ESLint configuration based on the selected project options. The next section examines this generated configuration and explains how its main parts control linting.

## Understanding the Generated ESLint Configuration

The generated `eslint.config.js` or `eslint.config.mjs` file defines how ESLint applies its configuration to the project. For a Node.js JavaScript project, it can look similar to the following.

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

The [official ESLint configuration documentation](https://eslint.org/docs/latest/use/configure/) provides the complete reference for configuration files and their available options. In this generated file, `defineConfig` defines the exported ESLint configuration, `globals` provides predefined global variables for JavaScript environments, and `@eslint/js` provides ESLint's JavaScript configurations.

The `files` pattern applies this configuration to `.js`, `.mjs`, and `.cjs` files throughout the project. `plugins: { js }` registers the imported `@eslint/js` package under the local name `js`, allowing `"js/recommended"` to be referenced through `extends`. The `languageOptions` setting adds `globals.node`, which tells ESLint about global names provided by the Node.js environment.

At this stage, the important point is how the generated configuration describes the project's JavaScript files and runtime. The recommended configuration also supplies ESLint's starting checks, but individual rules and their severity levels are covered later after ESLint has been run.

!!! info "Generated Configuration"

    ESLint creates the initial configuration from the project choices made during setup. It can later be adjusted as the project's linting requirements change.

With the generated configuration understood, the next section runs ESLint and examines how it reports problems in the project.

## Running ESLint

ESLint can now check the project from the terminal using the generated configuration. The [official ESLint command line documentation](https://eslint.org/docs/latest/use/command-line-interface) provides the current execution commands for supported package managers.

Because ESLint is installed locally, it can be executed through the package manager used by the project. ESLint reads the configuration, checks matching JavaScript files, and reports problems found by the enabled checks. Each report identifies where a problem was found and which ESLint rule reported it.

Some reported problems support automatic correction through ESLint's `--fix` option, while others require a manual change because ESLint cannot safely determine the intended solution.

!!! warning "Automatic Fixes Have Limits"

    `--fix` only changes problems for which ESLint provides an automatic fix. Other reported problems still require a manual change.

After seeing how ESLint reports a problem, the next section explains how individual rules and their severity levels can be adjusted for the project.

## Configuring ESLint Rules

ESLint rules define specific code-quality expectations. The generated `"js/recommended"` configuration already enables a useful starting set of rules for common JavaScript problems. The [official ESLint rules documentation](https://eslint.org/docs/latest/rules/) describes the available built-in rules, while the [official rule configuration documentation](https://eslint.org/docs/latest/use/configure/rules) explains how they can be enabled, disabled, and customized.

For this project, a small set of rule adjustments can be added directly to the existing configuration.

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
    rules: {
      "no-unused-vars": "warn",
      eqeqeq: "error",
      curly: "error",
    },
  },
]);
```

The three imports at the beginning provide the values used later in the configuration. `defineConfig` comes from ESLint itself and is used to define and export the configuration. `globals` comes from the `globals` package and contains predefined global variables for different JavaScript environments. It is used later as `globals.node` so ESLint recognizes globals provided by Node.js. `js` comes from the `@eslint/js` package and provides ESLint's JavaScript configurations. Registering it with `plugins: { js }` makes the local name `js` available to the configuration, which is then used by `"js/recommended"` in `extends`.

The `rules` property adds project-specific choices on top of that recommended configuration. `no-unused-vars` reports variables that are declared but never used. It is already enabled by `"js/recommended"`, but setting it to `"warn"` changes its severity for this project. `eqeqeq` requires strict equality operators such as `===` and `!==`, while `curly` requires curly braces around control statements such as `if`, `else`, `for`, and `while`.

Each rule has a severity that determines how ESLint handles a violation. `"off"` disables the rule, `"warn"` reports a warning without affecting the normal exit code, and `"error"` reports an error and causes ESLint to finish with a nonzero exit code when a violation is found. Some rules also accept additional options, which are documented on their individual rule pages.

!!! tip "Add Rules with a Purpose"

    Start with the recommended configuration and add or adjust rules when they express a clear code-quality expectation for the project. Avoid adding large collections of rules without understanding what they check.

With the project's ESLint rules configured, the next section introduces Prettier for the separate task of formatting source code.

## Setting Up Prettier

Prettier handles source-code formatting separately from the code-quality rules checked by ESLint. The [official Prettier installation guide](https://prettier.io/docs/install) provides the current installation instructions for supported package managers and recommends installing an exact version locally in the project.

After installation, Prettier can format supported files using its default behavior without requiring custom formatting options. How those options are stored depends on the workflow the project chooses, which is covered in the next section.

!!! info "Local Prettier Installation"

    Keeping Prettier in the project gives the project a consistent formatter version that can also be used by command-line tools and supported editor integrations.

With Prettier installed, the next section looks at the available ways to configure its formatting behavior.

## Configuring Prettier

Prettier provides formatting defaults, so a project only needs a configuration when it wants to change them. The [official Prettier configuration documentation](https://prettier.io/docs/configuration) explains the supported configuration methods, while the [official Prettier options documentation](https://prettier.io/docs/options) describes the available formatting choices.

When Prettier runs independently, custom options can be stored in a `.prettierrc.json` file in the project root.

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

These options define several common formatting choices. `semi` keeps semicolons at the ends of statements, while `singleQuote` set to `false` keeps double quotes as the preferred quote style. `tabWidth` uses two spaces for each indentation level, and `useTabs` set to `false` keeps indentation space based. `trailingComma` allows trailing commas wherever Prettier supports them, while `printWidth` gives Prettier a preferred line length when deciding how code should wrap.

Instead of creating a separate Prettier configuration file, the same options can be stored under the `prettier` property in `package.json`.

```json
{
  "name": "example-project",
  "version": "1.0.0",
  "type": "module",
  "prettier": {
    "semi": true,
    "singleQuote": false,
    "tabWidth": 2,
    "useTabs": false,
    "trailingComma": "all",
    "printWidth": 80
  }
}
```

A project normally chooses one configuration location rather than duplicating the same options. If the default formatting behavior is sufficient, no custom Prettier configuration is required.

Prettier can also use a `.prettierignore` file in the project root to identify files and directories that should not be formatted. This file serves a different purpose from `.prettierrc.json` or the `prettier` property in `package.json`. The configuration defines **how** Prettier formats files, while `.prettierignore` defines **which files Prettier should skip**.

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

A `.prettierignore` file is useful for generated output, coverage files, minified files, or other project content that should remain untouched. Prettier's CLI already ignores `node_modules` by default, so installed dependencies normally do not need to be added manually.

The ignore file is useful regardless of where the formatting options are stored. A project can therefore use `.prettierignore` alongside `.prettierrc.json`, alongside the `prettier` property in `package.json`, or without a custom Prettier configuration when the default formatting options are sufficient.

It can also remain useful when Prettier is later connected to ESLint through `eslint-plugin-prettier`. In that workflow, formatting options can be placed in `eslint.config.js`, while `.prettierignore` continues to describe files that direct Prettier commands should skip. However, ignore behavior for files processed through ESLint is controlled by ESLint's own file selection and ignore configuration, so `.prettierignore` should not be treated as a replacement for ESLint ignores.

These configuration choices establish how Prettier behaves when it runs directly. The next section explains how ESLint and Prettier can work together and how the formatting configuration changes when Prettier is run through ESLint.

## Connecting ESLint and Prettier

ESLint checks code quality while Prettier handles formatting. When both tools are used in the same project, they can remain separate or Prettier can run through ESLint. The [Prettier linter integration documentation](https://prettier.io/docs/integrating-with-linters) explains the relationship between formatters and linters, while the [`eslint-plugin-prettier` package documentation](https://www.npmjs.com/package/eslint-plugin-prettier) provides the setup instructions for running Prettier through ESLint.

The usual approach keeps ESLint and Prettier independent. Some ESLint stylistic rules can conflict with Prettier, so `eslint-config-prettier` can be installed as a development dependency to disable those rules. The project can also use `globalIgnores` from `eslint/config` to exclude generated output and other files that ESLint should not analyze.

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

`globalIgnores` tells ESLint to skip the listed directories, while `eslintConfigPrettier` disables ESLint rules that could conflict with Prettier. These settings have different responsibilities. The ignore configuration controls which files ESLint analyzes, while `eslint-config-prettier` prevents rule conflicts. Prettier still runs separately in this workflow and can use `.prettierrc.json` or the `prettier` property in `package.json` for custom formatting options.

ESLint's ignore configuration is also separate from `.prettierignore`. `globalIgnores` controls files processed by ESLint, while `.prettierignore` controls files skipped by direct Prettier commands. ESLint already ignores common locations such as `node_modules` and `.git` by default, so they normally do not need to be listed manually.

A project can instead run Prettier through ESLint with `eslint-plugin-prettier`. Its recommended flat configuration is provided through `eslint-plugin-prettier/recommended` and includes the integration needed to enable the `prettier/prettier` rule and prevent conflicting ESLint formatting rules. Because ESLint now controls which files are processed, the same `globalIgnores` configuration continues to determine which files are excluded.

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

`eslintPluginPrettierRecommended` is the local name of the imported recommended configuration. Adding it after the project's ESLint configuration sets up `eslint-plugin-prettier`, enables `prettier/prettier`, and applies the conflict-prevention configuration. Prettier therefore runs as part of ESLint using its default formatting options.

If custom formatting options are needed, they can be supplied to the already enabled `prettier/prettier` rule. The recommended configuration must remain before the rule override because it creates the integration that the final configuration object customizes.

```js
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
  {
    rules: {
      "prettier/prettier": [
        "error",
        {
          semi: true,
          singleQuote: false,
          tabWidth: 2,
          useTabs: false,
          trailingComma: "all",
          printWidth: 80,
        },
      ],
    },
  },
]);
```

Here, `"error"` makes formatting differences ESLint errors, while the following object provides the Prettier options. A separate `.prettierrc.json` is not required when these options are kept in `eslint.config.js`. Files excluded by `globalIgnores` do not reach the `prettier/prettier` rule because ESLint skips them before applying its rules.

The main difference between the two workflows is where Prettier runs. `eslint-config-prettier` prevents rule conflicts while ESLint and Prettier remain separate, whereas `eslint-plugin-prettier/recommended` runs Prettier through ESLint and includes the conflict-prevention configuration.

!!! info "Choosing an Integration"

    Use `eslint-config-prettier` when ESLint and Prettier should run independently. Use `eslint-plugin-prettier/recommended` when Prettier should run through ESLint. ESLint exclusions belong in its configuration, while `.prettierignore` applies to direct Prettier formatting.

Once the project has chosen how ESLint and Prettier will work together, the same workflow can be made easier to run through package scripts.

## Scripts for Linting and Formatting

**Package scripts** provide reusable names for the linting and formatting commands used by a project. Their definitions should match the way ESLint and Prettier were connected in the previous section. When the tools run independently, scripts can expose each tool separately and combine them when both are needed. When Prettier runs through `eslint-plugin-prettier`, ESLint can handle the basic linting and formatting workflow through the same commands.

When ESLint and Prettier remain separate, the `scripts` property can provide commands for checking and fixing each responsibility.

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

`lint` checks the project with ESLint without changing files, while `lint:fix` applies fixes supported by ESLint rules. `format` uses Prettier with `--write` to rewrite files that do not match the configured formatting, while `format:check` verifies formatting without changing files. The non-writing `format:check` form is especially useful for verification workflows such as continuous integration, where the project should fail a check rather than modify files automatically. The combined `check` script runs ESLint and then verifies formatting, while `fix` applies supported ESLint fixes before formatting the project with Prettier. The `&&` operator runs the second command only when the first command finishes successfully.

This provides a command for each common task. Use `lint` or `format:check` when only one type of check is needed, and use `format` when the goal is specifically to rewrite files with Prettier. Use `check` when both code quality and formatting should be verified together, and use `fix` when both ESLint fixes and Prettier formatting should be applied.

If the project instead uses `eslint-plugin-prettier`, Prettier formatting is already reported through the `prettier/prettier` ESLint rule, so the basic workflow can use fewer scripts.

```json
{
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint . --fix"
  }
}
```

In this workflow, `lint` reports both ESLint rule violations and Prettier formatting differences. `lint:fix` applies supported fixes, including formatting corrections provided through the Prettier rule. Separate formatting scripts are therefore unnecessary for the basic ESLint-driven workflow.

Package managers use slightly different syntax for executing package scripts, but the definitions stored in `package.json` remain the same regardless of the package manager used by the project.

!!! info "Scripts Follow the Integration"

    When ESLint and Prettier run independently, package scripts can expose their separate responsibilities and provide combined commands when needed. When Prettier runs through `eslint-plugin-prettier`, the basic workflow can run through ESLint alone.

At this point, the project has a foundation for automated code quality and formatting that can be used consistently through reusable project commands. These foundations can later be extended with additional ESLint rules and plugins as the project's requirements become more specialized. A later Code Quality and Formatting **Code Quality and Formatting Level 2** can build on this foundation with Node-specific linting through tools such as `eslint-plugin-n`.
