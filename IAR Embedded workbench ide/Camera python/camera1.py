# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PIL import Image
#ImageFile='home/pi/Documents/essai_belleudy/Camera/image1.jpg'
ImageFile='image1.jpg'
img=Image.open(ImageFile)
imgflou=img
imgout=img

#print('hello')
#img.format, img.size, img.mode)
#img.show()
print (img.format, img.size, img.mode)
#img.show()
colonne,ligne=img.size
print(colonne,ligne)
for i in range(ligne):
    for j in range(colonne):
        pixel=img.getpixel((j,i))
        p=(0,pixel[1],0)
        img.putpixel((j,i),p)
#création image flou
for i in range(ligne):
    for j in range(colonne):
        pixel=img.getpixel((j,i))
        p=(0,pixel[1],0)
        img.putpixel((j,i),p)   
#detection contour
for i in range(ligne):
    for j in range(colonne):
        pixel=img.getpixel((j,i))
        pixel2=imgflou
        p=(0,pixel[1],0)
        img.putpixel((j,i),p)   
        
img.show()
