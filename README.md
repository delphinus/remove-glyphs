# remove-glyph.py

```sh
~/git/github.com/pettarin/glyphIgo/src/glyphIgo.py list -f ~/Shared/Documents/fonts/Iosevka/iosevka-pack-1.11.4/iosevka-regular.ttc > glyph-list.txt
./remove-glyphs.py ~/Shared/Documents/fonts/Iosevka/iosevka-pack-1.11.4/iosevka-regular.ttf /usr/local/opt/ricty/share/fonts/RictyDiscord-Regular.ttf
for i in ~/git/github.com/delphinus/nerd-fonts-simple/build2/*
do
  echo $i
  ./remove-glyphs.py ~/Shared/Documents/fonts/Iosevka/iosevka-pack-1.11.4/iosevka-regular.ttc $i
done
for i in /usr/local/opt/ricty/share/fonts/*
do
  echo $i
  ./remove-glyphs.py ~/Shared/Documents/fonts/Iosevka/iosevka-pack-1.11.4/iosevka-regular.ttc $i
done
```
