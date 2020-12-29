import os
import lmdb  # install lmdb by "pip install lmdb"
import cv2
import numpy as np
import glob
from PIL import Image
from cykooz.heif.pil import register_heif_opener #pip install cykooz.heif

file_name = [os.path.splitext(f)[0] for f in glob.glob("/home/huy/Computer-Vision/CS529/rawdata/*.HEIC")]
heic_file = [s + ".HEIC" for s in file_name]
# print(heic_file)
for i in heic_file:
    img_file = i.replace('.HEIC', '.jpg')
    
    register_heif_opener()
    img = Image.open(i)
    assert isinstance(img, Image.Image)
    assert img.size == (3024, 4032)
    assert img.mode == 'RGB'
    # assert img.getpixel((100, 100)) == (73, 74, 69)
    img.save(img_file, 'JPEG')
    print(img_file)