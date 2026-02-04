"""Void UI color tokens.

All colors match the CSS custom properties from @void-ui/css.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    """Base color scheme interface."""

    # Surfaces
    void: str
    surface: str
    raised: str
    elevated: str

    # Warm pastels
    peach: str
    blush: str
    sand: str
    moss: str
    lilac: str
    clay: str

    # Semantic
    accent: str
    accent_hover: str
    accent_bg: str
    success: str
    success_bg: str
    warning: str
    warning_bg: str
    danger: str
    danger_bg: str
    info: str
    info_bg: str

    # Text
    white: str
    gray: str
    muted: str
    faint: str

    # Borders
    border: str
    border_light: str

    # Glass
    glass_bg: str
    glass_border: str


# Dark theme (default)
DarkColors = Colors(
    # Surfaces
    void="#0f0d0b",
    surface="#171412",
    raised="#1f1b18",
    elevated="#2a2521",

    # Warm pastels
    peach="#e8a87c",
    blush="#d4a5a5",
    sand="#c9b896",
    moss="#a5b5a0",
    lilac="#b8a9c9",
    clay="#c17c60",

    # Semantic
    accent="#e8a87c",
    accent_hover="#d4965e",
    accent_bg="rgba(232, 168, 124, 0.12)",
    success="#a5b5a0",
    success_bg="rgba(165, 181, 160, 0.12)",
    warning="#c9b896",
    warning_bg="rgba(201, 184, 150, 0.12)",
    danger="#c9544e",
    danger_bg="rgba(201, 84, 78, 0.12)",
    info="#b8a9c9",
    info_bg="rgba(184, 169, 201, 0.12)",

    # Text
    white="#f5f0eb",
    gray="#9a918a",
    muted="#4a4540",
    faint="#2a2622",

    # Borders
    border="#252220",
    border_light="#1f1b18",

    # Glass
    glass_bg="rgba(23, 20, 18, 0.72)",
    glass_border="rgba(232, 168, 124, 0.08)",
)


# Light theme
LightColors = Colors(
    # Surfaces
    void="#faf8f5",
    surface="#f5f2ee",
    raised="#ede9e4",
    elevated="#ffffff",

    # Warm pastels (same as dark)
    peach="#e8a87c",
    blush="#d4a5a5",
    sand="#c9b896",
    moss="#a5b5a0",
    lilac="#b8a9c9",
    clay="#c17c60",

    # Semantic
    accent="#e8a87c",
    accent_hover="#c08058",
    accent_bg="rgba(232, 168, 124, 0.12)",
    success="#a5b5a0",
    success_bg="rgba(165, 181, 160, 0.12)",
    warning="#c9b896",
    warning_bg="rgba(201, 184, 150, 0.12)",
    danger="#c9544e",
    danger_bg="rgba(201, 84, 78, 0.12)",
    info="#b8a9c9",
    info_bg="rgba(184, 169, 201, 0.12)",

    # Text
    white="#1a1816",
    gray="#6e6660",
    muted="#b5ada6",
    faint="#e8e2dc",

    # Borders
    border="#e0dbd5",
    border_light="#ebe6e0",

    # Glass
    glass_bg="rgba(250, 248, 245, 0.72)",
    glass_border="rgba(0, 0, 0, 0.06)",
)


@dataclass(frozen=True)
class Spacing:
    xs: int = 4
    sm: int = 8
    md: int = 16
    lg: int = 24
    xl: int = 32
    xxl: int = 48
    xxxl: int = 64


@dataclass(frozen=True)
class Radius:
    sm: int = 4
    md: int = 6
    lg: int = 8
    xl: int = 12
    full: int = 9999


@dataclass(frozen=True)
class Typography:
    font_family: str = (
        "Inter, -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif"
    )
    font_mono: str = "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace"
    font_jp: str = "'Noto Sans JP', sans-serif"
    font_tech: str = "'Orbitron', sans-serif"

    size_xs: int = 11
    size_sm: int = 12
    size_base: int = 13
    size_md: int = 14
    size_lg: int = 16
    size_xl: int = 18
    size_2xl: int = 22
    size_3xl: int = 28


SPACING = Spacing()
RADIUS = Radius()
TYPOGRAPHY = Typography()
