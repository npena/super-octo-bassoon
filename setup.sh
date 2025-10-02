#!/bin/bash

# Super Octo Bassoon - Project Setup Script
# This script sets up the development environment

set -e

echo "🚀 Setting up Super Octo Bassoon development environment..."

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed. Please install Poetry first:"
    echo "   curl -sSL https://install.python-poetry.org | python3 -"
    echo "   or visit: https://python-poetry.org/docs/#installation"
    exit 1
fi

echo "✅ Poetry found: $(poetry --version)"

# Enforce Poetry >= 2.0.0
POETRY_VERSION_RAW=$(poetry --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
POETRY_MAJOR=${POETRY_VERSION_RAW%%.*}
if [ "${POETRY_MAJOR}" -lt 2 ]; then
    echo "❌ Detected Poetry ${POETRY_VERSION_RAW}. This project now requires Poetry >= 2.0.0." >&2
    echo "   Please upgrade: curl -sSL https://install.python-poetry.org | python3 -" >&2
    exit 1
fi

echo "✅ Poetry version constraint satisfied (>=2.0.0)"

# Install dependencies
echo "📦 Installing dependencies..."
poetry install

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
poetry run pre-commit install

# Run initial quality checks
echo "🧪 Running initial quality checks..."
poetry run black src tests
poetry run isort src tests
poetry run flake8 src tests
poetry run mypy src

# Run tests
echo "🧪 Running tests..."
poetry run pytest

echo "✅ Setup complete! You can now:"
echo "   - Run 'poetry shell' to activate the virtual environment"
echo "   - Run 'hello' to test the CLI"
echo "   - Run 'make help' to see available commands"
echo "   - Start developing! 🎉"