#!/usr/bin/env python
import fontforge
import os
import pprint
import psMat
import re
import sys

if len(sys.argv) != 3:
  print('please specify filenames')
  sys.exit(1)

source_font_filename = sys.argv[1]
dest_font_filename = sys.argv[2]
glyph_codes = []
pat = re.compile(r'0x([\da-f]+)', re.I)
glyph_list = './glyph-list.txt'
with open(glyph_list, 'r') as f:
  for line in f:
    m = pat.search(line)
    if m:
      glyph_codes.append(int(m.group(1), 16))

sw_font = fontforge.open(source_font_filename)
dw_font = fontforge.open(dest_font_filename)

scale_size = 1.0
y_move = -40.0
#scale_size = 0.90
#y_move = 40.0
#powerline_codes = range(0xe0b0, 0xe0b3)
#powerline_scale_size = 0.87
#powerline_y_move = 40.0

for code in glyph_codes:
  sw_font.selection.select(code)
  sw_font.copy()
  dw_font.selection.select(code)
  dw_font.paste()
#  if code in powerline_codes:
#    dw_font.transform(psMat.scale(powerline_scale_size))
#    dw_font.transform(psMat.translate(0, powerline_y_move))
#  else:
#    dw_font.transform(psMat.scale(scale_size))
#    dw_font.transform(psMat.translate(0, y_move))
  dw_font.transform(psMat.scale(scale_size))
  dw_font.transform(psMat.translate(0, y_move))

font_pat = re.compile(r'^([^-]*).*?([^-]*(?!.*-))$')
dw_font.familyname += ' Reduced'
fullname, fallbackStyle = font_pat.match(dw_font.fullname).groups()
dw_font.fullname = fullname + ' Reduced'
if fallbackStyle != '':
  dw_font.fullname += ' ' + fallbackStyle
fontname, fallbackStyle = font_pat.match(dw_font.fontname).groups()
dw_font.fontname = fontname + 'Reduced'
if fallbackStyle != '':
  dw_font.fontname += '-' + fallbackStyle
dw_font.appendSFNTName('English (US)', 'Preferred Family', dw_font.familyname)
dw_font.appendSFNTName('English (US)', 'Compatible Full', dw_font.fullname)
dw_font.appendSFNTName('English (US)', 'SubFamily', fallbackStyle)

dest = os.path.basename(dest_font_filename).replace('.', '-Reduced.')
dw_font.generate(dest)
print('{0} generated'.format(dw_font.fullname))
