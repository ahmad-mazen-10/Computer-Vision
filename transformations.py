import cv2
import numpy as np

img_road = cv2.imread('road.jpg')

# ------------  Translated   ----------------------
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

translated = translate(img_road, 12, 12)
cv2.imshow('translated', translated)


# ------------  Rotated   ----------------------
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    
    if(rotPoint) is None:
        rotPoint  = (w//2 ,h//2)
        
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (w, h)
    
    return cv2.warpAffine(img, rotMat, dimensions)

rotated =rotate(img_road, 45)
cv2.imshow('Rotated', rotated)




#   50 : 21  min




cv2.waitKey(0)
cv2.destroyAllWindows()
