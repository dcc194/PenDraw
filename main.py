import numpy as np
import cv2

img = cv2.imread('DSC_0107.JPG',0)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
height, width = img.shape
cv2.resizeWindow('image',width/4,height/4)
cv2.waitKey(0)
cv2.destroyAllWindows()