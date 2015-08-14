# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 09:45:13 2015

@author: Django
"""
#IRENE NANDUTU JAN15/COMP/0573U
from skimage import data, io, filter
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage import color


image = data.coins() # or any NumPy array!

#putting lines with in the image
image[10:13, 20:23]
image[100:120] = 255

#this creates a circular shape with curved edge at y-axis and x-axis
lx, ly = image.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
image[mask] = 0
image[range(303), range(303)] = 255

#This resizes the image
plt.figure(figsize=(3, 3))
#this makes the middle grid pure white
plt.axes([0, 0, 1, 1])
#this makes the circular part grey
plt.imshow(image, cmap=plt.cm.gray)
#this removes the axis
plt.axis('off')
#displays the image
plt.show()

#This is the core code that calls the scikit image coins
#edges = filter.sobel(image)
#io.imshow(edges)
#io.show()
