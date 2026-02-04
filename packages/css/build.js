#!/usr/bin/env node
/**
 * Void UI - CSS Build Script
 * Concatenates src/*.css into dist/void.css (and minified variant).
 */

const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, 'src');
const DIST = path.join(__dirname, 'dist');

const FILES = ['tokens.css', 'base.css', 'components.css'];

function minify(css) {
  return css
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\s+/g, ' ')
    .replace(/\s*([{}:;,>~+])\s*/g, '$1')
    .replace(/;}/g, '}')
    .replace(/^\s+|\s+$/g, '');
}

function build() {
  fs.mkdirSync(DIST, { recursive: true });

  const parts = FILES.map((f) => {
    const fp = path.join(SRC, f);
    return fs.readFileSync(fp, 'utf8');
  });

  const css = parts.join('\n\n');
  const min = minify(css);

  fs.writeFileSync(path.join(DIST, 'void.css'), css);
  fs.writeFileSync(path.join(DIST, 'void.min.css'), min);

  const sizeKB = (Buffer.byteLength(css) / 1024).toFixed(1);
  const minKB = (Buffer.byteLength(min) / 1024).toFixed(1);
  console.log(`Built dist/void.css (${sizeKB} KB)`);
  console.log(`Built dist/void.min.css (${minKB} KB)`);
}

if (process.argv.includes('--watch')) {
  build();
  console.log('\nWatching for changes...');
  fs.watch(SRC, { recursive: false }, (event, filename) => {
    if (filename && filename.endsWith('.css')) {
      console.log(`\n${filename} changed, rebuilding...`);
      try {
        build();
      } catch (e) {
        console.error('Build error:', e.message);
      }
    }
  });
} else {
  build();
}
