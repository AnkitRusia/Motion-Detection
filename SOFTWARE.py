import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Smart_Recorder.avi',fourcc,20.0,(640,480))
while True :
       got_pixels = 0
       _, frame = cap.read()
       fgmask = fgbg.apply(frame)
       cv2.imshow('frame',frame)
       cv2.imshow('mask',fgmask)
       analytic = np.asarray(fgmask)
       
       for i in analytic :
              for j in i :
                     if j > 100:
                            got_pixels += 1
                            
       if (got_pixels/307200) > 0.03 :
              out.write(frame)
              time.sleep(0.001)
       if cv2.waitKey(1) & 0xff == ord('q') :
          print("pressed quit")
          break

cap.release()
out.release()
cv2.destroyAllWindows()


