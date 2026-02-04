"""Void UI styled widgets.

Pre-styled PySide6 widgets matching the design system.
"""

from __future__ import annotations

from typing import Optional

try:
    from PySide6.QtWidgets import (
        QPushButton,
        QLabel,
        QLineEdit,
        QFrame,
        QVBoxLayout,
        QWidget,
        QProgressBar,
        QGraphicsDropShadowEffect,
    )
    from PySide6.QtCore import Qt, Signal
    from PySide6.QtGui import QColor
    HAS_PYSIDE = True
except ImportError:
    HAS_PYSIDE = False
    QPushButton = object
    QLabel = object
    QLineEdit = object
    QFrame = object
    QProgressBar = object

from void_ui.colors import DarkColors, RADIUS, SPACING


class VoidButton(QPushButton if HAS_PYSIDE else object):
    """Void UI styled button.

    Variants:
        - default: Secondary/outline style
        - primary: Peach accent background
        - ghost: Transparent
        - danger: Red/destructive

    Usage:
        btn = VoidButton("Click me")
        btn = VoidButton("Submit", variant="primary")
        btn = VoidButton("Delete", variant="danger")
    """

    def __init__(
        self,
        text: str = "",
        variant: str = "default",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(text, parent)
        self._variant = variant
        self._apply_variant()

    def _apply_variant(self) -> None:
        if self._variant == "primary":
            self.setProperty("class", "primary")
        elif self._variant == "ghost":
            self.setProperty("class", "ghost")
        elif self._variant == "danger":
            self.setProperty("class", "danger")
        else:
            self.setProperty("class", "")

        self.style().unpolish(self)
        self.style().polish(self)

    @property
    def variant(self) -> str:
        return self._variant

    @variant.setter
    def variant(self, value: str) -> None:
        self._variant = value
        self._apply_variant()


class VoidLabel(QLabel if HAS_PYSIDE else object):
    """Void UI styled label.

    Styles:
        - default: Gray text
        - white: Primary white text
        - muted: Very muted text
        - accent: Peach accent color

    Usage:
        label = VoidLabel("Hello")
        label = VoidLabel("Title", style="white")
        label = VoidLabel("Hint", style="muted")
    """

    def __init__(
        self,
        text: str = "",
        style: str = "default",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(text, parent)
        self._label_style = style
        self._apply_style()

    def _apply_style(self) -> None:
        if self._label_style == "white":
            self.setProperty("class", "white")
        elif self._label_style == "muted":
            self.setProperty("class", "muted")
        elif self._label_style == "accent":
            self.setProperty("class", "accent")
        else:
            self.setProperty("class", "")

        self.style().unpolish(self)
        self.style().polish(self)


class VoidInput(QLineEdit if HAS_PYSIDE else object):
    """Void UI styled input field.

    Usage:
        input_field = VoidInput(placeholder="Enter name...")
    """

    def __init__(
        self,
        placeholder: str = "",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(36)


class VoidCard(QFrame if HAS_PYSIDE else object):
    """Void UI card container.

    A styled container with optional elevation shadow.

    Variants:
        - default: Basic card with border
        - elevated: With drop shadow
        - interactive: Clickable with hover effects

    Usage:
        card = VoidCard()
        layout = QVBoxLayout(card)
        layout.addWidget(QLabel("Card content"))
    """

    if HAS_PYSIDE:
        clicked = Signal()

    def __init__(
        self,
        variant: str = "default",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(parent)
        self._variant = variant
        self._setup()

    def _setup(self) -> None:
        c = DarkColors
        r = RADIUS
        s = SPACING

        self.setFrameStyle(QFrame.StyledPanel)

        base_style = f"""
            VoidCard {{
                background: {c.surface};
                border: 1px solid {c.border};
                border-radius: {r.xl}px;
                padding: {s.lg}px;
            }}
        """

        if self._variant == "elevated":
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(16)
            shadow.setOffset(0, 4)
            shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(shadow)

            base_style = f"""
                VoidCard {{
                    background: {c.raised};
                    border: none;
                    border-radius: {r.xl}px;
                    padding: {s.lg}px;
                }}
            """

        elif self._variant == "interactive":
            self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet(base_style)

    def mousePressEvent(self, event) -> None:
        if self._variant == "interactive":
            self.clicked.emit()
        super().mousePressEvent(event)


class VoidBadge(QLabel if HAS_PYSIDE else object):
    """Void UI badge/tag component.

    Variants:
        - default: Neutral elevated background
        - peach: Peach accent
        - moss: Green/success
        - sand: Warning
        - blush: Blush pink
        - lilac: Purple info
        - danger: Red

    Usage:
        badge = VoidBadge("Active", variant="peach")
        badge = VoidBadge("Error", variant="danger")
    """

    def __init__(
        self,
        text: str = "",
        variant: str = "default",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(text, parent)
        self._variant = variant
        self._setup()

    def _setup(self) -> None:
        c = DarkColors
        r = RADIUS

        colors_map = {
            "default": (c.elevated, c.gray, "transparent"),
            "peach": (c.accent_bg, c.peach, "transparent"),
            "moss": (c.success_bg, c.moss, "transparent"),
            "sand": (c.warning_bg, c.sand, "transparent"),
            "blush": ("rgba(212, 165, 165, 0.15)", c.blush, "transparent"),
            "lilac": (c.info_bg, c.lilac, "transparent"),
            "danger": (c.danger_bg, c.danger, "transparent"),
        }

        bg, fg, border = colors_map.get(self._variant, colors_map["default"])

        self.setStyleSheet(f"""
            VoidBadge {{
                background: {bg};
                color: {fg};
                border: 1px solid {border};
                border-radius: {r.sm}px;
                padding: 3px 8px;
                font-size: 11px;
                font-weight: 500;
            }}
        """)

        self.setAlignment(Qt.AlignCenter)


class VoidProgress(QProgressBar if HAS_PYSIDE else object):
    """Void UI progress bar.

    Colors:
        - peach: Default peach accent
        - moss: Green
        - sand: Yellow/warning
        - danger: Red

    Usage:
        progress = VoidProgress(value=60)
        progress = VoidProgress(value=80, color="moss")
    """

    def __init__(
        self,
        value: int = 0,
        color: str = "peach",
        parent: Optional[QWidget] = None,
    ) -> None:
        if not HAS_PYSIDE:
            raise ImportError("PySide6 is required: pip install void-ui[pyside]")

        super().__init__(parent)
        self._color = color
        self.setValue(value)
        self.setTextVisible(False)
        self.setFixedHeight(8)
        self._apply_color()

    def _apply_color(self) -> None:
        c = DarkColors
        r = RADIUS

        color_map = {
            "peach": c.peach,
            "moss": c.moss,
            "sand": c.sand,
            "danger": c.danger,
        }

        bar_color = color_map.get(self._color, c.peach)

        self.setStyleSheet(f"""
            VoidProgress {{
                background: {c.elevated};
                border: none;
                border-radius: {r.sm}px;
            }}
            VoidProgress::chunk {{
                background: {bar_color};
                border-radius: {r.sm}px;
            }}
        """)
