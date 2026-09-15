# Level 1

## Table of Contents: Code Quality and Formatting

- [Why Code Quality and Formatting Matter](#why-code-quality-and-formatting-matter)
- [Linting vs Formatting](#linting-vs-formatting)
- [Installing the Tools](#installing-the-tools)
- [Configuring ESLint with eslint.config.js](#configuring-eslint-with-eslintconfigjs)
- [Configuring Prettier](#configuring-prettier)
- [Connecting ESLint and Prettier](#connecting-eslint-and-prettier)
- [Scripts for Linting and Formatting](#scripts-for-linting-and-formatting)

**Code Quality and Formatting Level 1** introduces the basic tools and practices used to keep JavaScript source code consistent and easier to maintain. It begins by explaining why readable and consistent code matters, then separates the roles of linting and formatting. The level introduces **ESLint** for detecting code problems and **Prettier** for applying consistent formatting. It then shows how to install and configure both tools, connect them without conflicting rules, create reusable npm scripts, and explains how editor integration can support the workflow.

## Why Code Quality and Formatting Matter

A program can execute correctly and still be difficult to read, change, or maintain. **Code quality** includes characteristics that make source code easier to understand and work with, while **formatting** controls the visual presentation of that code. Consistent indentation, spacing, quotation style, and line wrapping make files easier to scan because developers do not need to interpret a different visual style in every file.

Consistency becomes especially important when several developers work on the same project. If each person formats code manually according to personal preferences, unnecessary differences can appear in source files even when the program behavior has not changed. Automated tools reduce this problem by applying the same checks and formatting rules throughout the project.

The effect of consistent formatting is easiest to see by comparing two versions of the same code.

```js
const userName="Example"

if(userName){console.log("Hello, "+userName)}
```

The first version places the statements close together and uses inconsistent spacing, which makes the structure harder to recognize quickly. The same program can be written with clear spacing and indentation without changing what it does.

```js
const userName = "Example";

if (userName) {
  console.log("Hello, " + userName);
}
```

Both examples can express the same behavior, but the second is easier to scan because its structure is visually clear. In a real project, manually maintaining this consistency across many files becomes repetitive and unreliable. Development tools can perform much of this work automatically.

!!! info "Working Code and Maintainable Code"

    Code that produces the expected result is not automatically easy to maintain. Automated quality checks and consistent formatting help developers notice problems earlier and understand source code more quickly.

Automated tools can handle these concerns consistently, but they do not all solve the same problem. The next section separates **linting** from **formatting** so that the purpose of each tool is clear before the tools are installed.

## Linting vs Formatting

**Linting** and **formatting** improve code in different ways. **Linting checks the code itself.** ESLint looks for code that may be incorrect, unnecessary, or against the project's quality rules. For example, the following code is formatted clearly, but it still contains a problem.

```js
const userName = "Example";

console.log("Hello");
```

The spacing and indentation are fine, but `userName` is assigned a value and never used. ESLint can report this because it analyzes the code for quality problems rather than visual appearance.

**Formatting checks how the code looks.** Prettier does not decide whether a variable is useful or whether the program logic is good. It makes source code follow a consistent visual style. For example, the following code can work even though its formatting is inconsistent.

```js
const message="Hello"

console.log( message )
```

Prettier can format the same code automatically.

```js
const message = "Hello";

console.log(message);
```

The program still does the same thing. Prettier only changes its visual presentation by applying consistent spacing and statement formatting. A simple way to remember the difference is **ESLint finds problems in the code, while Prettier fixes the appearance of the code**.

!!! abstract "Linting vs Formatting"

    **ESLint** checks for code quality problems, while **Prettier** applies consistent formatting.

Both tools can also integrate with code editors such as **Visual Studio Code**. The ESLint extension can show linting problems while code is being written, while the Prettier extension can format supported files automatically. The project tools are installed and configured first, so editor integration can be added after the command line workflow is working.

Now that the difference is clear, the next section installs ESLint and Prettier so both can be used in the project.

## Installing the Tools

ESLint and Prettier are tools used while developing the project, so they are installed as **development dependencies** rather than packages required by the running application. The distinction between `dependencies` and `devDependencies` was introduced in **Package Management Level 1**. From the project folder, install ESLint, its official JavaScript configuration package, Prettier, and the configuration that prevents ESLint formatting rules from conflicting with Prettier.

```bash
npm install -D eslint @eslint/js prettier eslint-config-prettier
```

The `-D` option saves these packages under `devDependencies` in `package.json`. Because the tools are installed inside the project, their command line programs are also available locally. Instead of installing ESLint and Prettier globally on the computer, `npx` can run the versions installed in the current project. This is useful because the commands use the tools declared by that project.

After installation, use `npx` to confirm that the local ESLint and Prettier commands are available.

```bash
npx eslint --version
npx prettier --version
```

Each command asks the installed tool to print its version. If both commands display version information, the installation was successful and the project can use those local versions of ESLint and Prettier.

If you use **Visual Studio Code**, also install the **ESLint** extension and the **Prettier - Code formatter** extension from the Extensions view. The npm packages installed in the project provide the actual project tools, while the editor extensions connect those tools to Visual Studio Code. The ESLint extension can display linting problems while code is being edited, and the Prettier extension provides formatting directly in the editor.

!!! tip "Why Use npx Here?"

    `npm install -D` installs ESLint and Prettier in the project. `npx` then lets you run those locally installed command line tools directly. This avoids requiring a separate global installation.

The tools are now installed and can be run from the project. The next section configures ESLint so it knows which code quality rules to apply.

## Configuring ESLint with eslint.config.js

ESLint needs a configuration that tells it which rules to use when checking JavaScript. Modern ESLint projects can store this configuration in `eslint.config.js` at the project root. For this **Code Quality and Formatting Level 1**, create `eslint.config.js` with ESLint's recommended JavaScript rules, which provide a useful starting point without configuring individual rules one by one.

```js
import js from "@eslint/js";

export default [
    js.configs.recommended,
];
```

The first line imports the JavaScript configuration provided by the `@eslint/js` package that was installed earlier. The `export default` array then gives that recommended configuration to ESLint. When ESLint runs, it reads this file and uses those rules while checking the project's JavaScript.

This configuration uses ECMAScript module syntax with `import` and `export default`. If the project uses ECMAScript modules, `package.json` can include `"type": "module"` so Node.js treats the project's `.js` files as ECMAScript modules. Module systems are covered separately in the course, so for now the important point is that the project must support the module syntax used in `eslint.config.js`.

Once the configuration exists, run the locally installed ESLint with `npx`. The `.` means that ESLint should check files starting from the current project directory.

```bash
npx eslint .
```

For example, suppose a JavaScript file contains the following code.

```js
const message = "Hello";
const unusedValue = 42;

console.log(message);
```

ESLint reports `unusedValue` because the variable is assigned a value but never used. This is a code quality problem rather than a formatting problem, which connects back to the difference between linting and formatting from the previous section.

A report for this example looks similar to the following output. ESLint shows the location of the problem, describes what is wrong, and identifies the rule that reported it.

```bash
2:7  error  'unusedValue' is assigned a value but never used  no-unused-vars
✖ 1 problem (1 error, 0 warnings)
```

Some ESLint problems can be corrected automatically. Instead of only checking the project, add `--fix` to ask ESLint to apply the fixes that its rules support.

```bash
npx eslint . --fix
```

Not every problem has a safe automatic solution. If ESLint cannot determine the correct change, it reports the problem and leaves the code for the developer to fix.

!!! warning "Automatic Fixes Have Limits"

    `--fix` only changes problems that ESLint knows how to fix safely. Other reported problems still require the developer to decide how the code should be corrected.

When ESLint reports a rule name such as `no-unused-vars`, that rule name can be looked up in the [official ESLint rules documentation](https://eslint.org/docs/latest/rules/). The rule page explains what the rule checks, why it exists, examples of incorrect and correct code, available options, and whether the rule can apply automatic fixes. The broader [ESLint configuration documentation](https://eslint.org/docs/latest/use/configure/) explains how rules, files, language options, and other configuration features work.

ESLint can also be extended beyond its built-in rules. The [ESLint plugin documentation](https://eslint.org/docs/latest/use/configure/plugins) explains how plugins add rules and other capabilities to a project. When a project later introduces a framework, runtime, or language feature that needs additional linting support, students can check that technology's documentation and the package registry for an appropriate ESLint plugin rather than adding plugins without a specific need.

ESLint is now configured to check the project's JavaScript for code quality problems. The next section configures Prettier to handle the separate task of keeping the project's formatting consistent.

## Configuring Prettier

Prettier can format code using its default behavior, but a project configuration makes the chosen formatting style explicit and consistent for everyone working on the project. Create `.prettierrc.json` at the project root and define the basic formatting options in one place.

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 80
}
```

These options tell Prettier to use semicolons, prefer single quotes where appropriate, use two spaces for each indentation level, and use a preferred line width of 80 characters when deciding how to wrap supported code.

For example, suppose `app.js` contains code that works but is formatted inconsistently.

```js
const user={name:"Example",role:"developer"}

console.log("Hello",user.name)
```

Run the locally installed Prettier with `npx`. The `--write` option tells Prettier to format the files and save the changes, while `.` tells it to start from the current project directory.

```bash
npx prettier --write .
```

After Prettier applies the configuration, the same code is formatted consistently.

```js
const user = { name: 'Example', role: 'developer' };

console.log('Hello', user.name);
```

Prettier should format the project's source files rather than installed package files. A `.prettierignore` file tells Prettier which paths to skip. For example, the installed dependencies in `node_modules` do not need to be reformatted.

The `--write` command changes files, but sometimes the project only needs to check whether formatting is correct. In that case, use `--check` instead.

```bash
npx prettier --check .
```

`--write` formats files and saves the changes, while `--check` only reports whether the files already follow the configured formatting.

If you use **Visual Studio Code** with the Prettier extension installed, you can also make Prettier the default formatter and format supported files automatically whenever they are saved. Add the following settings to the appropriate Visual Studio Code `settings.json` file.

``` json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true
}
```

With `editor.formatOnSave` enabled, saving a supported file asks Prettier to format it automatically. This is convenient during development, but it does not replace the project commands. `npm run lint` and `npm run format:check` remain useful because they work independently of a particular editor and can verify the project as a whole.

The [official Prettier options documentation](https://prettier.io/docs/options) is the reference for settings such as `semi`, `singleQuote`, `tabWidth`, and `printWidth`. Students should use that reference when they want to understand an option or see which values are supported. Prettier already supports JavaScript and many common web formats, while the [Prettier plugin documentation](https://prettier.io/docs/plugins) explains how plugins can add support for additional languages or formatting behavior when a project actually requires it.

With ESLint checking code quality and Prettier handling formatting, both tools now have their own clear responsibilities. The next section connects their configurations so ESLint does not use formatting rules that conflict with Prettier.

## Connecting ESLint and Prettier

ESLint and Prettier can be used in the same project, but their responsibilities should remain separate. Some ESLint configurations can contain stylistic rules that disagree with formatting decisions made by Prettier. When that happens, one tool can report code that the other tool intentionally produced.

The `eslint-config-prettier` package disables ESLint rules that are known to conflict with Prettier. Import it into `eslint.config.js` and place it **after** the other ESLint configurations.

```js
import js from "@eslint/js";
import eslintConfigPrettier from "eslint-config-prettier";
export default [
    js.configs.recommended,
    eslintConfigPrettier,
];
```

Configuration order matters because later configuration can override earlier configuration. Placing `eslintConfigPrettier` last allows it to disable conflicting rules introduced by earlier configurations.

This connection does not make ESLint run Prettier. ESLint still performs linting, and Prettier still performs formatting. The configuration simply prevents unnecessary conflicts between their responsibilities.

The project can now be checked with both tools.

```bash
npx eslint .
npx prettier --check .
```

!!! success "Separate Responsibilities"

    A clean setup lets ESLint report code quality problems while Prettier controls formatting. `eslint-config-prettier` helps the two tools coexist by disabling conflicting ESLint formatting rules.

Typing the full `npx` commands is useful while learning what each tool does. Once the tools work together correctly, the next section turns these commands into reusable npm scripts for regular project work.

## Scripts for Linting and Formatting

**npm scripts** were introduced in **Package Management Level 1** as named commands stored in the `scripts` property of `package.json`. They can be used to give the project's linting and formatting tasks predictable names.

Add the following scripts to `package.json`.

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

These script names describe the task rather than the package manager used to run it. The `lint` script checks the project without requesting automatic fixes, while `lint:fix` asks ESLint to apply fixes that its rules can perform safely. The `format` script rewrites supported files according to the Prettier configuration, while `format:check` checks whether files are formatted without modifying them.

The scripts can be run through the package manager used by the project. Different package managers use slightly different command syntax, but the scripts stored in `package.json` remain the same. This keeps the project configuration reusable without tying the workflow to a particular package manager.

!!! info "Checks and Changes"

    Scripts that check files without changing them are useful when a project needs to verify code automatically. Scripts that use `--fix` or `--write` modify files and are useful during development when the developer wants the tool to apply supported corrections.

The package scripts now provide a consistent way to run the project's checks and formatting tasks regardless of the package manager used.

At this point, the project has a basic code quality and formatting workflow. ESLint analyzes JavaScript for configured code quality problems, Prettier applies consistent formatting, `eslint-config-prettier` prevents conflicting formatting rules, package scripts provide reusable project commands, and optional editor integration can automate formatting during everyday development. A later **Code Quality and Formatting Level 2** can extend this foundation with Node-specific linting, including tools such as `eslint-plugin-n` for rules that are specific to Node.js projects.
