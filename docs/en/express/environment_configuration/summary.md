# Summary

This summary brings together the most important concepts from the **Environment and Configuration** module. It provides a quick reference for reviewing how an Express application selects a runtime environment, loads environment-specific configuration, centralizes configuration access, validates values before startup, and protects secrets.

## Table of Contents: Environment and Configuration

- [Level 1](#level-1)

## Level 1

Level 1 establishes the foundations of **runtime environments, environment-specific configuration, centralized configuration access, configuration validation, and secret protection**. The main goal is to understand how an Express application can move from directly reading environment variables to using a consistent configuration path from application startup to server execution.

Applications commonly run in different environments such as `development`, `test`, `staging`, and `production`. This project uses `NODE_ENV` to identify the current environment and keeps separate environment files so each environment can provide its own values.

```text
project/
├── app/
│   ├── app.js
│   └── config.js
├── .env.development
├── .env.test
├── .env.staging
├── .env.production
├── .env.example
├── .gitignore
└── package.json
```

In this configuration design, `NODE_ENV` is supplied before the application starts. The application reads that value and dotenv loads the matching `.env.${environment}` file.

```js
import dotenv from "dotenv";

const environment = process.env.NODE_ENV || "development";

dotenv.config({
  path: `.env.${environment}`,
});
```

Project scripts use `cross-env` to supply `NODE_ENV` consistently across operating systems. Each script identifies the runtime environment while the application remains responsible for selecting and loading the corresponding environment file.

```json
{
  "scripts": {
    "dev": "cross-env NODE_ENV=development node --watch app/app.js",
    "test": "cross-env NODE_ENV=test node app/app.js",
    "staging": "cross-env NODE_ENV=staging node app/app.js",
    "start": "cross-env NODE_ENV=production node app/app.js"
  }
}
```

!!! note "Environment Selection"

    `cross-env` supplies `NODE_ENV`, the application reads that value, and dotenv uses it to select the matching environment file. Node.js's `--env-file` option can also load a selected file directly, but that represents a different design in which the startup command chooses the file.

As configuration grows, reading `process.env` throughout the application can spread loading, conversion, defaults, and other configuration logic across multiple modules. A central `config.js` module keeps these responsibilities in one place and exports ordinary configuration properties for the rest of the application.

```js
import dotenv from "dotenv";

const environment = process.env.NODE_ENV || "development";

dotenv.config({
  path: `.env.${environment}`,
});

const config = {
  environment,
  port: Number(process.env.PORT) || 3000,
  baseUrl: process.env.BASE_URL,
};

export default config;
```

The main application can import the configuration object instead of reading environment variables directly.

``` js
import express from "express";
import config from "./config.js";

const app = express();

app.listen(config.port, () => {
  console.log(`Server is running on port ${config.port}`);
  console.log(`Environment: ${config.environment}`);
  console.log(`Base URL: ${config.baseUrl}`);
});
```

Configuration should also be validated before the server starts. Some values can have appropriate defaults, while required values should cause startup to stop when they are missing. Converted values should also be checked before they are used.

```js
function required(name) {
  const value = process.env[name];

  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }

  return value;
}

const port = Number(process.env.PORT || 3000);

if (Number.isNaN(port)) {
  throw new Error("PORT must be a number");
}
```

Because the configuration module is imported before `app.listen()` runs, invalid configuration can stop the application before the Express server begins accepting requests.

!!! danger "Validate Configuration and Protect Secrets"

    Required configuration should be validated during startup. Secrets such as database passwords, API keys, signing secrets, and service credentials should remain outside source code and should not receive hardcoded fallback credentials. Private environment files should remain outside version control, while `.env.example` can document expected variable names without containing real secret values.

!!! abstract "Environment and Configuration Flow"

    **A project script supplies `NODE_ENV`, the application uses it to select an environment-specific file, dotenv loads the file into `process.env`, the configuration module converts and validates the values, and the Express application imports the resulting configuration before starting the server.**

After reviewing Level 1, you should be able to explain **how runtime environments and environment-specific configuration work together**, describe the role of **`NODE_ENV`**, use **dotenv** to load the matching environment file, explain why project scripts use **cross-env** in this configuration design, distinguish this approach from Node.js's **`--env-file`** option, centralize environment access in a **configuration module**, convert and validate configuration values before startup, explain when **fallback values** are appropriate, and describe how **secrets and private environment files** should be protected.
