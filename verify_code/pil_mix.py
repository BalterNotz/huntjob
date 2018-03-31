#!/usr/bin/env python
# Python3

import PIL
import PIL.BdfFontFile as bdf

print(PIL._plugins)
print(type(PIL._plugins))
print(PIL.PILLOW_VERSION)
print(type(PIL.PILLOW_VERSION))
a = "abc"
b = "abc"
print(id(a) == id(b))
print(PIL.VERSION)
print(PIL.version)
print(PIL.__version__)

print(type(bdf.bdf_slant))

