import cv2



suits = cv2.VideoCapture('suits.mp4')

# fps = suits.get(cv2.CAP_PROP_FPS)
# size = (int(suits.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(suits.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# fourcc = cv2.VideoWriter_fourcc(*'I630')
# V_Write=cv2.VideoWriter('suits_out.mp4', fourcc , fps, size)


# if not suits.isOpened():
#     print("Error opening video file")

# success, frame = suits.read()

# if not success:
#     print("Error reading frame from video file")

# while True:
#     isTrue, frame = suits.read()  
#     cv2.imshow('video', frame)
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break  
#     # V_Write.write(frame)  

# suits.release()
# cv2.destroyAllWindows()
# # V_Write.release()
# # cv2.waitKey(5000)


# ===========   rescale  video  ==========================

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =(width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(width, height):
    videoPlay.set(3,width)
    videoPlay.set(4,height)
    

videoPlay = cv2.VideoCapture('play.mp4')

if not videoPlay.isOpened:
    print("Error opening video file")
    

while True:
    success ,frame=videoPlay.read()

    if not success:
        print("Error reading frame from video file")
        
    
    frame_resized = rescaleFrame(frame)
    
    cv2.imshow('video' ,frame)
    cv2.imshow('video resized' ,frame_resized)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

videoPlay.release()
cv2.destroyAllWindows()