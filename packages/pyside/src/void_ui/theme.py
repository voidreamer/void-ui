"""Void UI theme and QSS generation.

Generates Qt stylesheets matching the CSS design system.
"""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from void_ui.colors import (
    Colors,
    DarkColors,
    LightColors,
    RADIUS,
    SPACING,
    TYPOGRAPHY,
)

if TYPE_CHECKING:
    from PySide6.QtWidgets import QApplication, QWidget


class ThemeMode(Enum):
    DARK = "dark"
    LIGHT = "light"


class Theme:
    """Void UI theme manager.

    Usage:
        theme = Theme()  # Dark by default
        theme.apply(app)

        # Or light mode
        theme = Theme(ThemeMode.LIGHT)
        theme.apply(app)
    """

    def __init__(self, mode: ThemeMode = ThemeMode.DARK) -> None:
        self.mode = mode
        self._colors = DarkColors if mode == ThemeMode.DARK else LightColors

    @property
    def colors(self) -> Colors:
        return self._colors

    def toggle(self) -> None:
        """Toggle between dark and light mode."""
        self.mode = ThemeMode.LIGHT if self.mode == ThemeMode.DARK else ThemeMode.DARK
        self._colors = DarkColors if self.mode == ThemeMode.DARK else LightColors

    def generate_qss(self) -> str:
        """Generate complete Qt stylesheet."""
        c = self._colors
        r = RADIUS
        s = SPACING
        t = TYPOGRAPHY

        return f'''
/* ==========================================================================
   VOID UI -- Qt Stylesheet
   Generated from @void-ui design tokens
   ========================================================================== */

/* -- Global -- */
QWidget {{
    font-family: {t.font_family};
    font-size: {t.size_base}px;
    color: {c.white};
    background: transparent;
}}

QMainWindow, QDialog {{
    background: {c.void};
}}

/* -- Labels -- */
QLabel {{
    color: {c.gray};
    background: transparent;
    padding: 0;
}}

QLabel[class="white"] {{
    color: {c.white};
}}

QLabel[class="muted"] {{
    color: {c.muted};
}}

QLabel[class="accent"] {{
    color: {c.accent};
}}

/* -- Buttons -- */
QPushButton {{
    background: {c.surface};
    color: {c.gray};
    border: 1px solid {c.border};
    border-radius: {r.md}px;
    padding: {s.sm}px {s.lg}px;
    font-weight: 500;
    font-size: {t.size_sm}px;
    min-height: 32px;
}}

QPushButton:hover {{
    background: {c.raised};
    border-color: {c.elevated};
    color: {c.white};
}}

QPushButton:pressed {{
    background: {c.elevated};
}}

QPushButton:disabled {{
    opacity: 0.5;
    color: {c.muted};
}}

QPushButton[class="primary"] {{
    background: {c.peach};
    color: {c.void};
    border: none;
    font-weight: 500;
}}

QPushButton[class="primary"]:hover {{
    background: {c.accent_hover};
}}

QPushButton[class="danger"] {{
    background: {c.danger};
    color: {c.white};
    border: none;
}}

QPushButton[class="danger"]:hover {{
    background: {c.danger};
}}

QPushButton[class="ghost"] {{
    background: transparent;
    color: {c.gray};
    border: none;
}}

QPushButton[class="ghost"]:hover {{
    background: {c.surface};
    color: {c.white};
}}

/* -- Inputs -- */
QLineEdit, QTextEdit, QPlainTextEdit {{
    background: {c.surface};
    color: {c.white};
    border: 1px solid {c.border};
    border-radius: {r.md}px;
    padding: {s.sm}px {s.md}px;
    font-size: {t.size_base}px;
    selection-background-color: {c.peach};
    selection-color: {c.void};
}}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
    border-color: {c.peach};
    background: {c.raised};
}}

QLineEdit::placeholder {{
    color: {c.muted};
}}

/* -- ComboBox -- */
QComboBox {{
    background: {c.surface};
    color: {c.white};
    border: 1px solid {c.border};
    border-radius: {r.md}px;
    padding: {s.sm}px {s.md}px;
    padding-right: 32px;
    min-height: 32px;
}}

QComboBox:focus {{
    border-color: {c.peach};
}}

QComboBox::drop-down {{
    border: none;
    width: 24px;
}}

QComboBox::down-arrow {{
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid {c.muted};
}}

QComboBox QAbstractItemView {{
    background: {c.surface};
    color: {c.white};
    border: 1px solid {c.border};
    border-radius: {r.sm}px;
    selection-background-color: {c.accent_bg};
    selection-color: {c.accent};
}}

/* -- Checkbox & Radio -- */
QCheckBox, QRadioButton {{
    color: {c.gray};
    spacing: {s.sm}px;
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border: 1px solid {c.border};
    border-radius: {r.sm}px;
    background: {c.surface};
}}

QCheckBox::indicator:checked {{
    background: {c.peach};
    border-color: {c.peach};
}}

QRadioButton::indicator {{
    width: 18px;
    height: 18px;
    border: 1px solid {c.border};
    border-radius: 9px;
    background: {c.surface};
}}

QRadioButton::indicator:checked {{
    background: {c.peach};
    border-color: {c.peach};
}}

/* -- Scrollbars -- */
QScrollBar:vertical {{
    background: transparent;
    width: 6px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background: {c.border};
    border-radius: 3px;
    min-height: 40px;
}}

QScrollBar::handle:vertical:hover {{
    background: {c.muted};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 6px;
    margin: 0;
}}

QScrollBar::handle:horizontal {{
    background: {c.border};
    border-radius: 3px;
    min-width: 40px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {c.muted};
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0;
}}

/* -- TreeView & ListView -- */
QTreeView, QListView, QTableView {{
    background: {c.surface};
    color: {c.white};
    border: 1px solid {c.border_light};
    border-radius: {r.md}px;
    outline: none;
}}

QTreeView::item, QListView::item {{
    padding: {s.sm}px;
    border-radius: {r.sm}px;
}}

QTreeView::item:hover, QListView::item:hover {{
    background: {c.raised};
}}

QTreeView::item:selected, QListView::item:selected {{
    background: {c.accent_bg};
    color: {c.accent};
}}

QHeaderView::section {{
    background: {c.surface};
    color: {c.gray};
    border: none;
    border-bottom: 1px solid {c.border};
    padding: {s.sm}px {s.md}px;
    font-weight: 500;
    font-size: {t.size_xs}px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* -- TabWidget -- */
QTabWidget::pane {{
    border: 1px solid {c.border};
    border-radius: {r.md}px;
    background: {c.surface};
}}

QTabBar::tab {{
    background: transparent;
    color: {c.gray};
    padding: {s.sm}px {s.lg}px;
    border-radius: {r.md}px;
    font-weight: 500;
}}

QTabBar::tab:hover {{
    color: {c.white};
}}

QTabBar::tab:selected {{
    background: {c.raised};
    color: {c.white};
}}

/* -- GroupBox -- */
QGroupBox {{
    background: {c.surface};
    border: 1px solid {c.border_light};
    border-radius: {r.lg}px;
    padding: {s.lg}px;
    padding-top: {s.xl}px;
    margin-top: {s.md}px;
}}

QGroupBox::title {{
    color: {c.white};
    font-weight: 700;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 {s.sm}px;
    left: {s.md}px;
}}

/* -- ProgressBar -- */
QProgressBar {{
    background: {c.elevated};
    border: none;
    border-radius: {r.sm}px;
    height: 8px;
    text-align: center;
}}

QProgressBar::chunk {{
    background: {c.peach};
    border-radius: {r.sm}px;
}}

/* -- Slider -- */
QSlider::groove:horizontal {{
    background: {c.border};
    height: 4px;
    border-radius: 2px;
}}

QSlider::handle:horizontal {{
    background: {c.peach};
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}}

QSlider::handle:horizontal:hover {{
    background: {c.accent_hover};
}}

/* -- SpinBox -- */
QSpinBox, QDoubleSpinBox {{
    background: {c.surface};
    color: {c.white};
    border: 1px solid {c.border};
    border-radius: {r.md}px;
    padding: {s.sm}px;
}}

QSpinBox:focus, QDoubleSpinBox:focus {{
    border-color: {c.peach};
}}

/* -- ToolTip -- */
QToolTip {{
    background: {c.white};
    color: {c.void};
    border: none;
    border-radius: {r.md}px;
    padding: {s.sm}px {s.md}px;
    font-size: {t.size_xs}px;
}}

/* -- Menu -- */
QMenu {{
    background: {c.surface};
    border: 1px solid {c.border};
    border-radius: {r.lg}px;
    padding: {s.xs}px;
}}

QMenu::item {{
    padding: {s.sm}px {s.lg}px;
    border-radius: {r.sm}px;
    color: {c.gray};
}}

QMenu::item:selected {{
    background: {c.raised};
    color: {c.white};
}}

QMenu::separator {{
    height: 1px;
    background: {c.border};
    margin: {s.xs}px {s.sm}px;
}}

/* -- StatusBar -- */
QStatusBar {{
    background: {c.surface};
    color: {c.gray};
    border-top: 1px solid {c.border_light};
}}
'''

    def apply(self, widget: QWidget | QApplication) -> None:
        """Apply theme to a widget or application."""
        widget.setStyleSheet(self.generate_qss())


def apply_theme(widget: QWidget | QApplication, mode: ThemeMode = ThemeMode.DARK) -> Theme:
    """Convenience function to apply theme.

    Usage:
        from void_ui import apply_theme
        apply_theme(app)
    """
    theme = Theme(mode)
    theme.apply(widget)
    return theme
