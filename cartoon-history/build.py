#!/usr/bin/env python3
"""Inline fonts and sound effects into cartoon.src.html -> cartoon.html (one self-contained file)."""
import base64, json, pathlib

here = pathlib.Path(__file__).parent
sfx_dir = here.parent / '.claude/skills/sound-effects/sfx'
SFX = {
    'impact': 'kit/impact.ogg',
    'whoosh': 'kit/whoosh.ogg',
    'pop': 'kit/pop.ogg',
    'click': 'kit/click.ogg',
    'tick': 'kit/tick.ogg',
    'boom': 'impact/kenney-sci-lowfrequency-explosion-000.ogg',
}
sfx = {k: base64.b64encode((sfx_dir / v).read_bytes()).decode() for k, v in SFX.items()}
src = (here / 'cartoon.src.html').read_text()
src = src.replace('/*FONTS*/', (here / 'fonts/fonts.css').read_text())
src = src.replace('/*SFX*/{}', json.dumps(sfx))
(here / 'cartoon.html').write_text(src)
print('cartoon.html', len(src) // 1024, 'KB')
