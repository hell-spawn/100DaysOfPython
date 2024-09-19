import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg

img=plt.imread("../data/27295659492.jpg")

#img=plt.imread("../data/demo.jpg")
#print(type(img)) #numpy.ndarray
print(img[0,0,:])
print(img.shape)
#plt.imshow(img)
#plt.show()

img_array = img / 255

print(img_array.max(), img_array.min())
print(img_array.dtype)

red_array = img_array[:, :, 0]
green_array = img_array[:, :, 1]
blue_array = img_array[:, :, 2]

print(img[0,0,:])
print(img_array[0,0,:])
print(red_array[0, 0:3 ])

#plt.imshow(red_array, cmap="Reds")
#plt.show()
#
#plt.imshow(green_array, cmap="Greens")
#plt.show()
#
#plt.imshow(blue_array, cmap="Blues")
#plt.show()

img_gray = img_array @ [0.2126, 0.7152, 0.0722]
print(img_gray.shape)
print(img_gray[0,])

#plt.imshow(img_gray, cmap="gray")
#plt.show()

U, s, Vt = linalg.svd(img_gray)

print(U.shape, s.shape, Vt.shape)

