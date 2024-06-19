import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
# giving the camera access
camera  = cv2.VideoCapture(0)

#declaring the variables as none
firstFrame = None
gun_exist = None

#implementing an infinite true 
while True:
# making the camera to read the image shown
  ret, frame = camera.read()
  
# resizing the image shown into required width
  frame = imutils.resize(frame , width = 500)
# converting the BGR color to gray color
  gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
# detecting multiscale of the image we are having
  gun = gun_cascade.detectMultiScale(gray, 1.3,5,minSize= (100,100))
# conditions
  if len(gun)>0:
    gun_exist = True
  
  for (x,y,w,h) in gun:
# setting up the rectangular frame    
    frame = cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0),2)
    
    roi_gray = gray[y: y + h , x: x + w]
    roi_color = frame[y : y + h , x : x + w]
    
    
  if firstFrame is None:
    firstFrame = gray
    continue
  
  cv2.imshow(" Security feed", frame)
  key = cv2.waitKey(1) & 0xFF
  
  if key == ord('q'):
    break
  
if gun_exist :
  print("Guns Detected")
  
else:
  print(" Guns didn't detected")
  
# closing the camera 
camera.release()
# closing all the windows
cv2.destroyAllWindows()