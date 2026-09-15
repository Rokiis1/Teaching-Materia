# Overview

Code quality and formatting help keep source code readable, consistent, and easier to maintain as a project grows. Code can produce the expected result while still being difficult to understand because of unnecessary statements, inconsistent formatting, or patterns that make problems harder to notice. Automated development tools provide a consistent way to check these concerns across a project.

**Linting** and **formatting** address different parts of this process. Linting analyzes source code for potential problems and patterns that do not follow configured rules, while formatting controls how code is visually presented. In JavaScript projects, **ESLint** is commonly used for linting and **Prettier** for automated formatting. Their rules and behavior can be configured for the needs of a project and extended as the project introduces additional environments and technologies.

The **Code Quality and Formatting** module develops from the foundations of automated linting and formatting to more specialized code-quality configurations. It establishes the separate responsibilities of ESLint and Prettier, how these tools become part of a project workflow, and how their rules and capabilities can be explored and extended as project requirements grow.

**Level 1** introduces the foundations of **linting and formatting** with ESLint and Prettier. It develops a basic project workflow for installing and configuring both tools, checking JavaScript for code-quality problems, applying consistent formatting, preventing conflicts between linting and formatting responsibilities, and creating reusable project commands. It also introduces optional editor integration and the official documentation used to explore additional rules, options, and plugins.

Later levels can build on this foundation by introducing more specialized linting requirements and plugins for particular JavaScript environments. This allows the code-quality configuration to develop alongside the project rather than introducing rules and tools before they are needed.

Together, these concepts provide a foundation for maintaining consistent JavaScript projects with automated development tools. They establish why linting and formatting are separate concerns, how ESLint and Prettier fit into the development workflow, and how that workflow can be extended as a project's code-quality requirements become more advanced.
