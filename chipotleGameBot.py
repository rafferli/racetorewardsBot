# Chipotle Race to Rewards Bot
# https://racetorewards.com/

from PIL import ImageGrab, ImageOps, Image
from pyautogui import press
import time
import cv2
import numpy as np
import keyboard

# define blue color range
lower_val_b = np.array([0,80,0]) 
upper_val_b = np.array([107,255,255]) 

# define green color range
lower_val_g = np.array([45,173,198]) 
upper_val_g = np.array([62,179,215])

# define yellow color range
lower_val_y = np.array([30,60,200]) 
upper_val_y = np.array([90,80,250])


# define GUAC color range
lower_val_guac = np.array([101,133,78]) 
upper_val_guac = np.array([135,234,255])

# define SLIDE color range
lower_val_s = np.array([101,21,0])
upper_val_s = np.array([179,45,73])


# we're gonna swap between lanes 2 and 3 cause it works :/
lane2Okay = True
lane3Okay = True

#change to whatever lane the car will be in when the game starts
currentLane = 2

time.sleep(5)

print("bot starting...")
while True:

        #pixel def example: bbox=('LEFT SIDE X', 100, 'RIGHT SIDE X', 500)

        #for lane 2
        img2 =  np.array(ImageGrab.grab(all_screens=True, bbox=(877, 100, 1052, 500)))

        #for lane 3
        img3 =  np.array(ImageGrab.grab(all_screens=True, bbox=(1072, 100, 1261, 500)))
        
        hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

        #find threshold, any pixels that light up means we have a match

        #color masks
        mask_b2 = cv2.inRange(hsv2, lower_val_b, upper_val_b)
        mask_g2 = cv2.inRange(hsv2, lower_val_g, upper_val_g)
        mask_y2 = cv2.inRange(hsv2, lower_val_y, upper_val_y)
        
        mask_guac2 = cv2.inRange(hsv2, lower_val_guac, upper_val_guac)
        mask_s2 = cv2.inRange(hsv2, lower_val_s, upper_val_s)

        #color masks
        mask_b3 = cv2.inRange(hsv3, lower_val_b, upper_val_b)
        mask_g3 = cv2.inRange(hsv3, lower_val_g, upper_val_g)
        mask_y3 = cv2.inRange(hsv3, lower_val_y, upper_val_y)

        mask_guac3 = cv2.inRange(hsv3, lower_val_guac, upper_val_guac)
        mask_s3 = cv2.inRange(hsv3, lower_val_s, upper_val_s)


        #LANE2
        if (np.sum(mask_b2) + np.sum(mask_g2) + np.sum(mask_y2)) > 0:
            lane2Okay = False
            print("Object in Lane 2")
        else:
            lane2Okay = True

        #LANE3
        if (np.sum(mask_b3) + np.sum(mask_g3) + np.sum(mask_y3)) > 0:
            lane3Okay = False
            print("Object in Lane 2")
        else:
            lane3Okay = True


        # checks to see if the object is a bonus item. collets item if it is
        l2good = np.sum(mask_guac2) + np.sum(mask_s2)
        if l2good:
                lane2Okay = True
                time.sleep(.1)
        l3good = np.sum(mask_guac3) + np.sum(mask_s3)
        if l3good:
                lane3Okay = True
                time.sleep(.1)

        #move lane if necessary
        if currentLane == 2:
            if lane2Okay == False:
                press("right")
                currentLane = 3
        if currentLane == 3:
            if lane3Okay == False:
                press("left")
                currentLane = 2

        

