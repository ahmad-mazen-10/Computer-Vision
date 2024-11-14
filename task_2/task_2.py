import cv2
import numpy as np
from scipy import ndimage
# from matplotlib import puplot as plt

image = cv2.imread('image_task_2.0.png')
figure_3 =cv2.imread('image_task_2.2.png')
cv2.imshow('Image ', image)
cv2.imshow('figure_3 ', figure_3)


#Q1: Read an image (Figure 1) and resize it to (120, 300) :

resize = cv2.resize(image, (120, 300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resize image ', resize)

#Q2: Read a BGR image (Figure 1) and convert it to a binary image :
#1-gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image ', gray)
#2-binary
(thresh, binaryImage) = cv2.threshold(gray,127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary image ', binaryImage)


# Q3: Show the 3 channels for the BGR image (Figure 1) :

RGB = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
R, G, B = cv2.split(image)
cv2.imshow('RGB image ', RGB)
cv2.imshow('R image ', R)
cv2.imshow('G image ', G)
cv2.imshow('B image ', B)

merge = cv2.merge((R, G, B))
cv2.imshow('merge image ', merge)

# Q4: Display the saturation channel from an HSV (Figure 2) image :

HSV = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV image ', HSV)

H = HSV[:,:,0]
S = HSV[:,:,1]
V = HSV[:,:,2]
cv2.imshow('Hue image ', H)
cv2.imshow('Saturation image ', S)
cv2.imshow('Value image ', V)


# Q5: Blur the image (Figure 1) with an average filter using a 5*5 kernel :
average_blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('average blur (5, 5) Image', average_blur)


# Q6: Using the median filter with kernel size from your choice to smooth the image (Figure 1) :
median = cv2.medianBlur(image, 17)
cv2.imshow('Blurred median 17 Image', median)


# Q7: We noticed some imperfections after segmenting the image (Figure 3). Write the code to erode this image :
gray_Fig3 = cv2.cvtColor(figure_3, cv2.COLOR_BGR2GRAY)
(thresh, binaryFig3) = cv2.threshold(gray_Fig3,127, 255, cv2.THRESH_BINARY)

kernal1 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04],
                    [0.04, 0.04, 0.04, 0.04, 0.04] ])

kernal2 = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])

smooth = cv2.filter2D(figure_3, -1, kernal1)
sharp = cv2.filter2D(figure_3, -1, kernal2)
enosion = cv2.dilate(binaryFig3, kernal1, iterations=2)

cv2.imshow('figure_3', figure_3)
cv2.imshow('smooth', smooth)
cv2.imshow('sharp', sharp)
cv2.imshow('enosion', enosion)


# Q8: When applying the previous code, the problem isn’t solved. Write a code to merge erosion and dilation, starting with dilation :
gray_Fig3 = cv2.cvtColor(figure_3, cv2.COLOR_BGR2GRAY)
(thresh, binaryFig3) = cv2.threshold(gray_Fig3,127, 255, cv2.THRESH_BINARY)
kernal = np.ones((5, 5), np.uint8)  #create kernal
dilation = cv2.dilate(binaryFig3, kernal, iterations=2)
cv2.imshow('dilation', dilation)




 




cv2.waitKey(0)
cv2.destroyAllWindows()
