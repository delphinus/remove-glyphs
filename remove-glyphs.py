#!/usr/bin/env python
import fontforge
import os
import pprint
import re
import sys

if len(sys.argv) != 2:
  print('please specify filenames')
  sys.exit(1)

font_filename = sys.argv[1]
glyph_codes = []
pat = re.compile(r'0x([\da-f]+)', re.I)
glyph_list = './glyph-list.txt'
with open(glyph_list, 'r') as f:
  for line in f:
    m = pat.search(line)
    if m:
      glyph_codes.append(int(m.group(1), 16))

source_font = fontforge.open(font_filename)

for code in glyph_codes:
  source_font.selection.select(('more', 'unicode'), code)
  for glyph in source_font.selection.byGlyphs:
    source_font.removeGlyph(glyph)

fontname, fallbackStyle = re.match("^([^-]*).*?([^-]*(?!.*-))$", source_font.fontname).groups()
new_fontname = fontname + ' Reduced'
source_font.familyname = new_fontname
source_font.fullname = new_fontname + ' ' + fallbackStyle
source_font.fontname = new_fontname.replace(' ', '') + '-' + fallbackStyle
source_font.appendSFNTName('English (US)', 'Preferred Family', source_font.familyname)
source_font.appendSFNTName('English (US)', 'Compatible Full', source_font.fullname)
source_font.appendSFNTName('English (US)', 'SubFamily', fallbackStyle)


dest = os.path.basename(font_filename).replace('.', '-Reduced.')
source_font.generate(dest)
print('{0} generated'.format(new_fontname))
