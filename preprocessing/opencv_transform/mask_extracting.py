import numpy as np
import cv2

def extract_mask(cv_mask: cv2.Mat):
    """Returns b&w mask"""

    #Create a total green image
    green = np.zeros((512,512,3), np.uint8)
    green[:,:,:] = (0,255,0)      # (B, G, R)
    white = np.ones((512,512,3), np.uint8)
    white[:,:,:] = (255,255,255)      # (B, G, R)

    #Define the green color filter
    f1 = np.asarray([0, 250, 0])   # green color filter
    f2 = np.asarray([10, 255, 10])
    
    #From mask, extrapolate only the green mask		
    green_mask = cv2.inRange(cv_mask, f1, f2) #green is 0

    # (OPTIONAL) Apply dilate and open to mask
    kernel = np.ones((5,5),np.uint8) #Try change it?
    green_mask = cv2.dilate(green_mask, kernel, iterations = 1)

    return green_mask
    # return cv2.bitwise_and(white, white, mask = green_mask)

