"""Void UI for PySide6.

Cryptic tech aesthetic. Warm void, soft pastels, Japanese and tech vibes.
"""

__version__ = "0.1.0"

from void_ui.theme import Theme, apply_theme
from void_ui.colors import Colors, DarkColors, LightColors
from void_ui.widgets import (
    VoidButton,
    VoidCard,
    VoidInput,
    VoidLabel,
    VoidBadge,
    VoidProgress,
)

__all__ = [
    "Theme",
    "apply_theme",
    "Colors",
    "DarkColors",
    "LightColors",
    "VoidButton",
    "VoidCard",
    "VoidInput",
    "VoidLabel",
    "VoidBadge",
    "VoidProgress",
]
