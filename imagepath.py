# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 09:45:13 2015

@author: Django
"""
#IRENE NANDUTU JAN15/COMP/0573U
#from skimage import data, io, filter
import matplotlib.pyplot as plt
import os
import numpy as np
from array import array
#from skimage import color



# get the path to the script so we can use relative paths
full_path = os.path.realpath(__file__)
script_path, file = os.path.split(full_path)
sep = os.path.sep

#getting the path to the image
path_to_image = script_path + sep + 'pants.jpg'
image = plt.imread(path_to_image).astype(np.float32)

#putting lines with in the image
image[10:13, 20:23]
image[100:120] = 255

#this creates a circular shape with curved edge at y-axis and x-axis
#lx, ly = image.shape
#X, Y = np.ogrid[0:lx, 0:ly]
#mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
#image[mask] = 0

#passing the and passing the line between an x-axis and y-axis
#while measuring the width and height dimensions of the image
image[range(200), range(200)] = 255


# Jpeg has values of 0-255 we need values normalized of 0.0 - 1.0
image = image/255

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
