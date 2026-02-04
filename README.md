# Void UI

Cryptic tech aesthetic. Warm void, soft pastels, Japanese and tech vibes.

A design system extracted from [voidreamer.github.io](https://voidreamer.github.io). Available as CSS, React components, and PySide6 widgets.

## Packages

| Package | Description | Path |
|---------|-------------|------|
| `@void-ui/css` | CSS design tokens and components | `packages/css` |
| `@void-ui/react` | React component library | `packages/react` |
| `void-ui` (PyPI) | PySide6 theme and widgets | `packages/pyside` |

## Quick Start

### CSS

```html
<link rel="stylesheet" href="@void-ui/css/dist/void.css">
```

Or import in JS/CSS:

```css
@import '@void-ui/css/dist/void.css';
```

### React

```tsx
import { Button, Card, useTheme } from '@void-ui/react'

function App() {
  const { theme, toggle } = useTheme()
  return (
    <Card>
      <Button variant="primary" onClick={toggle}>
        Toggle Theme
      </Button>
    </Card>
  )
}
```

### PySide6

```python
from void_ui import apply_theme, VoidButton

app = QApplication([])
apply_theme(app)
```

## Design Tokens

### Colors

| Token | Value | Use |
|-------|-------|-----|
| `--void` | `#0f0d0b` | Page background |
| `--surface` | `#171412` | Card/panel backgrounds |
| `--raised` | `#1f1b18` | Hover states, elevated surfaces |
| `--elevated` | `#2a2521` | Higher elevation |
| `--peach` | `#e8a87c` | Primary accent |
| `--blush` | `#d4a5a5` | Secondary warm |
| `--sand` | `#c9b896` | Tertiary, warnings |
| `--moss` | `#a5b5a0` | Success states |
| `--lilac` | `#b8a9c9` | Info, subtle accent |
| `--clay` | `#c17c60` | Bold, logo accent |

### Fonts

| Token | Stack | Use |
|-------|-------|-----|
| `--font` | Inter | Body text |
| `--mono` | JetBrains Mono | Code, data |
| `--jp` | Noto Sans JP | Cryptic decorations |
| `--tech` | Orbitron | Technical labels, numbers |

## CSS Components

### Button

```html
<button class="void-btn void-btn--primary">Submit</button>
<button class="void-btn void-btn--outline">Cancel</button>
<button class="void-btn void-btn--ghost void-btn--sm">Details</button>
```

Variants: `--primary`, `--outline`, `--ghost`, `--danger`
Sizes: `--sm`, `--lg`
Modifiers: `--icon`, `--block`, `--pill`, `--loading`

### Card

```html
<div class="void-card">
  <div class="void-card__header">
    <div class="void-card__title">Pipeline Status</div>
    <div class="void-card__desc">Last updated 5m ago</div>
  </div>
  <div class="void-card__body">...</div>
  <div class="void-card__footer">
    <button class="void-btn void-btn--ghost">Cancel</button>
    <button class="void-btn void-btn--primary">Save</button>
  </div>
</div>
```

Variants: `--elevated`, `--interactive`, `--glass`, `--compact`

### Input

```html
<div class="void-form-group">
  <label class="void-label">Shot Name</label>
  <input class="void-input" placeholder="SH010" />
  <span class="void-hint">Sequence_Shot format</span>
</div>
```

### Badge

```html
<span class="void-badge void-badge--peach">Active</span>
<span class="void-badge void-badge--moss">Approved</span>
<span class="void-badge void-badge--tech">v2.1</span>
```

Colors: `--peach`, `--moss`, `--sand`, `--blush`, `--lilac`, `--danger`, `--outline`

### Table

```html
<div class="void-table-wrap">
  <table class="void-table">
    <thead><tr><th>Shot</th><th>Status</th></tr></thead>
    <tbody><tr><td>SH010</td><td>In Progress</td></tr></tbody>
  </table>
</div>
```

### More Components

- Tabs: `.void-tabs` + `.void-tab`
- Modal: `.void-overlay` + `.void-modal`
- Dropdown: `.void-dropdown` + `.void-dropdown__menu`
- Alert: `.void-alert` with `--success`, `--warning`, `--danger`
- Progress: `.void-progress` + `.void-progress__bar`
- Toast: `.void-toast` with status variants
- Avatar: `.void-avatar` with `--sm`, `--lg`, groups
- Sidebar: `.void-sidebar` with sections and links
- Navbar: `.void-navbar` glass navigation
- Tooltip: `.void-tooltip-wrap` + `.void-tooltip`
- Spinner: `.void-spinner`
- Skeleton: `.void-skeleton`

## Light Theme

```html
<body data-theme="light">
```

All tokens automatically adjust for warm-light surfaces.

## Cryptic Decorations

The signature void aesthetic. Use sparingly:

```html
<span class="void-cryptic">虚空設計</span>
<span class="void-tech">SYS.GRID.04</span>
<span class="void-mono">0x4F70656E</span>
```

## Development

```bash
npm install
npm run build:css    # Build CSS
npm run build:react  # Build React components
npm run build        # Build everything
```

## Used By

- [voidreamer.github.io](https://voidreamer.github.io) (Portfolio)
- [OpenGrid](https://github.com/voidreamer/opengrid-lite) (Production tracking)

## License

MIT
