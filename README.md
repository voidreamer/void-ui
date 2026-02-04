# ⬛ Void UI

Cryptic tech aesthetic — warm void, soft pastels, Japanese/tech vibes.

A CSS design system extracted from [voidreamer.github.io](https://voidreamer.github.io). Drop it into any project for instant dark, warm, production-ready UI.

## Quick Start

```html
<link rel="stylesheet" href="void.css">
```

Or import in JS/CSS:

```css
@import 'void-ui/void.css';
```

## Modular Imports

Pick what you need:

```css
@import 'void-ui/tokens.css';      /* Design tokens only (CSS variables) */
@import 'void-ui/base.css';        /* Reset + typography + utilities */
@import 'void-ui/components.css';  /* All components */
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
| `--sand` | `#c9b896` | Tertiary/warnings |
| `--moss` | `#a5b5a0` | Success states |
| `--lilac` | `#b8a9c9` | Info/subtle accent |
| `--clay` | `#c17c60` | Bold/logo accent |

### Fonts

| Token | Stack | Use |
|-------|-------|-----|
| `--font` | Inter | Body text |
| `--mono` | JetBrains Mono | Code, data |
| `--jp` | Noto Sans JP | Cryptic decorations |
| `--tech` | Orbitron | Technical labels, numbers |

## Components

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

### Sidebar & Side Rail

```html
<!-- Full sidebar -->
<aside class="void-sidebar">
  <div class="void-sidebar__header">...</div>
  <div class="void-sidebar__section">
    <div class="void-sidebar__section-title">Production</div>
    <a class="void-sidebar__link void-sidebar__link--active">Projects</a>
    <a class="void-sidebar__link">Shots</a>
  </div>
</aside>

<!-- Minimal rail (icon-only, like the blog) -->
<nav class="void-rail">
  <div class="void-rail__logo">V</div>
  <a class="void-rail__link void-rail__link--active">...</a>
  <span class="void-rail__cryptic">虚空設計</span>
</nav>
```

### More Components

- **Tabs** — `.void-tabs` + `.void-tab`
- **Modal** — `.void-overlay` + `.void-modal`
- **Dropdown** — `.void-dropdown` + `.void-dropdown__menu`
- **Alert** — `.void-alert` with `--success`, `--warning`, `--danger`
- **Progress** — `.void-progress` + `.void-progress__bar`
- **Toast** — `.void-toast` with status variants
- **Avatar** — `.void-avatar` with `--sm`, `--lg`, groups
- **Tooltip** — `.void-tooltip-wrap` + `.void-tooltip`
- **Separator** — `.void-sep` with optional text
- **Kbd** — `.void-kbd`
- **Skeleton** — `.void-skeleton`
- **Spinner** — `.void-spinner`

## Light Theme

```html
<body data-theme="light">
```

All tokens automatically adjust for warm-light surfaces.

## Cryptic Decorations

The signature void aesthetic — use sparingly:

```html
<span class="void-cryptic">虚空設計</span>
<span class="void-tech">SYS.GRID.04</span>
<span class="void-mono">0x4F70656E</span>
```

## Used By

- [voidreamer.github.io](https://voidreamer.github.io) — Portfolio
- [OpenGrid](https://github.com/voidreamer/opengrid-lite) — Production tracking

## License

MIT
