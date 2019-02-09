# -*- coding: utf-8 -*-


from Imagehandler import Imagehandler
import yaml
import glob
import os
import cv2 as cv2
import argparse




import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('path', help= 'paste path to biog.txt file')
args = parser.parse_args()



image = cv2.imread(args.path)
#image = cv.imread('uncomment to directly debugg')
obj = Imagehandler(image)
TransformImage = obj.QRCodeInImage()

cv.imshow('Qr code is ',TransformImage)
cv.waitKey(0)
cv.destroyAllWindows()
