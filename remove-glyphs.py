#!/usr/bin/env python
import pprint
import re

glyph_codes = []
pat = re.compile(r'0x([\da-f]+)', re.I)
glyph_list = './glyph-list.txt'
with open(glyph_list, 'r') as f:
  for line in f:
    m = pat.search(line)
    if m:
      glyph_codes.append(int(m.group(1), 16))

pprint.pprint(glyph_codes)
