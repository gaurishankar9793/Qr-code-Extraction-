# -*- coding: utf-8 -*-


from Imagehandler import Imagehandler
import yaml
import glob
import os
import cv2 as cv2
import argparse
#import cv2 as cv
import pyzbar

import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('path', help= 'paste path to biog.txt file')
args = parser.parse_args()


name = args.path
head, sep, tail = name.partition('.')
image = cv2.imread(args.path)


src = image
scale_ratio = 2.0
image = cv2.resize(src, None, fx=scale_ratio, fy=scale_ratio, interpolation=cv2.INTER_NEAREST)
src = image
image = cv2.GaussianBlur(src, (5, 5), 0)

obj = Imagehandler(image)
TransformImage = obj.QRCodeInImage()
cv2.imwrite(head+'_output.'+tail,TransformImage)

cv2.imshow('Qr code is ',TransformImage)
cv2.waitKey(0)
cv2.destroyAllWindows() 