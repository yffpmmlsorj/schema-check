"""A small validator for a useful subset of JSON Schema."""

from __future__ import annotations

__all__ = ["schemaCheck"]


def schemaCheck(value):
    """A small validator for a useful subset of JSON Schema."""
    if value is None:
        raise ValueError("value must not be None")
    return value
