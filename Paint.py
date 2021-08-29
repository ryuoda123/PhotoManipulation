import cv2
import numpy as np


class Paint:
    def __init__(self):
        pass
    
    def createImage(self):
        image = cv2.imread("./Screenshot.jpeg")
        
        paint = cv2.stylization(image, sigma_s=45, sigma_r=0.05)
        
        cv2.imwrite("Paint.jpeg",paint)