# Level 1

## Table of Contents: Package Management

- [Creating a Package and the package.json File](#creating-a-package-and-the-packagejson-file)
- [Packages, Dependencies, and Package Managers](#packages-dependencies-and-package-managers)
- [npm and the npm Registry](#npm-and-the-npm-registry)
- [Installing Packages](#installing-packages)
- [Semantic Versioning (SemVer)](#semantic-versioning-semver)
- [dependencies and devDependencies](#dependencies-and-devdependencies)
- [`node_modules` and package-lock.json](#node_modules-and-package-lockjson)
- [Viewing, Updating, and Removing Packages](#viewing-updating-and-removing-packages)
- [npm Scripts](#npm-scripts)
- [Running Package Commands with npx](#running-package-commands-with-npx)
- [Global Packages](#global-packages)

**Package Management Level 1** introduces the foundations of managing packages in Node.js projects with **npm**. We begin by creating a `package.json` file, then explain packages, dependencies, npm, and the npm registry so that the information recorded in a project has a clear purpose. From there, we install a small package and examine how npm records it, how package versions work, and why dependencies are separated into different categories. The level then explains `node_modules` and `package-lock.json`, common package maintenance commands, npm scripts, and the difference between local and global package installation.

## Creating a Package and the package.json File

When a Node.js project begins to use external packages, it needs a consistent place to record information about the project and the packages it requires. npm uses a file named `package.json` for this purpose. The file can describe the project and later record its dependencies and scripts, allowing npm and other developers to understand important parts of the project's package configuration.

The `npm init` command creates this file in the current project folder. Running the command without additional options starts an interactive process in which npm asks for information such as the package name and version.

```bash
npm init
```

For a simple learning project, the questions can be skipped with the `-y` option. npm then creates `package.json` using default values that can be edited later when necessary.

```bash
npm init -y
```

A newly created file may contain information similar to the following example.

```json
{
  "name": "example-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

The `name` property identifies the package and `version` stores its current version. Other properties can describe the project or configure npm behavior. The exact contents can vary according to the npm version and the choices made during initialization.

!!! warning "Valid JSON syntax"

    `package.json` must contain valid JSON. Property names and string values use double quotation marks, and trailing commas are not allowed. Invalid JSON can prevent npm from reading the file correctly.

Creating `package.json` does not install any external packages by itself. It establishes the project metadata that npm can later update when dependencies are added or removed. To understand what npm will record in this file, we first need to distinguish packages, dependencies, and package managers.

## Packages, Dependencies, and Package Managers

Modern applications often use code and development tools created outside the project itself. A project might use an existing package to format output, validate data, test code, or provide functionality that would otherwise need to be written from the beginning. Reusing suitable packages can reduce duplicated work and allows a project to build on existing functionality.

A **package** is a collection of files that provides reusable code or tooling together with metadata that describes the package. When a project requires another package in order to run or support its development process, that package becomes a **dependency** of the project. A dependency can also have dependencies of its own, which means one direct installation can result in several related packages being installed.

A **package manager** is a tool that manages these packages and dependency relationships. Instead of manually downloading package files and copying them into a project, a package manager can install, update, remove, and keep track of the packages the project requires.

```text
application/
├── package.json
├── package-lock.json
├── node_modules/
└── index.js
```

In a project managed by npm, `package.json` records declared package information, `package-lock.json` records the resolved dependency installation, and `node_modules` contains installed packages. We will examine each of these parts as they become relevant rather than treating them as separate files without context.

With the basic relationship between packages, dependencies, and package managers established, we can now focus on **npm**, the package manager used throughout this **Package Management Level 1**.

## npm and the npm Registry

**npm** is the package manager commonly distributed with Node.js. Its command line tool, also named `npm`, can create package metadata, install dependencies, run project scripts, and perform other package management tasks. The installed npm version can be checked with `npm --version`.

Packages installed through npm are commonly retrieved from the **npm registry**, an online collection of published packages. The npm command line tool and the registry therefore have different roles. npm performs package management operations on the local computer, while the registry provides published packages that npm can retrieve.

Packages in the public npm registry can be searched and explored through the **npm website** at [npmjs.com](https://www.npmjs.com/). A package page provides information such as its description, available version, installation command, documentation, dependencies, and other package metadata. This makes the website a useful place to find packages and learn what they provide before installing them.

Before installing a package, it is useful to know what problem the package solves and whether the project actually needs it. Once a suitable package has been chosen, npm can install it into the project and record the dependency.

## Installing Packages

A package can be installed into the current project with `npm install` followed by its package name. For a small first example, we can install `is-odd`, a package with a simple purpose that makes the result of the installation easy to understand.

```bash
npm install is-odd
```

This is a **local installation**. npm installs the package for the current project and records it under `dependencies` in `package.json`. Part of the file will then contain an entry similar to the following example.

```json
{
  "dependencies": {
    "is-odd": "^3.0.1"
  }
}
```

The exact version recorded depends on the version npm resolves when the command is run. At this point, the important result is not how the package is imported into JavaScript code, which belongs to the modules material. The important result is that npm has installed an external package and recorded the dependency relationship in the project.

Several packages can also be named in one installation command. When an existing project already contains dependency information in `package.json`, running `npm install` without a package name installs the dependencies declared by that project.

``` bash
npm install is-odd is-even # Install multiple named packages
npm install # Install the dependencies declared by the project
```

Installing a package records a version or version range in the project's package configuration. Understanding how these versions are written and interpreted is therefore the next part of managing dependencies.

## Semantic Versioning (SemVer)

Packages commonly use **semantic versioning**, usually called **SemVer**, to communicate the kind of change represented by a version number. A semantic version has three main numeric parts written as `MAJOR.MINOR.PATCH`. For example, version `3.5.2` has major version `3`, minor version `5`, and patch version `2`.

When a particular package version is required, npm allows that version to be specified after the package name with `@`.

```bash
npm install is-odd@3.0.1
```

The **MAJOR** number changes when a release introduces incompatible changes that may require existing code to be updated. The **MINOR** number changes when compatible functionality is added, while the **PATCH** number changes for compatible fixes. If version `2.4.1` receives a compatible bug fix, a later version might be `2.4.2`. A compatible feature could produce `2.5.0`, while an incompatible change could produce `3.0.0`.

`package.json` can specify a **version range** instead of requiring one exact version. Two common range prefixes are the caret `^` and the tilde `~`.

```json
{
  "dependencies": {
    "package-a": "^2.4.1",
    "package-b": "~2.4.1",
    "package-c": "2.4.1"
  }
}
```

For ordinary versions at or above `1.0.0`, `^2.4.1` permits compatible updates below `3.0.0`, while `~2.4.1` permits patch updates below `2.5.0`. Writing `2.4.1` without a range prefix requests that exact version.

!!! warning "Version zero requires extra care"

    Version ranges behave more narrowly for `0.x.x` releases because semantic versioning treats major version zero as initial development. For example, `^0.2.3` allows versions from `0.2.3` up to, but not including, `0.3.0`. In this case, the caret keeps the minor version fixed while allowing compatible patch updates.

Version ranges describe which package releases a project can accept, but package configuration also distinguishes why a dependency is needed. The next section separates packages required by the application from packages used only while developing it.

## dependencies and devDependencies

npm commonly records installed packages under either `dependencies` or `devDependencies` in `package.json`. **Dependencies** are packages required for the application's normal runtime behavior, while **development dependencies** are packages used to develop, test, format, or otherwise work on the project without being required by the running application itself.

A regular installation records a package under `dependencies`, while the `--save-dev` option, which can also be written as `-D`, records it under `devDependencies`.

```bash
npm install is-odd # Record a runtime dependency
npm install --save-dev eslint # Record a development dependency
```

The corresponding parts of `package.json` can appear together.

```json
{
  "dependencies": {
    "is-odd": "^3.0.1"
  },
  "devDependencies": {
    "is-even": "^9.0.0"
  }
}
```

The versions in this example are illustrative. The actual versions depend on what npm resolves when the packages are installed.

!!! example "Choosing a dependency category"

    If application code requires a package while the application is running, that package normally belongs in `dependencies`. If a package is used only by development tooling, such as a linter or test runner, it normally belongs in `devDependencies`.

Both categories describe declared dependencies, but npm must also store the installed package files and record the versions it actually resolved. This leads to the roles of `node_modules` and `package-lock.json`.

## `node_modules` and package-lock.json

A local installation normally creates a `node_modules` directory. This directory contains packages installed for the project together with packages required by those dependencies. Because dependency trees can contain many packages, `node_modules` can become much larger than the small set of dependencies written directly in `package.json`.

The `package-lock.json` file serves a different purpose. While `package.json` can contain version ranges describing acceptable releases, `package-lock.json` records the concrete dependency resolution produced by npm, including the specific package versions selected for the installation. npm creates and updates this file automatically during relevant package operations.

``` text
example-project/
├── node_modules/
├── package.json
├── package-lock.json
└── index.js
```

For most projects, `node_modules` is generated rather than committed to version control. The project keeps `package.json` and normally keeps `package-lock.json`, allowing the dependency installation to be recreated without storing the entire installed directory.

!!! note "Keep the lockfile"

    Application projects should normally commit `package-lock.json` to version control. The lockfile helps developers and automated environments work from the same resolved dependency information and should normally be updated through npm rather than edited manually.

Once dependencies are installed and their project files are understood, the next task is maintaining them. npm provides commands for inspecting installed packages, checking for updates, updating them, and removing packages that are no longer required.

## Viewing, Updating, and Removing Packages

npm can inspect package information before a package is installed. The `npm view` command reads metadata published for a package in the registry, making it useful for checking details such as the current version, repository URL, or the dependencies declared by a particular release.

```bash
npm view is-odd # View published package metadata
npm view is-odd version # View the current version
npm view is-odd repository.url # View the repository URL
npm view is-odd@3.0.1 dependencies # View dependencies for a specific version
```

For packages that are already installed, `npm list` displays the local dependency tree. Adding `--depth=0` limits the output to the project's top level packages, while a package name can be supplied when only one installed package needs to be inspected.

```bash
npm list # Display the local dependency tree
npm list --depth=0 # Display top level installed packages
npm list is-odd # Inspect one installed package
```

The `npm outdated` command checks whether newer versions are available. Running `npm update` without a package name updates installed dependencies within the version ranges allowed by the project, while naming a package limits the operation to that dependency. When the goal is to request the version currently published under the `latest` tag rather than remain within the existing declared range, the package can be installed with `@latest`.

```bash
npm outdated # Check for available updates
npm update # Update dependencies within allowed ranges
npm update is-odd # Update one package within its allowed range
npm install is-odd@latest # Request the version published under the latest tag
npm uninstall is-odd # Remove the package from the project
```

These operations can update `package.json` and `package-lock.json` when the project's declared or resolved dependencies change.

!!! warning "Test after dependency updates"

    Even when an update is expected to be compatible, run the project's relevant tests and checks after changing dependencies. Package updates can affect behavior, tooling, or interactions with other dependencies.

Package maintenance manages what the project has installed, while npm scripts provide a consistent way to define and run commands used by the project.

## npm Scripts

The `scripts` property in `package.json` defines named commands for common project tasks. These commands are called **npm scripts** and provide a consistent way to run project commands, such as starting the application, running tests, or formatting code.

```json
{
  "scripts": {
    "start": "node index.js",
    "test": "node test.js",
    "format": "prettier --write ."
  }
}
```

Scripts are generally executed with `npm run` followed by the script name. Some commonly used script names, including `start` and `test`, can also be executed using shorter commands.

```bash
npm run format # Run the format script
npm start # Run the start script
npm test # Run the test script
```

Keeping these commands in `package.json` gives common project tasks consistent names and makes them available to anyone working with the project. Sometimes, however, a package provides a command that needs to be run directly without first defining an npm script. The next section introduces `npx` for this purpose.

## Running Package Commands with npx

**`npx`** runs commands provided by npm packages. It is useful when a package exposes a command-line tool and you want to execute that tool without installing it globally.

When the required package is already installed in the current project, `npx` can run its executable from the project's local dependencies. For example, if ESLint has been installed as a development dependency, its command can be run with `npx eslint`.

```bash
npm install --save-dev eslint # Install ESLint in the project
npx eslint . # Run the locally installed ESLint command
```

Using the project's local version keeps the tool associated with the project and avoids depending on a separate global installation. This also makes it easier for different developers working on the project to use the version declared in `package.json`.

`npx` can also execute a package command when the package is not already installed locally. In that situation, npm can obtain the required package for the command without adding it to the project's dependencies.

```bash
npx cowsay "Hello from npx"
```

!!! info "npx and global installation"

    `npx` is useful for running package commands without requiring a permanent global installation. A global installation can still be appropriate when a command-line tool is intentionally meant to be available across projects and its documentation recommends that workflow.

`npx` therefore provides another way to work with package command-line tools without treating them as global dependencies. The next section explains when global package installation is appropriate.

## Global Packages

A package installed **globally** is managed outside a single project's local dependency set. The `--global` option, which can also be written as `-g`, is used for this form of installation.

```bash
npm install --global package-name # Install a package globally
npm list --global --depth=0 # View top level global packages
npm uninstall --global package-name # Remove a global package
```

Global installation is mainly useful for command line tools that are intentionally meant to be available across projects and whose documentation recommends that workflow. A package required by a particular project's code should generally be installed locally and recorded in that project's `package.json`, because another developer installing the project dependencies will not automatically receive packages that exist only in your global installation.

!!! warning "Do not replace project dependencies with global packages"

    If a project requires a package, declare it in the project rather than relying on a global installation. This keeps the project's requirements visible and reproducible for other developers and environments.

Understanding the difference between local and global packages completes the basic npm workflow. **Package Management Level 2** builds on these foundations by examining why alternative package managers exist and introducing **pnpm**, including its basic commands and the different approach it uses to store and resolve project dependencies.
