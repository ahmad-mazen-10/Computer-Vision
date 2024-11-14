import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage

Figure_1 = cv2.imread('task_3/Figure_2.0.png')
Figure_2 = cv2.imread('task_3/Figure_2.1.png')
# Figure_3 = cv2.imread('task_3/Figure_2.2.png')
cv2.imshow('Original Image 1', Figure_1)
cv2.imshow('Original Image 2', Figure_2)
# cv2.imshow('Original Image 3', Figure_3)

# Q1: Write the python code to blur the image (Figure 1) with a gaussian filter and kernel size=7 : 

Figure_1_blur = cv2.GaussianBlur(Figure_1, (7, 7), 0)
cv2.imshow('Blurred Image', Figure_1_blur)



# Q2: Write the python code to highlight the rapid transition in the image (Figure 1) with a canny filter : 

Figure_1_Canny = cv2.Canny(Figure_1, 70, 70)
cv2.imshow('Figure_1_Canny ', Figure_1_Canny)       # 1 , 0



# Q3: Write the python code to extract edges from image (Figure 2) using Sobel derivative : 
sobelx =  cv2.Sobel(Figure_2, cv2.CV_64F, 1,0 ,ksize=5)
sobely =  cv2.Sobel(Figure_2, cv2.CV_64F, 0,1 ,ksize=5)

sobelImg = cv2.add(sobelx, sobely)
cv2.imshow('Sobel Image', sobelImg)



# Q4: Write the python code to extract edges from image (Figure 2) using Scharr derivative : 

schx =  cv2.Scharr(Figure_2, cv2.CV_64F, 1,0 )
schy =  cv2.Scharr(Figure_2, cv2.CV_64F, 0,1 )

cv2.imshow('Scharr Image', sobelImg)



# Q5: Write the python code to extract edges from image (Figure 2) using Laplacian derivative : 

laplacian = cv2.Laplacian(Figure_2, cv2.CV_64F)
cv2.imshow('laplacian Image', laplacian)




# Q6: Write the python code to extract edges from image (Figure 1) using custom filter in image (Figure 3) : 



# Q7: What is the best edge detector and what is the reason? 

# ==> The " Canny Edge " is the best edge detector ,becouse it effectively reduces noise using a Gaussian filter and accurately detects edges through gradient calculation
 


cv2.waitKey(0)
cv2.destroyAllWindows()
