import cv2

detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img=cv2.VideoCapture("Elonmusk.jpg")
res,img=imp_img.read()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#for detecting face 1st gray scale img,resizing command,minNeighbor
faces = detect.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces:
    # 4 parameter 1st x,y coordinate,2nd width & height,3rd color,4th width of img
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
    #for showing img
cv2.imshow("Elon Musk",img)
#till when img stable at 0 it will be stable
cv2.waitKey(0)
#release the img we have capture
imp_img.release()
#destroy window
cv2.destroyAllWindows()
