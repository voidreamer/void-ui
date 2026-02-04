# Void UI for PySide6

Cryptic tech aesthetic UI library for Qt applications, matching the web design system.

## Installation

```bash
pip install void-ui[pyside]
```

## Quick Start

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from void_ui import apply_theme, VoidButton, VoidCard, VoidLabel, VoidBadge, VoidProgress

app = QApplication([])

# Apply Void theme
apply_theme(app)

# Create window
window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)
layout = QVBoxLayout(central)

# Use styled widgets
layout.addWidget(VoidLabel("Pipeline Status", style="white"))
layout.addWidget(VoidButton("Deploy", variant="primary"))
layout.addWidget(VoidButton("Cancel", variant="ghost"))
layout.addWidget(VoidBadge("Active", variant="peach"))
layout.addWidget(VoidProgress(value=72, color="moss"))

window.show()
app.exec()
```

## Theme

```python
from void_ui import Theme
from void_ui.theme import ThemeMode

# Dark theme (default)
theme = Theme()
theme.apply(app)

# Light theme
theme = Theme(ThemeMode.LIGHT)
theme.apply(app)

# Toggle
theme.toggle()
theme.apply(app)
```

## Colors

Access design tokens directly:

```python
from void_ui.colors import DarkColors, LightColors, SPACING, RADIUS

print(DarkColors.peach)       # #e8a87c
print(DarkColors.void)        # #0f0d0b
print(DarkColors.surface)     # #171412
print(SPACING.md)             # 16
print(RADIUS.lg)              # 8
```

## Widgets

### VoidButton

```python
VoidButton("Default")
VoidButton("Primary", variant="primary")
VoidButton("Ghost", variant="ghost")
VoidButton("Danger", variant="danger")
```

### VoidCard

```python
card = VoidCard()                          # Basic
card = VoidCard(variant="elevated")        # With shadow
card = VoidCard(variant="interactive")     # Clickable
card.clicked.connect(on_card_click)
```

### VoidBadge

```python
VoidBadge("Label")
VoidBadge("Active", variant="peach")
VoidBadge("Approved", variant="moss")
VoidBadge("Warning", variant="sand")
VoidBadge("Error", variant="danger")
VoidBadge("Info", variant="lilac")
```

### VoidLabel

```python
VoidLabel("Default gray text")
VoidLabel("Title text", style="white")
VoidLabel("Muted hint", style="muted")
VoidLabel("Accent text", style="accent")
```

### VoidProgress

```python
VoidProgress(value=50)
VoidProgress(value=80, color="moss")
VoidProgress(value=30, color="sand")
VoidProgress(value=90, color="danger")
```

## Custom QSS

Generate the stylesheet for manual application:

```python
from void_ui import Theme

theme = Theme()
qss = theme.generate_qss()
widget.setStyleSheet(qss)
```

## Design Tokens

| Token | Dark | Light |
|-------|------|-------|
| `void` | #0f0d0b | #faf8f5 |
| `surface` | #171412 | #f5f2ee |
| `peach` | #e8a87c | #e8a87c |
| `white` | #f5f0eb | #1a1816 |
| `border` | #252220 | #e0dbd5 |

See `void_ui/colors.py` for all tokens.

## License

MIT
