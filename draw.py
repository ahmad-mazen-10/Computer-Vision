import cv2
import numpy as np

height, width = 400, 400 
box = np.zeros((height, width, 3), dtype='uint8')
# cv2.imshow('Blank',blank)

# box[100:300, 100:700] = 0, 255, 255
# cv2.imshow('Box', box)


#    Draw a Regtangle 
cv2.rectangle(box,(10,10),(box.shape[1]//2,box.shape[0]//2 ),(0,255,255), thickness=2)
# cv2.imshow('reg', box)


# Draw Circle
center_coordinates = (box.shape[1] // 2, box.shape[0] // 2)  # Center of the image
radius = 40  
color = (0, 255, 255)
thickness = -3  # Thickness of the circle outline

cv2.circle(box, center_coordinates, radius, color, thickness)
# cv2.imshow('circle',  box)


# Draw Line
cv2.line(box, (40,40),(box.shape[1] // 2, box.shape[0] // 2), (255, 255, 255), thickness=3)
# cv2.imshow('line',  box)


# write text
text = 'WoW'
position = (255, 255)
font = cv2.FONT_HERSHEY_SIMPLEX 
font_scale = 1  
font_color = (255, 255, 255)  
thickness = 2  # Thickness of the text
line_type = cv2.LINE_AA  

cv2.putText(box, text, position, font, font_scale, font_color, thickness, line_type)
cv2.imshow('Shapes and Text', box)

cv2.waitKey(0)
cv2.destroyAllWindows()
