import cv2
from PIL import Image
import os
import argparse


def rotate(directory, rotate):
    for img in os.listdir(directory):
        im = cv2.imread(directory+img)

        if rotate == "right":
            img_rotate_90_clockwise = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(directory+"rotate/"+img, img_rotate_90_clockwise)
        if rotate == "top":
            img_rotate_90_counterclockwise = cv2.rotate(
            im, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(directory+"rotate/"+img, img_rotate_90_counterclockwise)
        if rotate == "left":
            img_rotate_180 = cv2.rotate(im, cv2.ROTATE_180)
            cv2.imwrite(directory+"rotate/"+img, img_rotate_180)


def name():
    print('hello')
    parser = argparse.ArgumentParser(description="Rescale image")
    parser.add_argument('-d', '--directory', type=str,
                        help='diectory img', required=True)
    parser.add_argument('-r', '--rotate', type=str,
                        help='rotate: left right top', required=True)
    args = parser.parse_args()
    rotate(args.directory, args.rotate)


name()
