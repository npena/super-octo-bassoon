"""Core hello world functionality."""

from datetime import date
from random import randint, sample
from typing import List, Optional, Tuple


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


def get_today_date() -> str:
    """Return today's date as an ISO string (YYYY-MM-DD).

    Returns:
        The current date in ISO format.
    """
    return date.today().isoformat()


def get_lottery_numbers() -> Tuple[List[int], int]:
    """Return 5 unique random numbers from 1 to 70 and an additional random
    number from 1 to 24.

    Returns:
        A tuple containing a list of 5 sorted unique numbers (1-70) and a
        single number (1-24).

    Examples:
        >>> nums, extra = get_lottery_numbers()
        >>> len(nums)
        5
        >>> all(1 <= n <= 70 for n in nums)
        True
        >>> 1 <= extra <= 24
        True
    """
    numbers = sorted(sample(range(1, 71), 5))
    extra = randint(1, 24)
    return numbers, extra
