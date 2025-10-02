"""Tests for CLI functionality."""

from click.testing import CliRunner

from super_octo_bassoon.cli import main


class TestCLI:
    """Test cases for CLI functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_without_arguments(self) -> None:
        """Test CLI with no arguments."""
        result = self.runner.invoke(main)
        assert result.exit_code == 0
        assert "Hello, World!" in result.output

    def test_cli_with_name_option(self) -> None:
        """Test CLI with --name option."""
        result = self.runner.invoke(main, ["--name", "Python"])
        assert result.exit_code == 0
        assert "Hello, Python!" in result.output

    def test_cli_with_name_short_option(self) -> None:
        """Test CLI with -n short option."""
        result = self.runner.invoke(main, ["-n", "Test"])
        assert result.exit_code == 0
        assert "Hello, Test!" in result.output

    def test_cli_version_flag(self) -> None:
        """Test CLI with --version flag."""
        result = self.runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "super-octo-bassoon version" in result.output

    def test_cli_version_short_flag(self) -> None:
        """Test CLI with -v short flag."""
        result = self.runner.invoke(main, ["-v"])
        assert result.exit_code == 0
        assert "super-octo-bassoon version" in result.output