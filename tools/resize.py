import cv2
import os
import lmdb  # install lmdb by "pip install lmdb"
import cv2
import numpy as np
import glob



path = '/home/huy/Computer-Vision/CS529/rawdata/huy/'
file_name = [os.path.splitext(f)[0] for f in glob.glob(path + "*.jpg")]
jpg_file = [s + ".jpg" for s in file_name]
# print(heic_file)
for i in jpg_file:
    img_file = i.replace('.jpg', '_resize.jpg')
    img_name = img_file.split('/')[-1]
    img = cv2.imread(i, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    if img.shape[0] > 3000:
        scale_percent = 20
    else:
        scale_percent = 40 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    if not os.path.exists(path+"resized"):
        os.mkdir(path+"resized")
    cv2.imwrite(path +"resized/" + img_name,resized)

    if width > height:
        img_rotate_90_counterclockwise = cv2.rotate(
                resized, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(path +"resized/" + img_name, img_rotate_90_counterclockwise)