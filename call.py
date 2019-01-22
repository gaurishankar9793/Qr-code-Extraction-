# -*- coding: utf-8 -*-


from Imagehandler import Imagehandler
import yaml
import glob
import os
import cv2 as cv





image = cv.imread('C:/Users/Gauri Shankar Mishra/Desktop/QRCodeReader-master/QRCodeReader-master/Input/qw.png')
obj = Imagehandler(image)
TransformImage = obj.QRCodeInImage()

cv.imshow('Qr code is ',TransformImage)
cv.waitKey(0)
cv.destroyAllWindows()







