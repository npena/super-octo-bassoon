# Super Octo Bassoon

[![CI/CD Pipeline](https://github.com/npena/super-octo-bassoon/workflows/CI/CD%20Pipeline/badge.svg)](https://github.com/npena/super-octo-bassoon/actions)
[![codecov](https://codecov.io/gh/npena/super-octo-bassoon/branch/main/graph/badge.svg)](https://codecov.io/gh/npena/super-octo-bassoon)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![Poetry](https://img.shields.io/badge/poetry-managed-blue.svg)](https://python-poetry.org/)


A hello world Python project demonstrating best practices with Poetry package management, comprehensive testing, and automated CI/CD workflows.

## Features

- 🐍 **Modern Python**: Supports Python 3.9+
- 📦 **Poetry**: Dependency management and packaging
- 🧪 **Testing**: Comprehensive test suite with pytest
- 🔍 **Code Quality**: Black, isort, flake8, and mypy
- 🚀 **CI/CD**: GitHub Actions for testing, building, and publishing
- 📝 **Documentation**: Well-documented codebase
- 🎯 **CLI**: Command-line interface with Click

## Quick Start

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/docs/#installation) >= 2.0.0 installed (project assumes v2 semantics)

### Installation

#### From PyPI (when published)

```bash
pip install super-octo-bassoon
```

#### From Source

```bash
git clone https://github.com/npena/super-octo-bassoon.git
cd super-octo-bassoon
poetry install
```

### Usage

#### Command Line Interface

```bash
# Basic hello world
hello

# Hello with a name
hello --name "Python"
hello -n "World"

# Show version
hello --version
hello -v
```

#### Python API

```python
from super_octo_bassoon import hello_world

# Basic usage
greeting = hello_world()
print(greeting)  # "Hello, World!"

# With a name
greeting = hello_world("Python")
print(greeting)  # "Hello, Python!"
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/npena/super-octo-bassoon.git
cd super-octo-bassoon

# Install dependencies (Poetry 2)
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

### Available Commands

```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src --cov-report=html

# Code formatting
poetry run black src tests
poetry run isort src tests

# Linting
poetry run flake8 src tests

# Type checking
poetry run mypy src

# Run all quality checks
poetry run pre-commit run --all-files
```

### Docker Usage

You can build and run the application using the provided multi-stage `Dockerfile`.

```bash
# Build the image
docker build -t super-octo-bassoon .

# Run the CLI (defaults to hello world)
docker run --rm super-octo-bassoon

# Pass a name
docker run --rm super-octo-bassoon --name Python

# Show version
docker run --rm super-octo-bassoon --version
```

The runtime image uses a non-root user and contains only runtime dependencies for a smaller, more secure footprint.

### Dev Container (VS Code / GitHub Codespaces)

A `.devcontainer` configuration is included for a ready-to-code environment with all development dependencies installed via Poetry.

Steps:
1. Open the repository in VS Code.
2. Install the Dev Containers extension if prompted.
3. Reopen in Container when prompted (or use: Command Palette -> Dev Containers: Reopen in Container).
4. After build, dependencies are installed automatically (`poetry install --with dev`).

Inside the dev container you can run:
```bash
poetry run pytest
make quality
hello --name DevContainer
```

Caching: pip and Poetry caches are persisted across rebuilds using mounted cache volumes.

### Project Structure

```
super-octo-bassoon/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline
├── src/
│   └── super_octo_bassoon/
│       ├── __init__.py        # Package initialization
│       ├── hello.py           # Core functionality
│       └── cli.py             # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_hello.py          # Core functionality tests
│   └── test_cli.py            # CLI tests
├── .gitignore
├── .pre-commit-config.yaml    # Pre-commit hooks
├── LICENSE                    # MIT License
├── README.md                  # This file
└── pyproject.toml            # Project configuration
```

## Testing

The project includes comprehensive tests covering:

- ✅ Core functionality
- ✅ CLI interface
- ✅ Edge cases and error handling
- ✅ Type hints and documentation

Run tests with:

```bash
poetry run pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks (`poetry run pre-commit run --all-files`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Release Process

This project uses automated releases via GitHub Actions:

1. **Development**: Work on feature branches and merge to `main` via PR
2. **Versioning**: Update version in `pyproject.toml` and create a git tag
3. **Release**: Push the tag to trigger automatic building and publishing

### Creating a Release

```bash
# Update version in pyproject.toml
poetry version patch  # or minor, major

# Commit the version bump
git add pyproject.toml
git commit -m "Bump version to $(poetry version -s)"

# Create and push tag
git tag "v$(poetry version -s)"
git push origin main --tags
```

## CI/CD Pipeline

The project includes a comprehensive CI/CD pipeline that:

- **Testing**: Runs tests across multiple Python versions (3.9-3.12)
- **Quality**: Enforces code quality with linting and formatting checks
- **Building**: Creates distribution packages
- **Publishing**: Automatically publishes to PyPI on tagged releases
- **Releases**: Creates GitHub releases with artifacts

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Poetry](https://python-poetry.org/) for dependency management
- CLI powered by [Click](https://click.palletsprojects.com/)
- Testing with [pytest](https://pytest.org/)
- Code quality tools: [Black](https://black.readthedocs.io/), [isort](https://pycqa.github.io/isort/), [flake8](https://flake8.pycqa.org/), [mypy](https://mypy.readthedocs.io/)
