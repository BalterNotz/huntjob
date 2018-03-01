#!/usr/bin/env python
# Python3

'''验证码识别'''

import pytesseract
from PIL import Image, ImageEnhance

img = Image.open(".BalterNotz.png")
print(img.size)
code = pytesseract.image_to_string(img, "eng")
print(code)
img.close()
