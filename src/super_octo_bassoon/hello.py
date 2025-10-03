"""Greeting and utility helpers.

This module contains small, pure (or near‑pure) helper functions that back the
library's public surface and CLI. The intent is to keep logic here free of any
CLI / I/O side effects so functions remain easy to test.

Available functions
-------------------
hello_world(name)
    Return a canonical greeting. Passing ``None`` triggers the special
    fallback to ``"Hello, World!"`` while an empty string is preserved
    verbatim (``"Hello, !"``) — this subtle distinction is relied upon by the
    test-suite; do not change without updating tests and documenting as a
    breaking change.

get_version()
    Return the package version string sourced from the top‑level package.

get_today_date()
    Convenience wrapper returning today's date as an ISO (YYYY-MM-DD) string.

Design notes
------------
* Keep functions single-purpose and fully type annotated (mypy strict).
* Preserve existing return string formats; downstream consumers and tests may
  rely on them.
* Avoid adding external dependencies here—standard library only.
"""

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
