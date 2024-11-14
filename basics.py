# import numpy as np

# # Create a 2D array
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# # Print the array
# print(arr)

# # Perform some basic operations
# print(arr + 2)  # Add 2 to each element
# print(arr * 2)  # Multiply each element by 2
# print(arr ** 2)  # Square each element

# ---------------------------------------------------------------

import cv2


# mems_gray = cv2.imread('mems.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Grayscale  image', mems_gray)


# mems_reduced_2 = cv2.imread('mems.png', cv2.IMREAD_REDUCED_COLOR_2)
# cv2.imshow('Reduced Color Image', mems_reduced_2)


# mems_reduced_8 = cv2.imread('mems.png', cv2.IMREAD_REDUCED_COLOR_8)
# cv2.imshow('image', mems_reduced_8)

# road = cv2.imread('road.jpg')
# cv2.imwrite('way.png', road)
 
image = cv2.imread('road.jpg')

road_blur = cv2.GaussianBlur(image, (7, 7), 0)
# cv2.imshow('Blurred Road Image', road_blur)

cascade_7 = cv2.Canny(image, 70, 70)
cascade_10 = cv2.Canny(image, 100, 100)
cascade_20 = cv2.Canny(image, 200, 200)
# cv2.imshow('Cascade Image 70', cascade_7)
# cv2.imshow('Cascade Image 100', cascade_10)
# cv2.imshow('Cascade Image 200', cascade_20)

dilated = cv2.dilate(cascade_10, (3, 3), iterations=1 )
# cv2.imshow('dilated Image ', dilated)

eroded = cv2.erode(dilated, (5, 5), iterations=1 )
# cv2.imshow('eroded Image ', eroded)

resize = cv2.resize(image, (300, 600), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('resize Image ', resize)

croped = image[50:200, 200:400]
# cv2.imshow('croped Image ', croped)





cv2.waitKey(0)
cv2.destroyAllWindows()
