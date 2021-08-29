import cv2
import numpy as np


class Cartoon:
    def __init__(self):
        pass
    
    def createImage(self):
        image = cv2.imread("./Screenshot.jpeg")
        cartoon = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)
        cv2.imwrite("Cartoon.jpeg",cartoon)