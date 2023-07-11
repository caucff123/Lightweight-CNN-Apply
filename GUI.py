#coding:utf-8
import tkinter as tk
import numpy as np
from tkinter import Button, LEFT
from tkinter.filedialog import askopenfile
import pandas as pd
from PIL import Image,ImageTk
windows=tk.Tk()
windows.title('草莓病害严重度估算系统')

canvas = tk.Canvas(windows, width=1200,height=699,bd=0, highlightthickness=0)
image=Image.open('EfficientNet/R-C.png')
photo = ImageTk.PhotoImage(image,master=windows)

canvas.create_image(700, 500, image=photo)
canvas.pack()

Buttonframe=tk.Frame(windows)
Buttonframe.pack(anchor='nw')
b1=tk.Button(Buttonframe,text='上传图片',activebackground='red')
b1.grid(row=0,column=0)
b2=tk.Button(Buttonframe,text='计算严重度',activebackground='red')
b2.grid(row=1,column=0)




windows.mainloop()