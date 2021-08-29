import tkinter as tk
from tkinter import ttk
import TakePhoto as tp
import cv2
import PIL
from PIL import ImageTk
from PIL import Image
import Cartoon
import Paint
import Sketch
import os

class GUI():
    def __init__(self, master):
        self.tphoto = tp.TakePhoto("Screenshot")
        self.tphoto.vid()
        self.photo = cv2.imread("./Screenshot.jpeg")
        self.h, self.w, self.c = self.photo.shape
        
        self.imagePanel = tk.Frame(master)
        self.imagePanel.grid(row=0, column=0)
        
        
        self.controlPanel = tk.Frame(master)
        self.controlPanel.grid(row=0, column=1)
        
        
        self.imageP(self.h,self.w)
        self.ctrlP(self.h/2, 200, 0, 0, 0)
        self.ctrlP(self.h/2, 200, 0, 1, 1)
        
        
    def imageP(self,height, width):
        self.frame = tk.Frame(self.imagePanel, border = 8)
        self.frame.grid(row=0, column=0)
        self.canvas = tk.Canvas(self.frame,width=width, height=height, borderwidth=0, highlightthickness=0, bg="grey")
        
        self.canvas.pack()
        self.photo = ImageTk.PhotoImage(Image.open("./Screenshot.jpeg"))
        self.canvas.create_image(0,0, anchor="nw", image=self.photo)
        
    def ctrlP(self, height, width, col, row, version):
        self.frame = tk.Frame(self.controlPanel, border = 8)
        self.frame.grid(row=row, column=col)
        self.cp = tk.Frame(self.frame, width=width, height=height)
        self.cp.pack()
        if version == 1:
            self.createButtons()
        else:
            self.createCbox()
        
    def createButtons(self):
        self.label1 = tk.Label(self.cp, text="Do you have a picture you \nwant to manipulate? \ntype in the directory "
                                             "here!")
        self.label1.place(relx=0.5, rely=0.1, anchor="center")

        self.tBox = tk.Text(self.cp, bg="white", height=1, width=20)
        self.tBox.place(relx=0.5, rely=0.3, anchor="center")

        self.loadImageButton = tk.Button(self.cp, text="LoadImage")
        self.loadImageButton["command"] = self.loadImageButtonPressed
        self.loadImageButton.place(relx=0.5, rely=0.4, anchor="center")

        self.takePhotoButton = tk.Button(self.cp, text="Re-take Photo")
        self.takePhotoButton["command"] = self.takePhoto
        self.takePhotoButton.place(relx=0.5, rely=0.8, anchor="center")



        
        
    def createCbox(self):
        self.label2 = tk.Label(self.cp, text="Choose the picture style!")
        self.label2.place(relx=0.5, rely=0.1, anchor="center")
        self.comboBox = ttk.Combobox(self.cp, textvariable=tk.StringVar())
        self.comboBox['values'] = ('Original', 'Cartoon', 'Sketch', 'Paint')
        self.comboBox.current(0)
        self.comboBox.place(relx=0.5, rely=0.2, anchor="center")
        
        self.changeButton = tk.Button(self.cp, text="Change Style")
        self.changeButton["command"] = self.changeButtonPressed
        self.changeButton.place(relx=0.5, rely=0.5, anchor="center")
        
    def takePhoto(self):
        self.labelWarning.destroy()
        self.tphoto.vid()
        self.changeImage("Screenshot")
        
    def changeImage(self, photoName):
        for image in self.canvas.winfo_children():
            image.destroy()
            
        self.newPhoto = ImageTk.PhotoImage(Image.open("./"+photoName+".jpeg"))
        self.canvas.create_image(0,0, anchor="nw", image=self.newPhoto)
    
    def changeButtonPressed(self):
        boxStr = self.comboBox.get()
        self.labelWarning.destroy()
        
        if boxStr == "Original":
            self.changeImage("Screenshot")
        elif boxStr == "Paint":
            paint = Paint.Paint()
            paint.createImage()
            self.changeImage("Paint")
        elif boxStr == "Sketch":
            sketch = Sketch.Sketch()
            sketch.createImage()
            self.changeImage("Sketch")
        else:
            cart = Cartoon.Cartoon()
            cart.createImage()
            self.changeImage("Cartoon")
            
        
    def loadImageButtonPressed(self):
        txtStr = self.tBox.get(1.0, tk.END+"-1c")
        if os.path.isfile(txtStr):
            if txtStr[-4:] == "jpeg" or txtStr[-3] == "jpg":
                img = cv2.imread(txtStr)
                cv2.imwrite("./Screenshot.jpeg", img)
                self.changeImage("Screenshot")
                self.labelWarning.destroy()
            else:
                self.labelWarning = tk.Label(self.cp, text="This software only supports jpeg or jpg type")
                self.labelWarning.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.labelWarning = tk.Label(self.cp, text="Directory entered does not exist")
            self.labelWarning.place(relx=0.5, rely=0.5, anchor="center")



