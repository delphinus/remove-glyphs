#!/usr/bin/env python
import fontforge
import os
import pprint
import re
import sys

if len(sys.argv) != 3:
  print('please specify filenames')
  sys.exit(1)

source_font_filename = sys.argv[1]
font_filename = sys.argv[2]
glyph_codes = []
pat = re.compile(r'0x([\da-f]+)', re.I)
glyph_list = './glyph-list.txt'
with open(glyph_list, 'r') as f:
  for line in f:
    m = pat.search(line)
    if m:
      glyph_codes.append(int(m.group(1), 16))

sw_font = fontforge.open(source_font_filename)
dw_font = fontforge.open(font_filename)

for code in glyph_codes:
  sw_font.selection.select(('more', 'unicode'), code)
  dw_font.selection.select(('more', 'unicode'), code)

for code in glyph_codes:
  print(code)
  sw_font.selection.select(code)
  sw_font.copy()
  dw_font.selection.select(code)
  dw_font.paste()

font_pat = re.compile(r'^([^-]*).*?([^-]*(?!.*-))$')
dw_font.familyname += ' Reduced'
fullname, fallbackStyle = font_pat.match(dw_font.fullname).groups()
dw_font.fullname = fullname + ' Reduced ' + fallbackStyle
fontname, fallbackStyle = font_pat.match(dw_font.fontname).groups()
dw_font.fontname = fontname + 'Reduced-' + fallbackStyle
dw_font.appendSFNTName('English (US)', 'Preferred Family', dw_font.familyname)
dw_font.appendSFNTName('English (US)', 'Compatible Full', dw_font.fullname)
dw_font.appendSFNTName('English (US)', 'SubFamily', fallbackStyle)

dest = os.path.basename(font_filename).replace('.', '-Reduced.')
dw_font.generate(dest)
print('{0} generated'.format(dw_font.fullname))
