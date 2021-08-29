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
        self.takePhotoButton = tk.Button(self.cp, text="Re-take Photo")
        self.takePhotoButton["command"] = self.takePhoto
        self.takePhotoButton.place(relx=0.5, rely=0.8, anchor="center")
        
        
    def createCbox(self):
        self.label = tk.Label(self.cp, text="Choose the picture style!")
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        self.comboBox = ttk.Combobox(self.cp, textvariable=tk.StringVar())
        self.comboBox['values'] = ('Original', 'Cartoon', 'Sketch', 'Paint')
        self.comboBox.current(0)
        self.comboBox.place(relx=0.5, rely=0.2, anchor="center")
        
        self.changeButton = tk.Button(self.cp, text="Change Style")
        self.changeButton["command"] = self.changeButtonPressed
        self.changeButton.place(relx=0.5, rely=0.5, anchor="center")
        
    def takePhoto(self):
        self.tphoto.vid()
        self.changeImage("Screenshot")
        
    def changeImage(self, photoName):
        for image in self.canvas.winfo_children():
            image.destroy()
            
        self.newPhoto = ImageTk.PhotoImage(Image.open("./"+photoName+".jpeg"))
        self.canvas.create_image(0,0, anchor="nw", image=self.newPhoto)
    
    def changeButtonPressed(self):
        boxStr = self.comboBox.get()
        print(boxStr)
        
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
            
        
        