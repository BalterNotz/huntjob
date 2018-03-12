#!/usr/bin/env python
# Python3

'''验证码识别'''

import pytesseract
from PIL import Image, ImageEnhance

fname = ".ffth"
fsuffix = "jpg"

img = Image.open(fname + "." + fsuffix)
assert isinstance(img, Image.Image)
print(img.getbands())
img.convert("1")
img.save(fname + "_b_" + "." + fsuffix)
for p in img.getdata():
    print(p)
code = pytesseract.image_to_string(img, "eng")
print(code)
img.close()
