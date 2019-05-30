import time
import math
import pyscreenshot
from PIL import Image, ImageFilter

while 1 == 1:
    if math.floor(time.time()) % 5 == 0:
        im = pyscreenshot.grab()
        print("took screenshot!")

        blurred_image = im.filter(ImageFilter.BLUR)
        blurred_image = blurred_image.filter(ImageFilter.BLUR)
        blurred_image = blurred_image.filter(ImageFilter.BLUR)
        blurred_image = blurred_image.filter(ImageFilter.BLUR)
        blurred_image = blurred_image.filter(ImageFilter.BLUR)
        print("screenshot blured!")
        blurred_image.save('/home/xdprindx/Pictures/lock.png')
        print("screenshot saved!")

    time.sleep(1)
