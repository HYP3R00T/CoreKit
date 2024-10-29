# Contributing to UtilityHub

We’re excited that you want to contribute to **UtilityHub**! Whether it’s a bug fix, new feature, or improvement, your contributions help make this project better.

## How to Contribute

### 1. Fork the Repository

Start by forking the repository on GitHub. This will create a personal copy of the project under your GitHub account where you can make changes.

### 2. Clone Your Fork

Clone your fork to your local machine:

```bash
git clone https://github.com/your-username/UtilityHub.git
```

### 3. Set Up Your Environment

Navigate to the project directory and install dependencies using Poetry:

```bash
cd UtilityHub
poetry install
pre-commit install
```

### 4. Make Your Changes

Create a new branch for your changes:

```bash
git checkout -b your-branch-name
```

Make your changes and commit them with a clear message:

```bash
git add .
git commit -m "feat: add dark mode toggle"
```

#### **Commit Message Structure**

```txt
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

- **`<type>`**: Specifies the type of change. Common types include:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation only changes
  - `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
  - `refactor`: A code change that neither fixes a bug nor adds a feature
  - `perf`: A code change that improves performance
  - `test`: Adding missing tests or correcting existing tests
  - `build`: Changes that affect the build system or external dependencies
  - `ci`: Changes to our CI configuration files and scripts
  - `chore`: Other changes that don't modify src or test files

- `[optional scope]`: A scope may be provided to indicate what part of the codebase the commit affects (e.g., `ui`, `api`, etc.).

- `<description>`: A short description of the change, written in the imperative mood (e.g., "add" instead of "added" or "adding").

- `[optional body]`: A more detailed explanation of the change, which can include the reasoning behind the change or its implications.

- `[optional footer]`: Used for breaking changes and issues being fixed. For example:
- `BREAKING CHANGE: <description>`
- `Closes #123`

### 5. Run Tests

Before submitting a pull request, ensure that all tests pass:

```bash
poetry run pytest
```

### 6. Lint Your Code

Ensure your code adheres to the project’s style guidelines by running:

```bash
poetry run ruff check .
```

### 7. Push Your Changes

Push your changes to your fork:

```bash
git push origin your-branch-name
```

### 8. Create a Pull Request

Go to the repository on GitHub and create a pull request from your branch. Provide a detailed description of your changes and why they’re needed.

## Questions?

If you have any questions or need further clarification, feel free to open an issue on GitHub or contact me at [rajesh@hyperoot.dev](mailto:rajesh@hyperoot.dev).

Thank you for contributing to **UtilityHub**!
