"""Uyghur text reshaper: basic Arabic block ⇄ Arabic Presentation Forms."""

from .shaper import UighurReshaper, main

# Backward-compatible aliases.
reshaper = UighurReshaper
uighur_reshaper = UighurReshaper

__all__ = ["UighurReshaper", "reshaper", "uighur_reshaper", "main"]
__version__ = "0.2.0"
