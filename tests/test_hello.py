"""Tests for hello world functionality."""

import pytest

from super_octo_bassoon.hello import hello_world, get_version


class TestHelloWorld:
    """Test cases for hello_world function."""

    def test_hello_world_without_name(self) -> None:
        """Test hello_world with no name parameter."""
        result = hello_world()
        assert result == "Hello, World!"

    def test_hello_world_with_name(self) -> None:
        """Test hello_world with name parameter."""
        result = hello_world("Python")
        assert result == "Hello, Python!"

    def test_hello_world_with_empty_string(self) -> None:
        """Test hello_world with empty string."""
        result = hello_world("")
        assert result == "Hello, !"

    def test_hello_world_with_none(self) -> None:
        """Test hello_world with None explicitly."""
        result = hello_world(None)
        assert result == "Hello, World!"

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Alice", "Hello, Alice!"),
            ("Bob", "Hello, Bob!"),
            ("World", "Hello, World!"),
            ("123", "Hello, 123!"),
        ],
    )
    def test_hello_world_parametrized(self, name: str, expected: str) -> None:
        """Test hello_world with various names."""
        result = hello_world(name)
        assert result == expected


class TestGetVersion:
    """Test cases for get_version function."""

    def test_get_version_returns_string(self) -> None:
        """Test that get_version returns a string."""
        version = get_version()
        assert isinstance(version, str)
        assert len(version) > 0

    def test_get_version_format(self) -> None:
        """Test that version follows semantic versioning format."""
        import re

        version = get_version()
        # Regex for semantic versioning: major.minor.patch(-prerelease)?(+build)?
        semver_regex = r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z-.]+)?(?:\+[0-9A-Za-z-.]+)?$"
        assert re.match(semver_regex, version), f"Version '{version}' does not match semantic versioning"