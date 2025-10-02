"""Core hello world functionality."""

from typing import Optional


def hello_world(name: Optional[str] = None) -> str:
    """Return a hello world greeting.
    
    Args:
        name: Optional name to include in the greeting.
        
    Returns:
        A greeting string.
        
    Examples:
        >>> hello_world()
        'Hello, World!'
        >>> hello_world("Python")
        'Hello, Python!'
    """
    if name is not None:
        return f"Hello, {name}!"
    return "Hello, World!"


def get_version() -> str:
    """Get the current package version.
    
    Returns:
        The version string.
    """
    from . import __version__
    return __version__