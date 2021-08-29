import cv2
import numpy as np


class Sketch:
    def __init__(self):
        pass
    
    def createImage(self):
        image = cv2.imread("./Screenshot.jpeg")
        
        img1, img2 = cv2.pencilSketch(image, sigma_s=45, sigma_r=0.1, shade_factor=0.02)
        
        cv2.imwrite("Sketch.jpeg",img1)
        